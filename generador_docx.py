"""
Módulo para generar el informe atencional en formato DOCX.
"""
from __future__ import annotations

import os
from datetime import datetime
from typing import Iterable, List, Optional
import math
import io
import math
import io
from docx.oxml.ns import qn, nsdecls
from docx.oxml import OxmlElement, parse_xml
from PIL import Image, ImageDraw, ImageFont
from docx import Document
from docx.shared import Pt, Inches, RGBColor, Emu, Cm, Mm
from docx.enum.table import WD_CELL_VERTICAL_ALIGNMENT
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx.enum.section import WD_ORIENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt, RGBColor
from PIL import Image

from textos import (
    PARRAFOS_FIJOS,
    PARRAFO_ACS_atenciongeneral,
    PARRAFO_ACS_cambio,
    PARRAFO_ACS_foco,
    PARRAFO_ANT_A,
    PARRAFO_ANT_C,
    PARRAFO_ANT_F,
    PARRAFO_ANT_O,
    PARRAFO_ANT_TR,
    PARRAFO_ANT_alerta,
    PARRAFO_ANT_ejecutivo,
    PARRAFO_ANT_orientacion,
    PARRAFO_CPT_C,
    PARRAFO_CPT_CON,
    PARRAFO_CPT_O,
    PARRAFO_CPT_TR,
    PARRAFO_CPT_VAR,
    PARRAFO_DUALTASK_A,
    PARRAFO_DUALTASK_C,
    PARRAFO_DUALTASK_O,
    PARRAFO_DUALTASK_PSV,
    PARRAFO_DUALTASK_PSV_cuando_concurrencia,
    PARRAFO_DUALTASK_Rendimiento_General_cuando_concurrencia,
    PARRAFO_DUALTASK_TR,
    PARRAFO_DUALTASK_TR_A_vs_C,
    PARRAFO_DUALTASK_si_inestable,
    PARRAFO_DUALTASK_Fatiga,
    PARRAFO_DUALTASK_automatización,
    PARRAFOS_CONDICIONALES_OPCIONALES_DUALTASK,
    PARRAFO_DUALTASK_General_PSV_y_A,
    PARRAFO_DUALTASK_final_dif_TR_A_y_C,
    PARRAFO_DigitsMemorization,
    PARRAFO_FourFigures_A,
    PARRAFO_FourFigures_C,
    PARRAFO_FourFigures_P4_A_obtenido_vs_esperado,
    PARRAFO_FourFigures_TR,
    PARRAFO_sintesis_arousal,
    PARRAFO_sintesis_atencionsostenida,
    PARRAFO_sintesis_controlejecutivo,
    PARRAFO_sintesis_flexibilidadcognitiva,
    PARRAFO_sintesis_memoriatrabajo,
    PARRAFO_sintesis_velocidadprocesamiento,
    PARRAFO_sintesis_final
)

TABLE_SLOTS = ['ACS', 'ANT', 'CPT', 'FourFigures', 'DUALTASK', 'DigitsMemorization']
RAW_LOW_IS_BETTER = {
    'ANT_C', 'ANT_O', 'ANT_TR', 'ANT_TR_alerta', 'ANT_TR_orientacion', 'ANT_TR_ejecutivo',
    'CPT_O', 'CPT_C', 'CPT_VAR',
    'FourFigures_C', 'FourFigures_TR',
    'DUALTASK_C', 'DUALTASK_O', 'DUALTASK_TR',
}

# Utilidades generales
# ---------------------------------------------------------------------------

# A continuación se añaden líneas eliminadas en el último pull request y que se cree eran necesarias para generar el formato de informe deseado.


def _rgb_to_hex(color_tuple):
    """Convierte (r,g,b) a string hex sin #."""
    return '{:02X}{:02X}{:02X}'.format(*color_tuple)


def _set_cell_bg(cell, color_hex):
    """Establece el color de fondo de una celda de tabla."""
    tc   = cell._tc
    tcPr = tc.get_or_add_tcPr()
    shd  = OxmlElement('w:shd')
    shd.set(qn('w:val'),   'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'),  color_hex)
    tcPr.append(shd)


def _set_cell_borders(cell, top=None, bottom=None, left=None, right=None):
    """Establece bordes individuales en una celda."""
    tc   = cell._tc
    tcPr = tc.get_or_add_tcPr()
    tcBorders = OxmlElement('w:tcBorders')
    for side, val in [('top', top), ('bottom', bottom),
                      ('left', left), ('right', right)]:
        if val is not None:
            el = OxmlElement(f'w:{side}')
            el.set(qn('w:val'),   val.get('val',   'single'))
            el.set(qn('w:sz'),    str(val.get('sz', 4)))
            el.set(qn('w:space'), '0')
            el.set(qn('w:color'), val.get('color', '000000'))
            tcBorders.append(el)
    tcPr.append(tcBorders)


def _no_space_before_after(para):
    """Elimina espaciado antes/después de un párrafo."""
    pPr = para._p.get_or_add_pPr()
    spacing = OxmlElement('w:spacing')
    spacing.set(qn('w:before'), '0')
    spacing.set(qn('w:after'),  '0')
    pPr.append(spacing)


def _add_bold_paragraph(doc, text):
    """Añade un párrafo con texto en negrita y espaciado compacto."""
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(2)
    run = p.add_run(text.strip())
    run.bold = True
    return p

def _fmt(resultados, nombre):
    """Devuelve un dict de formato para .format() en los textos."""
    return {'nombre': nombre, 'nombre_completo': resultados.get('nombre_completo', nombre)}

def _get_text(diccionario, clave, fmt):
    """Obtiene, limpia y formatea el texto si la clave existe en el diccionario."""
    texto = diccionario.get(clave)
    if texto:
        texto = texto.strip()
        try:
            return texto.format(**fmt)
        except (KeyError, IndexError):
            return texto
    return None

def _add_group(doc, *text_items):
    """Añade múltiples textos opcionales como párrafos independientes."""
    texts = [t for t in text_items if t]
    for text in texts:
        doc.add_paragraph(text)

def _remove_table_borders(table):
    """Elimina todos los bordes visibles de una tabla."""
    tbl   = table._tbl
    tblPr = tbl.tblPr
    if tblPr is None:
        tblPr = OxmlElement('w:tblPr')
        tbl.insert(0, tblPr)
    tblBorders = OxmlElement('w:tblBorders')
    for side in ('top', 'left', 'bottom', 'right', 'insideH', 'insideV'):
        el = OxmlElement(f'w:{side}')
        el.set(qn('w:val'),   'none')
        el.set(qn('w:sz'),    '0')
        el.set(qn('w:space'), '0')
        el.set(qn('w:color'), 'auto')
        tblBorders.append(el)
    tblPr.append(tblBorders)


def _cargar_fuente_pil(tamanio):
    """Carga una fuente TrueType para PIL o retorna la fuente por defecto."""
    rutas = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
        "arial.ttf",
        "C:/Windows/Fonts/arial.ttf",
    ]
    for ruta in rutas:
        try:
            return ImageFont.truetype(ruta, tamanio)
        except Exception:
            pass
    return ImageFont.load_default()


def _set_cell_bg(cell, color_hex: str) -> None:
    tc_pr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:fill'), color_hex)
    tc_pr.append(shd)


def _fmt_num(value) -> str:
    if value is None:
        return '-'
    if isinstance(value, float):
        return f"{value:.3f}".rstrip('0').rstrip('.')
    return str(value)


def _bar(value: Optional[int]) -> str:
    if value is None:
        return '░░░░░░░░░░'
    blocks = max(0, min(10, round(value / 10)))
    return '█' * blocks + '░' * (10 - blocks)


def _image_is_valid(path: str) -> bool:
    if not os.path.exists(path):
        return False
    try:
        with Image.open(path) as img:
            img.verify()
        return True
    except Exception:
        return False


def _add_heading(doc: Document, text: str, size: int = 12) -> None:
    p = doc.add_paragraph()
    p.alignment = WD_PARAGRAPH_ALIGNMENT.LEFT
    run = p.add_run(text)
    run.bold = True
    run.font.size = Pt(size)


def _add_paragraph(doc: Document, text: Optional[str], **fmt) -> None:
    if not text:
        return
    try:
        doc.add_paragraph(text.format(**fmt))
    except KeyError:
        doc.add_paragraph(text)


def _safe_dict_text(diccionario: dict, key: Optional[str], fallback: Optional[str] = None) -> Optional[str]:
    if key in diccionario:
        return diccionario[key]
    if fallback is not None:
        return fallback
    return None


def _raw_level(nivel: Optional[str], reverse_metric: bool = False) -> Optional[str]:
    if not reverse_metric or nivel is None:
        return nivel
    return {'alto': 'bajo', 'bajo': 'alto', 'normal': 'normal', 'N/D': None}.get(nivel, nivel)


def _formatear_fecha_aplicacion(valor) -> Optional[str]:
    """Devuelve la fecha y hora de aplicación en formato DD/MM/YYYY HH:MM."""
    if valor is None:
        return None

    try:
        if isinstance(valor, str):
            valor = valor.strip()
            if not valor:
                return None
            if 'T' in valor:
                dt = datetime.fromisoformat(valor.replace('Z', '+00:00'))
            else:
                try:
                    dt = datetime.strptime(valor, '%d/%m/%Y %H:%M')
                except ValueError:
                    try:
                        dt = datetime.strptime(valor, '%d/%m/%Y')
                    except ValueError:
                        dt = datetime.fromisoformat(valor)
        elif hasattr(valor, 'strftime'):
            dt = valor
        else:
            return str(valor)

        if dt.tzinfo is not None:
            dt = dt.astimezone().replace(tzinfo=None)

        return dt.strftime('%d/%m/%Y %H:%M')
    except Exception:
        return str(valor)


def agregar_portada(doc: Document, nombre_completo: str, datos: dict) -> None:
    """
    Agrega la portada del informe.

    Args:
        doc: Documento de Word.
        nombre_completo: Nombre completo del encuestado.
        datos: Diccionario con datos generales (edad, fecha_aplicacion, etc.)
    """
    titulo = doc.add_heading('Prueba de Evaluación Atencional', 0)
    titulo.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
    for run in titulo.runs:
            run.font.size = Pt(24)

    doc.add_paragraph().add_run().add_break()

    info = doc.add_paragraph()
    info.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
    run_nombre = info.add_run(f"Nombre del encuestado: {nombre_completo}\n")
    run_nombre.bold = True
    run_nombre.font.size = Pt(14)

    if datos.get('edad'):
        run_edad = info.add_run(f"Edad: {datos['edad']} años\n")
        run_edad.font.size = Pt(14)
    if datos.get('fecha_aplicacion'):
        fecha_aplicacion_formateada = _formatear_fecha_aplicacion(datos['fecha_aplicacion'])
        if fecha_aplicacion_formateada:
            run_fa = info.add_run(f"Fecha de aplicación: {fecha_aplicacion_formateada}\n")
            run_fa.font.size = Pt(14)

    fecha_actual = datetime.now().strftime("%d/%m/%Y")
    run_fi = info.add_run(f"Fecha del informe: {fecha_actual}\n")
    run_fi.font.size = Pt(14)

    doc.add_paragraph().add_run().add_break()

    nota = doc.add_paragraph()
    nota.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
    run_n = nota.add_run(
        f"Informe de evaluación atencional obtenido a partir de las declaraciones "
        f"de {nombre_completo} en el cuestionario ACS y su rendimiento en las pruebas conductuales "
         "ANT, CPT, FourFigures, DigitsMemorization y Dual-Task."
    )
    run_n.italic = True
    run_n.font.size = Pt(12)

    doc.add_paragraph()
    nota.add_run("\n" + "─" * 50 + "\n")
    nota.add_run(
        "\nEste es un informe confidencial de carácter educativo y orientativo. "
        "No es un diagnóstico clínico. Su interpretación es conveniente realizarla "
        "con un profesional competente."
    ).font.size = Pt(11)


# ---------------------------------------------------------------------------
# Función principal
# ---------------------------------------------------------------------------

def crear_informe_docx(resultados, clasificaciones, nombre_caso="caso",
                       script_dir=None):
    """
    Crea el documento Word con el informe de la evaluación atencional.

    Args:
        resultados:      Dict con puntuaciones, porcentajes e índices.
        clasificaciones: Dict con clasificaciones por factor.
        nombre_caso:     Nombre del evaluado (fallback).
        script_dir:      Directorio del script (para buscar imágenes).

    Returns:
        Document: Documento Word generado.
    """
    if script_dir is None:
        script_dir = os.path.dirname(os.path.abspath(__file__))

    doc = Document()

    for section in doc.sections:
        section.orientation = WD_ORIENT.PORTRAIT
        section.page_width = Mm(210)
        section.page_height = Mm(297)
        page_size = section._sectPr.pgSz
        page_size.set(qn('w:w'), '11906')
        page_size.set(qn('w:h'), '16838')
        page_size.set(qn('w:orient'), 'portrait')
        section.top_margin    = Inches(0.5)
        section.bottom_margin = Inches(0.5)
        section.left_margin   = Inches(0.5)
        section.right_margin  = Inches(0.5)

    nombre_completo = resultados.get('nombre_completo') or nombre_caso
    nombre          = resultados.get('nombre')          or nombre_caso
    fmt             = {'nombre': nombre, 'nombre_completo': nombre_completo}

    datos_portada = {
        'edad':             resultados.get('edad'),
        'fecha_aplicacion': resultados.get('fecha_aplicacion'),
    }

    # ------------------------------------------------------------------ #
    # 1. PORTADA                                                           #
    # ------------------------------------------------------------------ #
    agregar_portada(doc, nombre_completo, datos_portada)
    doc.add_page_break()


    # ------------------------------------------------------------------ #
    # 2. DESCRIPCIÓN DE LA PRUEBA                                         #
    # ------------------------------------------------------------------ #
    _add_bold_paragraph(doc, PARRAFOS_FIJOS['titulo_general_prueba'])
    doc.add_paragraph(PARRAFOS_FIJOS['objetivo_prueba'].format(**fmt))

    doc.add_paragraph()
    _add_bold_paragraph(doc, PARRAFOS_FIJOS['titulo_procedimiento'])
    doc.add_paragraph(PARRAFOS_FIJOS['descripcion_procedimiento0'])
    doc.add_paragraph(PARRAFOS_FIJOS['descripcion_procedimiento1.1'])
    doc.add_paragraph(PARRAFOS_FIJOS['descripcion_procedimiento2.1'])
    imagen_ant = os.path.join(script_dir, 'imagenes', 'ANT estimulo central.png')
    if _image_is_valid(imagen_ant):
        parrafo_imagen_ant = doc.add_paragraph()
        parrafo_imagen_ant.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
        parrafo_imagen_ant.add_run().add_picture(imagen_ant, width=Inches(6))

    doc.add_paragraph(PARRAFOS_FIJOS['descripcion_procedimiento2.2'])
    imagen_ant = os.path.join(script_dir, 'imagenes', 'ANT estimulo contextual.png')
    if _image_is_valid(imagen_ant):
        parrafo_imagen_ant = doc.add_paragraph()
        parrafo_imagen_ant.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
        parrafo_imagen_ant.add_run().add_picture(imagen_ant, width=Inches(6))

    doc.add_paragraph(PARRAFOS_FIJOS['descripcion_procedimiento3.1'])
    imagen_ant = os.path.join(script_dir, 'imagenes', 'CPT estimulos.png')
    if _image_is_valid(imagen_ant):
        parrafo_imagen_ant = doc.add_paragraph()
        parrafo_imagen_ant.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
        parrafo_imagen_ant.add_run().add_picture(imagen_ant, width=Inches(6))

    doc.add_paragraph(PARRAFOS_FIJOS['descripcion_procedimiento4.1'])
    imagen_ant = os.path.join(script_dir, 'imagenes', 'FourFigures estimulos.png')
    if _image_is_valid(imagen_ant):
        parrafo_imagen_ant = doc.add_paragraph()
        parrafo_imagen_ant.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
        parrafo_imagen_ant.add_run().add_picture(imagen_ant, width=Inches(6))

    doc.add_paragraph(PARRAFOS_FIJOS['descripcion_procedimiento5.1'])
    doc.add_paragraph(PARRAFOS_FIJOS['descripcion_procedimiento6.1'])

    doc.add_page_break()
    _add_bold_paragraph(doc, PARRAFOS_FIJOS['titulo_indices'])
    doc.add_paragraph(PARRAFOS_FIJOS['descripcion_indices'].format(**fmt))

    # ------------------------------------------------------------------ #
    # 3. RESULTADOS                                                        #
    # ------------------------------------------------------------------ #
    doc.add_page_break()


    titulo_resumen = doc.add_paragraph()
    run = titulo_resumen.add_run(PARRAFOS_FIJOS['titulo_resultados'].format(nombre_completo=nombre_completo))
    titulo_resumen.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
    run.bold = True
    run.font.size = Pt(14)
    doc.add_paragraph()  # Espacio

    doc.add_paragraph(PARRAFOS_FIJOS['texto_resultados'].format(**fmt))

    # ========================================================================
    # INSERTAR Tabla resultados
    # ========================================================================
    available_tests = resultados.get('available_tests', [])
    agregar_tabla_indices(
        doc,
        resultados,
        clasificaciones,
        available_tests,
    )


    _add_textual_results_sections(doc, resultados, clasificaciones, nombre)

    return doc

import argparse
import itertools
import logging
import numbers
import random
import unicodedata

from docx import Document
from docx.enum.section import WD_ORIENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Twips

log = logging.getLogger(__name__)

# ═════════════════════════════════════════════════════════════════════════════
# 1. CONSTANTES DE FORMATO
# ═════════════════════════════════════════════════════════════════════════════

FUENTE = "Times New Roman"          # la del docx original
PT_MAX = 11.0                       # tamaño máximo del texto de la tabla
PT_MIN = 4.0                        # suelo: nunca se baja de aquí
MARGEN_CELDA = 20                   # margen interno izq./der. de celda (twips)

# Anchos de columna del docx original (twips). Suman 11483. Se reescalan
# proporcionalmente al ancho útil de la página.
COLS_BASE = [1276, 993, 496, 496, 993, 567, 567, 567, 1134, 992, 850, 993, 779, 780]
N_COLS = len(COLS_BASE)

# Colores de relleno (hex RRGGBB). Cámbialos aquí si quieres otros tonos.
COLOR_CABECERA = "A6A6A6"           # gris medio de las cabeceras
COLOR_NEGRO = "D9D9D9"              # gris claro de las celdas NEGRO
COLOR_ROJO = "FF5050"
COLOR_VERDE = "66CC66"
COLOR_AMARILLO = "FFFF00"

# Cabecera (se repite idéntica como última fila): (columna, span, texto)
CABECERA = [
    (0, 2, "Pruebas"),
    (2, 2, "Arousal"),
    (4, 2, "Atención Sostenida y Fatiga"),
    (6, 2, "Control ejecutivo"),
    (8, 1, "Atención Selectiva"),
    (9, 1, "Control inhibitorio (impulsividad)"),
    (10, 1, "Flexibilidad cognitiva"),
    (11, 1, "Memoria de Trabajo"),
    (12, 2, "Velocidad de procesamiento"),
]

# ═════════════════════════════════════════════════════════════════════════════
# 2. DEFINICIÓN DE LA REJILLA (una entrada por prueba)
# ═════════════════════════════════════════════════════════════════════════════
# Cada prueba ocupa 3 filas: Índice / PD / Rendimiento.
# Cada celda: (columna, span, etiqueta_indice, clave_PD, clave_clasificacion, tipo)
#   - etiqueta_indice: texto EXACTO del docx original (con sus '*'); 'NEGRO' =
#     celda bloqueada (se rellena de casi negro, sin texto, combinada en vertical).
#   - clave_PD / clave_clasificacion: claves en los dicts ``resultados`` y
#     ``clasificaciones``. Pueden ser una tupla de alias (se usa la primera que
#     exista). '{T}' se sustituye por el nombre de la prueba que esté disponible
#     (CPT/D2, FourFigures/FiveDigits).
#   - tipo (color de la fila Rendimiento):
#       'clasif' -> rojo si malo, verde si bueno, sin color si normal
#       'sign'   -> amarillo si 'sign'; sin color si 'no sign'
#       'signo'  -> rojo si Negativo/Bajo; verde si Positivo/Alto
NEGRO = "NEGRO"

BLOQUES = [
    {   # ── ANT ────────────────────────────────────────────────────────────
        "variantes": ("ANT",),
        "celdas": [
            (2, 2, "Red de alerta", ("PD_ANT_TR_alerta", "PD_ANT_TR_alert"), "ANT_TR_alerta", "clasif"),
            (4, 1, "Dif.* A*", "PD_ANT_A_principio_vs_final", "ANT_A_principio_vs_final", "sign"),
            (5, 1, "Dif TR*", "PD_ANT_TR_principio_vs_final", "ANT_TR_principio_vs_final", "sign"),
            (6, 1, "C*", "PD_ANT_C", "ANT_C", "clasif"),
            (7, 1, "Red ejecutiva", ("PD_ANT_TR_ejecutivo", "PD_ANT_red_ejecutiva", "PD_ANT_red_rejecutiva"), "ANT_TR_ejecutivo", "clasif"),
            (8, 1, "Red de orientación", "PD_ANT_TR_orientacion", "ANT_TR_orientacion", "clasif"),
            (9, 1, NEGRO),
            (10, 1, NEGRO),
            (11, 1, NEGRO),
            (12, 1, "O*", "PD_ANT_O", "ANT_O", "clasif"),
            (13, 1, "TR", "PD_ANT_TR", "ANT_TR", "clasif"),
        ],
    },
    {   # ── CPT o D2 (excluyentes) ─────────────────────────────────────────
        "variantes": ("CPT", "D2"),
        "celdas": [
            (2, 2, "CON*", "PD_{T}_CON", "{T}_CON", "clasif"),
            (4, 1, "Dif. A", ("PD_{T}_A_principio_vs_final", "PD_{T}_Dif_A"), "{T}_A_principio_vs_final", "sign"),
            (5, 1, "Dif. TR", ("PD_{T}_TR_principio_vs_final", "PD_{T}_Dif_TR"), "{T}_TR_principio_vs_final", "sign"),
            (6, 2, NEGRO),
            (8, 1, "O", "PD_{T}_O", "{T}_O", "clasif"),
            (9, 1, "C", "PD_{T}_C", "{T}_C", "clasif"),
            (10, 1, NEGRO),
            (11, 1, NEGRO),
            (12, 2, "N*", "PD_{T}_N", "{T}_N", "clasif"),
        ],
    },
    {   # ── FourFigures o FiveDigits (excluyentes) ─────────────────────────
        "variantes": ("FourFigures", "FiveDigits"),
        "celdas": [
            (2, 2, "A", "PD_{T}_A", "{T}_A", "clasif"),
            (4, 2, NEGRO),
            (6, 2, "C", "PD_{T}_C", "{T}_C", "clasif"),
            (8, 2, NEGRO),
            (10, 1, "Dif. P4*",
             "PD_{T}_P4_A_obtenido_vs_esperado",
             "{T}_P4_A_obtenido_vs_esperado", "signo"),
            (11, 1, NEGRO),
            (12, 2, "TR", "PD_{T}_TR", "{T}_TR", "clasif"),
        ],
    },
    {   # ── DualTask ───────────────────────────────────────────────────────
        "variantes": ("DualTask",),
        "celdas": [
            (2, 1, "O", "PD_DUALTASK_O", "DUALTASK_O", "clasif"),
            (3, 1, "PSV*", "PD_DUALTASK_PSV", "DUALTASK_PSV", "clasif"),
            (4, 1, "Dif. A", ("PD_DUALTASK_A_principio_vs_final", "PD_DUALTASK_Dif_A"), "DUALTASK_A_principio_vs_final", "sign"),
            (5, 1, "Dif. PSV", "PD_DUALTASK_PSV_principio_vs_final", "DUALTASK_PSV_principio_vs_final", "sign"),
            (6, 2, "C", "PD_DUALTASK_C", "DUALTASK_C", "clasif"),
            (8, 2, NEGRO),
            (10, 1, NEGRO),
            (11, 1, NEGRO),
            (12, 2, "TR", "PD_DUALTASK_TR", "DUALTASK_TR", "clasif"),
        ],
    },
    {   # ── DigitsMemorization ─────────────────────────────────────────────
        "variantes": ("DigitsMemorization",),
        "celdas": [
            (2, 2, NEGRO),
            (4, 1, NEGRO),
            (5, 1, NEGRO),
            (6, 2, NEGRO),
            (8, 1, NEGRO),
            (9, 1, NEGRO),
            (10, 1, NEGRO),
            (11, 1, "M", "PD_Digits_Memorization_M", "Digits_Memorization_M", "clasif"),
            (12, 2, NEGRO),
        ],
    },
]

# ═════════════════════════════════════════════════════════════════════════════
# 3. LÓGICA DE COLOR (fila 'Rendimiento')
# ═════════════════════════════════════════════════════════════════════════════

def _norm(valor):
    """minúsculas, sin acentos, sin puntos, espacios colapsados."""
    t = unicodedata.normalize("NFD", str(valor).strip().lower())
    t = "".join(ch for ch in t if unicodedata.category(ch) != "Mn")
    return " ".join(t.replace(".", " ").split())


def color_clasificacion(valor):
    """malo/bajo -> rojo · bueno/alto -> verde · normal -> sin color."""
    palabras = set(_norm(valor).split())
    if palabras & {"malo", "mala", "bajo", "baja"}:
        return COLOR_ROJO
    if palabras & {"bueno", "buena", "alto", "alta"}:
        return COLOR_VERDE
    return None


def color_sign(valor):
    """'sign' -> amarillo · 'no sign' -> sin color."""
    t = _norm(valor)
    if t.startswith("no"):          # 'no sign', 'no significativo'
        return None
    if t.startswith("sign"):        # 'sign', 'significativo'
        return COLOR_AMARILLO
    return None


def color_signo(valor):
    """Negativo/Negativa/Bajo -> rojo · Positivo/Positiva/Alto -> verde."""
    palabras = set(_norm(valor).split())
    if palabras & {"negativo", "negativa", "bajo", "baja"}:
        return COLOR_ROJO
    if palabras & {"positivo", "positiva", "alto", "alta"}:
        return COLOR_VERDE
    return None


_COLOR_POR_TIPO = {"clasif": color_clasificacion, "sign": color_sign, "signo": color_signo}

# ═════════════════════════════════════════════════════════════════════════════
# 4. DISPONIBILIDAD DE PRUEBAS Y RECUPERACIÓN DE DATOS
# ═════════════════════════════════════════════════════════════════════════════

def _clave_prueba(nombre):
    return _norm(nombre).replace(" ", "").replace("_", "").replace("-", "")


def resolver_pruebas(available_tests):
    """
    Devuelve [(bloque, nombre_prueba_mostrado), ...] solo con los bloques
    disponibles, en el orden de la rejilla. En los bloques con dos variantes
    excluyentes (CPT/D2, FourFigures/FiveDigits) se conserva únicamente la
    variante presente; si no hay ninguna, el bloque se omite.
    """
    disponibles = {_clave_prueba(t) for t in available_tests}
    resueltos = []
    for bloque in BLOQUES:
        presentes = [v for v in bloque["variantes"] if _clave_prueba(v) in disponibles]
        if len(presentes) > 1:
            log.warning("Se han indicado a la vez %s (son excluyentes); se usa '%s'.",
                        " y ".join(presentes), presentes[0])
        if presentes:
            resueltos.append((bloque, presentes[0]))
    return resueltos


def _buscar(dic, claves, prueba, defecto="-"):
    if isinstance(claves, str):
        claves = (claves,)
    for clave in claves:
        valor = dic.get(clave.format(T=prueba))
        if valor is not None:
            return valor
    return defecto


def _fmt_pd(valor):
    if isinstance(valor, numbers.Real) and not isinstance(valor, bool):
        return str(round(float(valor), 4))
    return str(valor)


def _fmt_significacion(valor):
    """Adapta clasificaciones de diferencias a las etiquetas de la tabla."""
    normalizado = _norm(valor)
    if normalizado in {'sign', 'significativo'}:
        return 'sign'
    if normalizado.startswith('no sign') or normalizado.startswith('normal'):
        return 'no sign'
    if normalizado in {'bajo', 'baja', 'alto', 'alta', 'positivo', 'positiva', 'negativo', 'negativa'}:
        return 'sign'
    return str(valor)

# ═════════════════════════════════════════════════════════════════════════════
# 5. MODELO DE LA REJILLA (independiente de python-docx)
# ═════════════════════════════════════════════════════════════════════════════

def _celda(col, span, texto="", fill=None, jc=None, vmerge=None):
    return {"col": col, "span": span, "texto": texto, "fill": fill, "jc": jc, "vmerge": vmerge}


def _fila_cabecera():
    celdas = [_celda(c, s, t, fill=COLOR_CABECERA, jc="center") for c, s, t in CABECERA]
    return {"celdas": celdas, "cabecera": True}


def construir_modelo(resultados, clasificaciones, available_tests):
    """Lista de filas; cada fila = {'celdas': [...], 'cabecera': bool}."""
    filas = [_fila_cabecera()]

    for bloque, prueba in resolver_pruebas(available_tests):
        f_ind = [_celda(0, 1, prueba, vmerge="restart"), _celda(1, 1, "Índice")]
        f_pd = [_celda(0, 1, vmerge="continue"), _celda(1, 1, "PD")]
        f_rend = [_celda(0, 1, vmerge="continue"), _celda(1, 1, "Rendimiento")]

        for spec in bloque["celdas"]:
            col, span, etiqueta = spec[:3]
            if etiqueta == NEGRO:
                f_ind.append(_celda(col, span, fill=COLOR_NEGRO, vmerge="restart"))
                f_pd.append(_celda(col, span, fill=COLOR_NEGRO, vmerge="continue"))
                f_rend.append(_celda(col, span, fill=COLOR_NEGRO, vmerge="continue"))
                continue

            _, _, _, clave_pd, clave_cl, tipo = spec
            valor_pd = _buscar(resultados, clave_pd, prueba)
            valor_cl = _buscar(clasificaciones, clave_cl, prueba)
            if tipo == "sign":
                valor_cl = _fmt_significacion(valor_cl)

            f_ind.append(_celda(col, span, etiqueta))
            f_pd.append(_celda(col, span, _fmt_pd(valor_pd) if valor_pd != "-" else "-"))
            f_rend.append(_celda(col, span, str(valor_cl), fill=_COLOR_POR_TIPO[tipo](valor_cl)))

        for f in (f_ind, f_pd, f_rend):
            if sum(c["span"] for c in f) != N_COLS:
                raise ValueError(f"La fila de '{prueba}' no suma {N_COLS} columnas "
                                 f"(revisa BLOQUES).")
            filas.append({"celdas": f, "cabecera": False})

    filas.append(_fila_cabecera())          # última fila: repetición de cabeceras
    return filas

# ═════════════════════════════════════════════════════════════════════════════
# 6. AJUSTE AL ANCHO DE PÁGINA Y TAMAÑO DE TEXTO
# ═════════════════════════════════════════════════════════════════════════════

# Anchos de avance de Times New Roman (milésimas de em) para ASCII 32..126.
_W = [250, 333, 408, 500, 500, 833, 778, 180, 333, 333, 500, 564, 250, 333, 250, 278,
      500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 278, 278, 564, 564, 564, 444,
      921, 722, 667, 667, 722, 611, 556, 722, 722, 333, 389, 722, 611, 889, 722, 722,
      556, 722, 667, 556, 611, 722, 722, 944, 722, 722, 611, 333, 278, 333, 469, 500,
      333, 444, 500, 444, 500, 444, 333, 500, 500, 278, 278, 500, 278, 778, 500, 500,
      500, 500, 333, 389, 278, 500, 500, 722, 500, 500, 444, 480, 200, 480, 541]
_ANCHO_ASCII = {chr(32 + i): w / 1000 for i, w in enumerate(_W)}


def _ancho_em(palabra):
    total = 0.0
    for ch in palabra:
        if ch not in _ANCHO_ASCII:                       # á, ó, ñ… -> letra base
            ch = unicodedata.normalize("NFD", ch)[0]
        total += _ANCHO_ASCII.get(ch, 0.5)
    return total


def escalar_anchos(ancho_total):
    """Reparte ``ancho_total`` (twips) en proporción a COLS_BASE."""
    f = ancho_total / sum(COLS_BASE)
    anchos = [int(round(w * f)) for w in COLS_BASE]
    anchos[-1] += ancho_total - sum(anchos)              # corrige el redondeo
    return anchos


def calcular_pt(filas, anchos, pt_min=PT_MIN, pt_max=PT_MAX):
    """
    Mayor tamaño de fuente (pasos de 0,5 pt) con el que ninguna palabra de
    ninguna celda desborda su ancho, entre pt_min y pt_max.
    """
    limite = pt_max
    for fila in filas:
        for c in fila["celdas"]:
            if not c["texto"] or c["vmerge"] == "continue":
                continue
            interior = (sum(anchos[c["col"]:c["col"] + c["span"]]) - 2 * MARGEN_CELDA - 10) / 20
            for palabra in c["texto"].split():
                limite = min(limite, interior / (_ancho_em(palabra) * 1.03))   # 3 % de holgura
    pt = int(limite * 2) / 2
    if pt < pt_min:
        log.warning("Hace falta %.1f pt para que quepa todo, pero el mínimo es %.1f pt: "
                    "alguna palabra se partirá. Usa página apaisada o márgenes menores.",
                    limite, pt_min)
    return max(pt_min, min(pt_max, pt))

# ═════════════════════════════════════════════════════════════════════════════
# 7. GENERACIÓN DEL XML DE LA TABLA
# ═════════════════════════════════════════════════════════════════════════════

def _el(tag, padre=None, **attrs):
    e = OxmlElement(tag)
    for k, v in attrs.items():
        e.set(qn("w:" + k), str(v))
    if padre is not None:
        padre.append(e)
    return e


def _rpr(padre, pt):
    rpr = _el("w:rPr", padre)
    _el("w:rFonts", rpr, ascii=FUENTE, hAnsi=FUENTE, cs=FUENTE)
    _el("w:sz", rpr, val=int(pt * 2))
    _el("w:szCs", rpr, val=int(pt * 2))
    return rpr


def _crear_tc(c, ancho, pt, keep_next):
    tc = OxmlElement("w:tc")
    pr = _el("w:tcPr", tc)
    _el("w:tcW", pr, w=ancho, type="dxa")
    if c["span"] > 1:
        _el("w:gridSpan", pr, val=c["span"])
    if c["vmerge"] == "restart":
        _el("w:vMerge", pr, val="restart")
    elif c["vmerge"] == "continue":
        _el("w:vMerge", pr)
    if c["fill"]:
        _el("w:shd", pr, val="clear", color="auto", fill=c["fill"])
        if c["fill"] == COLOR_NEGRO and c["vmerge"] == "restart":
            diagonales = _el("w:tcBorders", pr)
            _el("w:tl2br", diagonales, val="single", sz=8, space=0, color="808080")
            _el("w:tr2bl", diagonales, val="single", sz=8, space=0, color="808080")

    p = _el("w:p", tc)
    ppr = _el("w:pPr", p)
    if keep_next:
        _el("w:keepNext", ppr)
    _el("w:spacing", ppr, before=0, after=0, line=240, lineRule="auto")
    if c["jc"]:
        _el("w:jc", ppr, val=c["jc"])
    _rpr(ppr, pt)                                        # marca de párrafo

    if c["texto"]:
        r = _el("w:r", p)
        _rpr(r, pt)
        t = _el("w:t", r)
        t.text = c["texto"]
        t.set("{http://www.w3.org/XML/1998/namespace}space", "preserve")
    return tc


def _ancho_util_twips(doc):
    s = doc.sections[-1]
    return int((s.page_width - s.left_margin - s.right_margin) / 635)   # 1 twip = 635 EMU


def agregar_tabla_indices(doc, resultados, clasificaciones, available_tests,
                          despues_de=None, ancho_twips=None,
                          pt_min=PT_MIN, pt_max=PT_MAX, mantener_junta=True):
    """
    Genera la tabla de índices y la inserta en ``doc`` (docx.Document).

    despues_de     párrafo tras el cual insertar la tabla (por defecto, al final).
    ancho_twips    ancho de la tabla; por defecto, el ancho útil entre márgenes
                   de la última sección del documento.
    mantener_junta evita que la tabla se parta entre páginas si cabe en una.

    Devuelve el objeto docx.table.Table (o None si no hay ninguna prueba).
    """
    filas = construir_modelo(resultados, clasificaciones, available_tests)
    if len(filas) <= 2:
        log.warning("Ninguna prueba disponible: no se genera la tabla.")
        return None

    ancho = ancho_twips or _ancho_util_twips(doc)
    anchos = escalar_anchos(ancho)
    pt = calcular_pt(filas, anchos, pt_min, pt_max)
    log.info("Tabla: %d filas, ancho %d twips, texto %.1f pt", len(filas), ancho, pt)

    tabla = doc.add_table(rows=0, cols=N_COLS)
    tbl = tabla._tbl

    # ── propiedades de tabla (orden exigido por el esquema) ──
    tpr = tbl.tblPr
    for hijo in list(tpr):
        tpr.remove(hijo)
    _el("w:tblW", tpr, w=ancho, type="dxa")
    _el("w:jc", tpr, val="center")
    bordes = _el("w:tblBorders", tpr)
    for lado in ("top", "left", "bottom", "right", "insideH", "insideV"):
        _el("w:" + lado, bordes, val="single", sz=4, space=0, color="auto")
    _el("w:tblLayout", tpr, type="fixed")
    mar = _el("w:tblCellMar", tpr)
    _el("w:top", mar, w=0, type="dxa")
    _el("w:left", mar, w=MARGEN_CELDA, type="dxa")
    _el("w:bottom", mar, w=0, type="dxa")
    _el("w:right", mar, w=MARGEN_CELDA, type="dxa")
    _el("w:tblLook", tpr, val="04A0", firstRow=1, lastRow=0, firstColumn=1,
        lastColumn=0, noHBand=0, noVBand=1)

    for gc, w in zip(tbl.tblGrid.findall(qn("w:gridCol")), anchos):
        gc.set(qn("w:w"), str(w))

    # ── filas ──
    for i, fila in enumerate(filas):
        tr = _el("w:tr", tbl)
        trpr = _el("w:trPr", tr)
        _el("w:cantSplit", trpr)
        if fila["cabecera"]:
            _el("w:trHeight", trpr, val=int(828 * pt / PT_MAX), hRule="atLeast")
        if i == 0:
            _el("w:tblHeader", trpr)                     # cabecera repetida si pagina
        keep = mantener_junta and i < len(filas) - 1
        for c in fila["celdas"]:
            w = sum(anchos[c["col"]:c["col"] + c["span"]])
            celda = dict(c)
            celda["jc"] = "center" if fila["cabecera"] or c["col"] >= 2 else None
            tr.append(_crear_tc(celda, w, pt, keep))

    if despues_de is not None:
        despues_de._p.addnext(tbl)

    # Pie de tabla con leyenda de siglas y colores.
    pie_tabla = doc.add_paragraph()
    pie_tabla.paragraph_format.space_before = Pt(0)
    pie_tabla.paragraph_format.space_after = Pt(0)
    run_siglas = pie_tabla.add_run(
        "A: Aciertos | Dif: Diferencia en una misma puntuación obtenida en una y otra parte de la prueba | C: Comisiones | O: Omisiones | TR: Tiempo de respuesta | "
        "CON: Concentración | N: Número de elementos procesados | "
        "Dif P4: A en la parte 4 de la prueba, obtenidos vs esperados en base a los A en las partes anteriores | "
        "PSV: Precisión de Seguimiento Visomotor | "
        "M: Promedio del número máximo de cifras memorizadas"
    )
    run_siglas.italic = True
    run_siglas.font.size = Pt(9)

    leyenda_rendimiento = doc.add_paragraph()
    leyenda_rendimiento.alignment = WD_PARAGRAPH_ALIGNMENT.LEFT
    cuadrado_rojo = leyenda_rendimiento.add_run('■ ')
    cuadrado_rojo.font.size = Pt(9)
    cuadrado_rojo.font.color.rgb = RGBColor(180, 0, 0)
    leyenda_rendimiento.add_run('Rendimiento deficiente   ')
    cuadrado_verde = leyenda_rendimiento.add_run('■ ')
    cuadrado_verde.font.size = Pt(9)
    cuadrado_verde.font.color.rgb = RGBColor(0, 128, 0)
    leyenda_rendimiento.add_run('Rendimiento excelente   ')
    cuadrado_amarillo = leyenda_rendimiento.add_run('■ ')
    cuadrado_amarillo.font.size = Pt(9)
    cuadrado_amarillo.font.color.rgb = RGBColor(255, 192, 0)
    leyenda_rendimiento.add_run('Diferencia significativa')

    return tabla

def _add_textual_results_sections(doc, resultados, clasificaciones, nombre):
    """Añade los párrafos interpretativos definidos en textos.py."""
    def nivel(clave):
        return clasificaciones.get(clave)

    def parrafo(textos, clave):
        valor = nivel(clave)
        if valor in textos:
            doc.add_paragraph(textos[valor].format(nombre=nombre))

    def parrafo_con_nivel(textos, titulo, nivel_clave, prefijo=None, mostrar_titulo=True):
        """Añade un subtítulo y busca el texto con la clave que usa textos.py."""
        if mostrar_titulo:
            subtitulo(f"🔹 {titulo}")
        valor = clasificaciones.get(nivel_clave)
        if valor is None and nivel_clave.endswith('_texto'):
            valor = clasificaciones.get(nivel_clave.replace('_texto', ''))
        if prefijo is not None and valor is not None:
            valor = f"{prefijo} {valor}"
        if valor is None:
            return

        if valor in textos:
            doc.add_paragraph(textos[valor].format(nombre=nombre))
            return

        # Compatibilidad con claves de texto con prefijos: e.g. 'O normal', 'C bajo'.
        if isinstance(valor, str):
            candidatos = [valor]
            if not valor.startswith(('O ', 'C ', 'TR ', 'A ', 'PSV ')):
                candidatos.extend([f'O {valor}', f'C {valor}', f'TR {valor}', f'A {valor}', f'PSV {valor}'])
            for candidato in candidatos:
                if candidato in textos:
                    doc.add_paragraph(textos[candidato].format(nombre=nombre))
                    return

        if textos is PARRAFO_DUALTASK_TR:
            tr_nivel = clasificaciones.get('DUALTASK_TR')
            c_nivel = clasificaciones.get('DUALTASK_C', 'normal')
            if tr_nivel == 'bajo':
                clave_tr = 'TR bajo y C bajo' if c_nivel == 'bajo' else 'TR bajo y C normal o alto'
            elif tr_nivel == 'alto':
                clave_tr = f'TR alto y C {c_nivel}'
            else:
                clave_tr = 'TR normal'
            texto_tr = textos.get(clave_tr)
            if texto_tr:
                doc.add_paragraph(texto_tr.format(nombre=nombre))
                return

        # Compatibilidad extra para CPT_N, que usa claves semánticas diferentes a las combinaciones internas.
        if textos is PARRAFO_CPT_TR:
            tr = clasificaciones.get('CPT_N')
            c = clasificaciones.get('CPT_C')
            if tr == 'alto' and c in ('bajo', 'normal'):
                clave = 'alto y E bajo o normal'
            elif tr == 'alto' and c == 'alto':
                clave = 'alto y E alto'
            elif tr == 'normal':
                clave = 'normal'
            elif tr == 'bajo' and c in ('normal', 'alto'):
                clave = 'bajo y E normal o alto'
            elif tr == 'bajo' and c == 'bajo':
                clave = 'bajo y E bajo'
            else:
                clave = None
            if clave is not None and clave in textos:
                doc.add_paragraph(textos[clave].format(nombre=nombre))
                return

    def subtitulo(texto):
        _add_bold_paragraph(doc, texto)

    doc.add_page_break()
    titulo_resultados_especificos = doc.add_paragraph()
    titulo_resultados_especificos.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
    run = titulo_resultados_especificos.add_run(
        PARRAFOS_FIJOS['titulo_resultados_específicos']
    )
    run.bold = True
    run.font.size = Pt(16)
    doc.add_paragraph()
    doc.add_paragraph()

    def titulo_prueba(texto):
        """Inicia una prueba con título destacado y subrayado."""
        parrafo_titulo = _add_bold_paragraph(doc, texto)
        for run in parrafo_titulo.runs:
            run.bold = True
            run.underline = True
            run.font.color.rgb = RGBColor(0, 0, 0)


    if 'ACS' in resultados.get('available_tests', []):
        titulo_prueba(PARRAFOS_FIJOS['titulo_ACS'])
        doc.add_paragraph()
        doc.paragraphs[-2].alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
        
        parrafo(PARRAFO_ACS_atenciongeneral, 'ACS_atenciongeneral')
        _add_bars_section(
            doc,
            {'ACS_atenciongeneral': {'nombre': 'Atención general', 'color': (70, 130, 180)}},
            resultados,
            tabla_destino_cell=None,
        )
        parrafo(PARRAFO_ACS_foco, 'ACS_foco')
        _add_bars_section(
            doc,
            {'ACS_foco': {'nombre': 'Foco', 'color': (70, 130, 180)}},
            resultados,
            tabla_destino_cell=None,
        )
        parrafo(PARRAFO_ACS_cambio, 'ACS_cambio')
        _add_bars_section(
            doc,
            {'ACS_cambio': {'nombre': 'Cambio', 'color': (70, 130, 180)}},
            resultados,
            tabla_destino_cell=None,
        )

    if 'ANT' in resultados.get('available_tests', []):
        doc.add_page_break()
        titulo_prueba(PARRAFOS_FIJOS['titulo_ANT'])
        doc.add_paragraph()
        doc.paragraphs[-2].alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
        parrafo_con_nivel(PARRAFO_ANT_TR, 'Velocidad de procesamiento / Tiempo de respuesta (TR)', 'ANT_TR_texto')
        parrafo_con_nivel(PARRAFO_ANT_A, 'Número de aciertos (A)', 'ANT_A', 'A')
        subtitulo('🔹 Precisión / Errores de omisión (O) y comisión (C)')
        parrafo_con_nivel(PARRAFO_ANT_O, 'Errores de omisión (O)', 'ANT_O', 'O', mostrar_titulo=False)
        parrafo_con_nivel(PARRAFO_ANT_C, 'Errores de comisión (C)', 'ANT_C_texto', mostrar_titulo=False)
        parrafo_con_nivel(PARRAFO_ANT_F, 'Atención sostenida / Fatiga', 'ANT_F_texto')
        subtitulo('🔹 Eficiencia de las redes neurales atencionales')
        _add_bars_section(
            doc,
            {'ANT_TR_alerta': {'nombre': 'Red de alerta', 'color': (70, 130, 180)}},
            resultados,
        )
        parrafo_con_nivel(PARRAFO_ANT_alerta, 'Eficiencia Redes neurales', 'ANT_TR_alerta', 'TR_alerta', mostrar_titulo=False)
        _add_bars_section(
            doc,
            {'ANT_TR_orientacion': {'nombre': 'Red de orientación', 'color': (70, 130, 180)}},
            resultados,
        )
        parrafo_con_nivel(PARRAFO_ANT_orientacion, 'Red de orientación', 'ANT_TR_orientacion', 'TR_orientacion', mostrar_titulo=False)
        _add_bars_section(
            doc,
            {'ANT_TR_ejecutivo': {'nombre': 'Red ejecutiva', 'color': (70, 130, 180)}},
            resultados,
        )
        parrafo_con_nivel(PARRAFO_ANT_ejecutivo, 'Red ejecutiva', 'ANT_TR_ejecutivo', 'TR_ejecutivo', mostrar_titulo=False)

    if 'DigitsMemorization' in resultados.get('available_tests', []):
        doc.add_paragraph()
        doc.add_paragraph()
        doc.add_paragraph()
        titulo_prueba(PARRAFOS_FIJOS['titulo_DigitsMemorization'])
        doc.add_paragraph()
        doc.paragraphs[-2].alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
        subtitulo('🔹 Memoria operativa o de trabajo')
        parrafo(PARRAFO_DigitsMemorization, 'Digits_Memorization_M')

    if 'CPT' in resultados.get('available_tests', []):
        doc.add_page_break()
        titulo_prueba(PARRAFOS_FIJOS['titulo_CPT'])
        doc.add_paragraph()
        doc.paragraphs[-2].alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
        parrafo_con_nivel(PARRAFO_CPT_TR, 'Número de elementos procesados (N)', 'CPT_N')
        subtitulo('🔹 Precisión / Errores de omisión (O) y comisión (C)')
        parrafo_con_nivel(PARRAFO_CPT_O, 'Errores de omisión (O)', 'CPT_O', mostrar_titulo=False)
        parrafo_con_nivel(PARRAFO_CPT_C, 'Errores de comisión (C)', 'CPT_C', mostrar_titulo=False)
        parrafo_con_nivel(PARRAFO_CPT_CON, 'Concentración (CON)', 'CPT_CON')
        subtitulo('🔹 Variabilidad del rendimiento (VAR)')
        var_nivel = nivel('CPT_VAR')
        var_condicion = clasificaciones.get('CPT_VAR_condicion', 'nada')
        var_key = (var_nivel, var_condicion)
        texto_var = PARRAFO_CPT_VAR.get(var_key)
        if texto_var is None and var_nivel in PARRAFO_CPT_VAR:
            texto_var = PARRAFO_CPT_VAR[var_nivel]
        if texto_var:
            doc.add_paragraph(texto_var.format(nombre=nombre))

    if 'FourFigures' in resultados.get('available_tests', []):
        doc.add_page_break()
        titulo_prueba(PARRAFOS_FIJOS['titulo_FourFigures'])
        doc.add_paragraph()
        doc.paragraphs[-2].alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
        parrafo_con_nivel(PARRAFO_FourFigures_TR, 'Velocidad de procesamiento / Tiempo de respuesta (TR)', 'FourFigures_TR_texto')
        parrafo_con_nivel(PARRAFO_FourFigures_A, 'Número de aciertos (A)', 'FourFigures_A')
        parrafo_con_nivel(PARRAFO_FourFigures_C, 'Errores de comisión (C)', 'FourFigures_C_texto')
        parrafo_con_nivel(PARRAFO_FourFigures_P4_A_obtenido_vs_esperado, 'Flexibilidad cognitiva', 'FourFigures_P4_A_obtenido_vs_esperado')

    if 'DUALTASK' in resultados.get('available_tests', []):
        doc.add_page_break()
        titulo_prueba(PARRAFOS_FIJOS['titulo_DualTask'])
        doc.add_paragraph()
        doc.paragraphs[-2].alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
        parrafo_con_nivel(PARRAFO_DUALTASK_General_PSV_y_A, 'Rendimiento general', 'DUALTASK_General_PSV_y_A')
        subtitulo('🔹 Atención sostenida / Fatiga o Automatización')
        parrafo_con_nivel(PARRAFO_DUALTASK_A, 'Atención sostenida', 'DUALTASK_A', 'A', mostrar_titulo=False)
        parrafo_con_nivel(PARRAFO_DUALTASK_PSV, 'Precisión de seguimiento visomotor (PSV)', 'DUALTASK_PSV', mostrar_titulo=False)
        parrafo_con_nivel(PARRAFO_DUALTASK_Fatiga, 'Fatiga', 'DUALTASK_Fatiga', mostrar_titulo=False)
        if clasificaciones.get('DUALTASK_automatización'):
            parrafo_con_nivel(
                PARRAFO_DUALTASK_automatización,
                'Automatización',
                'DUALTASK_automatización',
                mostrar_titulo=False,
            )
        parrafo_con_nivel(PARRAFO_DUALTASK_TR, 'Velocidad de procesamiento / Tiempo de respuesta (TR)', 'DUALTASK_TR_texto')
        subtitulo('🔹 Precisión / Errores de omisión (O) y comisión (C)')
        parrafo_con_nivel(PARRAFO_DUALTASK_O, 'Errores de omisión (O)', 'DUALTASK_O', mostrar_titulo=False)
        parrafo_con_nivel(PARRAFO_DUALTASK_C, 'Errores de comisión (C)', 'DUALTASK_C_texto', mostrar_titulo=False)

        nivel_general = clasificaciones.get('DUALTASK_General_PSV_y_A')
        nivel_psv = clasificaciones.get('DUALTASK_PSV')
        nivel_t2 = clasificaciones.get('DUALTASK_A')
        nivel_c = clasificaciones.get('DUALTASK_C')
        concurrencia = clasificaciones.get('DUALTASK_PSV_cuando_concurrencia', '')
        fatiga = clasificaciones.get('DUALTASK_Fatiga')
        tr_a_vs_c = clasificaciones.get('DUALTASK_TR_A_vs_C')

        recomendaciones = []
        if nivel_general in ('Inestable y negativo', 'Muy inestable'):
            recomendaciones.append('PARRAFO_DUALTASK_final_inestable_negativo_o_muy_inestable')
        if nivel_psv == 'alto' and nivel_t2 == 'normal':
            recomendaciones.append('PARRAFO_DUALTASK_final_inestable_mejor_T1_y_T2_positivo')
        if nivel_psv in ('normal', 'alto') and nivel_t2 == 'bajo':
            recomendaciones.append('PARRAFO_DUALTASK_final_inestable_mejor_T1_y_T2_negativo')
        if nivel_t2 == 'alto' and nivel_psv == 'normal':
            recomendaciones.append('PARRAFO_DUALTASK_final_mejor_T2_y_T1_positivo')
        if nivel_t2 in ('normal', 'alto') and nivel_psv == 'bajo':
            recomendaciones.append('PARRAFO_DUALTASK_final_inestable_mejor_T2_y_T1_negativo')
        if concurrencia.startswith('deterioro') and nivel_t2 == 'bajo':
            recomendaciones.append('PARRAFO_DUALTASK_final_concurrencia_peorT1_malT2')
        if nivel_psv == 'bajo':
            recomendaciones.append('PARRAFO_DUALTASK_final_PSV_bajo')

        if recomendaciones or (nivel_c in ('normal', 'alto') and tr_a_vs_c is not None) or (fatiga and fatiga != 'no F'):
            subtitulo('🔹 Recomendaciones')
            doc.add_paragraph(PARRAFOS_CONDICIONALES_OPCIONALES_DUALTASK['intro'].format(nombre=nombre))
            for clave in recomendaciones:
                texto = PARRAFOS_CONDICIONALES_OPCIONALES_DUALTASK.get(clave)
                if texto:
                    doc.add_paragraph(texto.format(nombre=nombre))

            if nivel_c in ('normal', 'alto') and tr_a_vs_c in ('positivo', 'negativo'):
                clave = 'impulsividad' if tr_a_vs_c == 'positivo' else 'distraibilidad'
                doc.add_paragraph(PARRAFO_DUALTASK_final_dif_TR_A_y_C[clave].format(nombre=nombre))

            if fatiga and fatiga != 'no F':
                texto_fatiga = PARRAFOS_CONDICIONALES_OPCIONALES_DUALTASK.get('PARRAFO_DUALTASK_final_fatiga ')
                if texto_fatiga:
                    doc.add_paragraph(texto_fatiga.format(nombre=nombre))

    # La síntesis se genera en una página independiente al final del informe.
    doc.add_page_break()
    titulo_sintesis = _add_bold_paragraph(
        doc,
        PARRAFOS_FIJOS['titulo_sintesis_final'].format(nombre_completo=nombre),
    )
    doc.add_paragraph() 
    doc.paragraphs[-2].alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
    for run in titulo_sintesis.runs:
        run.font.size = Pt(14)

    doc.add_paragraph(
        PARRAFOS_FIJOS['introduccion_sintesis_final'].format(nombre=nombre)
    )

    def nivel_sintesis(claves):
        niveles = [clasificaciones.get(clave) for clave in claves]
        niveles = [nivel for nivel in niveles if nivel in ('bajo', 'normal', 'alto')]
        if 'bajo' in niveles:
            return 'malo'
        if 'alto' in niveles:
            return 'bueno'
        return 'normal'

    def completar_dimensiones(indices):
        """Devuelve nombres de índices bajos y altos para los textos de síntesis."""
        deficits = []
        strengths = []
        for clave, etiqueta in indices:
            valor = clasificaciones.get(clave)
            if valor == 'bajo':
                deficits.append(etiqueta)
            elif valor == 'alto':
                strengths.append(etiqueta)
            elif clave == 'DUALTASK_Fatiga' and valor not in (None, 'no F'):
                deficits.append(etiqueta)
        return ', '.join(deficits) or 'ninguna', ', '.join(strengths) or 'ninguna'

    dimensiones = {
        'arousal': (
            ('ACS_atenciongeneral', 'ACS: atención general'),
            ('FourFigures_A', 'FourFigures: aciertos'),
            ('DUALTASK_A', 'DualTask: aciertos'),
        ),
        'atencionsostenida': (
            ('CPT_VAR', 'CPT: variabilidad'),
            ('ANT_A_principio_vs_final', 'ANT: fatiga en aciertos'),
            ('DUALTASK_Fatiga', 'DualTask: fatiga'),
        ),
        'controlejecutivo': (
            ('CPT_C', 'CPT: comisiones'),
            ('CPT_O', 'CPT: omisiones'),
            ('DUALTASK_C', 'DualTask: comisiones'),
            ('DUALTASK_O', 'DualTask: omisiones'),
        ),
        'velocidadprocesamiento': (
            ('CPT_N', 'CPT: elementos procesados'),
            ('DUALTASK_TR', 'DualTask: tiempo de respuesta'),
            ('ANT_TR', 'ANT: tiempo de respuesta'),
        ),
    }

    sintesis_fmt = {
        'nombre': nombre,
        'tarea_deficit_arousal': '',
        'tarea_fortaleza_arousal': '',
        'tarea_deficit_atencionsostenida': '',
        'tarea_fortaleza_atencionsostenida': '',
        'tarea_deficit_controlejecutivo': '',
        'tarea_fortaleza_controlejecutivo': '',
        'tarea_deficit_velocidadprocesamiento': '',
        'tarea_fortaleza_velocidadprocesamiento': '',
        'dimension_afectada': '',
        'prueba_afectada': '',
    }

    for dimension, indices in dimensiones.items():
        deficit, fortaleza = completar_dimensiones(indices)
        sintesis_fmt[f'tarea_deficit_{dimension}'] = deficit
        sintesis_fmt[f'tarea_fortaleza_{dimension}'] = fortaleza

    sintesis_fmt['dimension_afectada'] = sintesis_fmt['tarea_deficit_controlejecutivo']
    sintesis_fmt['prueba_afectada'] = sintesis_fmt['tarea_deficit_atencionsostenida']
    sintesis = (
        (PARRAFO_sintesis_arousal, nivel_sintesis(('ACS_atenciongeneral', 'FourFigures_A', 'DUALTASK_A'))),
        (PARRAFO_sintesis_atencionsostenida, nivel_sintesis(('CPT_VAR', 'ANT_A_principio_vs_final', 'DUALTASK_Fatiga'))),
        (PARRAFO_sintesis_controlejecutivo, nivel_sintesis(('CPT_C', 'CPT_O', 'DUALTASK_C', 'DUALTASK_O'))),
        (PARRAFO_sintesis_flexibilidadcognitiva, nivel_sintesis(('FourFigures_P4_A_obtenido_vs_esperado',))),
        (PARRAFO_sintesis_memoriatrabajo, nivel_sintesis(('DUALTASK_Rendimiento_General_cuando_concurrencia', 'Digits_Memorization_M'))),
        (PARRAFO_sintesis_velocidadprocesamiento, nivel_sintesis(('CPT_N', 'DUALTASK_TR', 'ANT_TR'))),
        (PARRAFO_sintesis_final, 'normal'),
    )
    textos_dimensiones = []
    for textos_sintesis, clave in sintesis[:-1]:
        texto = textos_sintesis.get(clave)
        if texto:
            texto = texto.format(**sintesis_fmt).strip()
            if texto and texto[-1] not in '.!?':
                texto += '.'
            textos_dimensiones.append(texto)

    if textos_dimensiones:
        doc.add_paragraph(' '.join(textos_dimensiones))

    textos_sintesis_final, clave_final = sintesis[-1]
    texto_final = textos_sintesis_final.get(clave_final)
    if texto_final:
        doc.add_paragraph(texto_final.format(**sintesis_fmt))


# Esta es la función _add_bars_section que sigue el formato adecuado y deseado.
def _add_bars_section(doc, factores_info, resultados, tabla_destino_cell=None):
    """
    Añade una sección de barras horizontales para los factores dados.

    Args:
        doc:              Documento (usado si tabla_destino_cell es None).
        factores_info:    Dict clave→{nombre, color, ...} (ACS_INFO o ANT_INFO).
        resultados:       Dict con PCT_<factor>.
        tabla_destino_cell: Si se pasa, añade el contenido dentro de esa celda.
    """
    BAR_CHARS  = 20   # caracteres de ancho total de la barra
    CHAR_LLENO = '█'
    CHAR_VACIO = '░'

    def obtener_puntuacion(clave):
        """Obtiene la puntuación normalizada de la escala 0-100."""
        valor = resultados.get(f'PT_{clave}')
        if valor is None:
            valor = resultados.get(f'PCT_{clave}')
        if valor is None:
            return 0
        try:
            return max(0, min(100, float(valor)))
        except (TypeError, ValueError):
            return 0

    # Ordenar factores de mayor a menor puntuación normalizada.
    orden = sorted(factores_info.keys(),
                   key=obtener_puntuacion, reverse=True)

    destino = tabla_destino_cell if tabla_destino_cell is not None else doc


    for clave in orden:
        info = factores_info[clave]
        pct  = obtener_puntuacion(clave)
        r, g, b = info['color']
        hex_color = _rgb_to_hex(info['color'])

        # --- Párrafo de encabezado: nombre + porcentaje ---
        p_header = destino.add_paragraph()
        _no_space_before_after(p_header)
        run_letra = p_header.add_run(f"{info['nombre']}  ")
        run_letra.bold = True
        run_letra.font.size = Pt(11)
        run_pct = p_header.add_run(f"{pct:g}%")
        run_pct.font.size  = Pt(11)
        run_pct.font.color.rgb = RGBColor(r, g, b)
        run_pct.bold = True

        # --- Párrafo de barra ---
        p_bar = destino.add_paragraph()
        _no_space_before_after(p_bar)
        llenos = round(pct / 100 * BAR_CHARS)
        vacios  = BAR_CHARS - llenos

        run_fill = p_bar.add_run(CHAR_LLENO * llenos)
        run_fill.font.color.rgb = RGBColor(r, g, b)
        run_fill.font.size      = Pt(9)

        run_empty = p_bar.add_run(CHAR_VACIO * vacios)
        run_empty.font.color.rgb = RGBColor(217, 217, 217)
        run_empty.font.size      = Pt(9)

        # Pequeño espacio
        sep = destino.add_paragraph()
        _no_space_before_after(sep)

    return

def guardar_informe(doc, ruta_salida):
    """
        Guarda el documento generado.
        Args:
            doc:         Documento Word.
            ruta_salida: Ruta donde guardar el archivo.
    """

    directory = os.path.dirname(ruta_salida)
    if directory:
        os.makedirs(directory, exist_ok=True)

    doc.save(ruta_salida)
    print(f"Informe generado exitosamente en: {ruta_salida}")
    return doc


