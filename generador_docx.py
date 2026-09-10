"""
Módulo para generar el informe atencional en formato DOCX.
"""
from __future__ import annotations

import os
from datetime import datetime
from typing import Iterable, List, Optional

from docx import Document
from docx.enum.table import WD_CELL_VERTICAL_ALIGNMENT
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt, RGBColor
from PIL import Image

from textos_runtime import (
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
    PARRAFO_DUALTASK_Fatiga,
    PARRAFO_DUALTASK_General_PSV_y_A,
    PARRAFO_DUALTASK_O,
    PARRAFO_DUALTASK_PSV,
    PARRAFO_DUALTASK_PSV_cuando_concurrencia,
    PARRAFO_DUALTASK_Rendimiento_General_cuando_concurrencia,
    PARRAFO_DUALTASK_TR,
    PARRAFO_DUALTASK_TR_A_vs_C,
    PARRAFO_DUALTASK_si_inestable,
    PARRAFO_DigitsMemorization,
    PARRAFO_FourFigures_A,
    PARRAFO_FourFigures_C,
    PARRAFO_FourFigures_P4_A_obtenido_vs_esperado,
    PARRAFO_FourFigures_TR,
    PARRAFOS_CONDICIONALES_OPCIONALES_DUALTASK,
)

TABLE_SLOTS = ['ACS', 'ANT', 'CPT', 'FourFigures', 'DUALTASK', 'DigitsMemorization']


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


def agregar_portada(doc: Document, nombre_completo: str, datos: dict) -> None:
    titulo = doc.add_heading('Prueba de Evaluación Atencional', 0)
    titulo.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER

    info = doc.add_paragraph()
    info.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
    info.add_run(f"Nombre del evaluado: {nombre_completo}\n").bold = True
    if datos.get('edad') is not None:
        info.add_run(f"Edad: {datos['edad']} años\n")
    if datos.get('fecha_aplicacion'):
        info.add_run(f"Fecha de aplicación: {datos['fecha_aplicacion']}\n")
    info.add_run(f"Fecha del informe: {datetime.now().strftime('%d/%m/%Y')}\n")

    nota = doc.add_paragraph()
    nota.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
    nota.add_run(
        "Informe orientativo generado automáticamente a partir del Excel de evaluación atencional."
    ).italic = True


def _build_results_lookup(resultados: dict, clasificaciones: dict) -> dict:
    lookup = {}
    for test in resultados.get('report_tests', []):
        lookup[test['slot']] = {
            'display_name': test['display_name'],
            'indices': [],
        }
        for indice in test['indices']:
            lookup[test['slot']]['indices'].append({
                'label': indice['label'],
                'pd': indice['pd'],
                'pt': resultados.get(indice['pt_key']),
                'clasificacion': clasificaciones.get(indice['key'], 'N/D'),
            })
    return lookup


def _add_results_table(doc: Document, resultados: dict, clasificaciones: dict) -> None:
    lookup = _build_results_lookup(resultados, clasificaciones)
    table = doc.add_table(rows=3, cols=len(TABLE_SLOTS) + 1)
    table.style = 'Table Grid'

    table.cell(0, 0).text = 'Campo'
    table.cell(1, 0).text = 'Disponibilidad'
    table.cell(2, 0).text = 'Resultados'

    for col, slot in enumerate(TABLE_SLOTS, start=1):
        presence = resultados['test_presence'][slot]
        header = table.cell(0, col)
        header.text = presence.display_name
        header.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER

        state = table.cell(1, col)
        body = table.cell(2, col)
        if presence.present:
            state.text = 'Disponible'
            lines = []
            for indice in lookup.get(slot, {}).get('indices', []):
                lines.append(
                    f"{indice['label']}: PD {_fmt_num(indice['pd'])} · PT {_fmt_num(indice['pt'])} · {indice['clasificacion']}"
                )
            body.text = "\n".join(lines) if lines else 'Sin índices configurados'
        else:
            state.text = 'Ausente'
            body.text = 'No se genera contenido para esta prueba.'
            for cell in (header, state, body):
                _set_cell_bg(cell, '404040')
                for paragraph in cell.paragraphs:
                    for run in paragraph.runs:
                        run.font.color.rgb = RGBColor(255, 255, 255)


def _add_bars_section(doc: Document, title: str, items: Iterable[tuple]) -> None:
    _add_heading(doc, title, size=11)
    table = doc.add_table(rows=1, cols=3)
    table.style = 'Table Grid'
    table.rows[0].cells[0].text = 'Índice'
    table.rows[0].cells[1].text = 'PT'
    table.rows[0].cells[2].text = 'Perfil'
    for label, pt in items:
        row = table.add_row().cells
        row[0].text = label
        row[1].text = _fmt_num(pt)
        row[2].text = _bar(pt)


def _paragraph_key_for_tr(clasificaciones: dict, prefix: str) -> str:
    return clasificaciones.get(f'{prefix}_TR_texto', 'TR normal y C normal o alto')


def _paragraph_key_for_c(clasificaciones: dict, prefix: str) -> str:
    return clasificaciones.get(f'{prefix}_C_texto', 'C normal')


def _add_acs_section(doc: Document, resultados: dict, clasificaciones: dict, fmt: dict) -> None:
    _add_heading(doc, PARRAFOS_FIJOS['titulo_ACS'])
    _add_paragraph(doc, PARRAFOS_FIJOS['texto_resultados_ACS'], **fmt)
    _add_paragraph(doc, PARRAFO_ACS_atenciongeneral[clasificaciones['ACS_atenciongeneral']], **fmt)
    _add_paragraph(doc, PARRAFO_ACS_foco[clasificaciones['ACS_foco']], **fmt)
    _add_paragraph(doc, PARRAFO_ACS_cambio[clasificaciones['ACS_cambio']], **fmt)
    _add_bars_section(
        doc,
        'Perfil ACS',
        [
            ('Atención general', resultados.get('PT_ACS_atenciongeneral')),
            ('Foco', resultados.get('PT_ACS_foco')),
            ('Cambio', resultados.get('PT_ACS_cambio')),
        ],
    )


def _add_ant_section(doc: Document, resultados: dict, clasificaciones: dict, fmt: dict) -> None:
    _add_heading(doc, PARRAFOS_FIJOS['titulo_ANT'])
    _add_paragraph(doc, _safe_dict_text(PARRAFO_ANT_TR, _paragraph_key_for_tr(clasificaciones, 'ANT')), **fmt)
    _add_paragraph(doc, _safe_dict_text(PARRAFO_ANT_A, clasificaciones.get('ANT_A')), **fmt)
    _add_paragraph(doc, _safe_dict_text(PARRAFO_ANT_C, _paragraph_key_for_c(clasificaciones, 'ANT')), **fmt)
    _add_paragraph(doc, _safe_dict_text(PARRAFO_ANT_O, clasificaciones.get('ANT_O')), **fmt)
    _add_paragraph(doc, _safe_dict_text(PARRAFO_ANT_F, clasificaciones.get('ANT_F_texto')), **fmt)
    _add_paragraph(doc, _safe_dict_text(PARRAFO_ANT_alerta, clasificaciones.get('ANT_TR_alerta')), **fmt)
    _add_paragraph(doc, _safe_dict_text(PARRAFO_ANT_orientacion, clasificaciones.get('ANT_TR_orientacion')), **fmt)
    _add_paragraph(doc, _safe_dict_text(PARRAFO_ANT_ejecutivo, clasificaciones.get('ANT_TR_ejecutivo')), **fmt)
    _add_bars_section(
        doc,
        'Perfil ANT',
        [
            ('A', resultados.get('PT_ANT_A')),
            ('C', resultados.get('PT_ANT_C')),
            ('O', resultados.get('PT_ANT_O')),
            ('TR', resultados.get('PT_ANT_TR')),
        ],
    )


def _add_cpt_section(doc: Document, resultados: dict, clasificaciones: dict, fmt: dict) -> None:
    nombre = resultados['display_names']['CPT']
    _add_heading(doc, f"{nombre} - prueba de rendimiento continuo")
    tr_key = clasificaciones['CPT_TR']
    e_key = 'bajo' if clasificaciones.get('CPT_O') == 'alto' or clasificaciones.get('CPT_C') == 'alto' else 'normal'
    if tr_key == 'alto':
        cpt_tr_texto = PARRAFO_CPT_TR['alto y E alto' if e_key == 'bajo' else 'alto y E bajo o normal']
    elif tr_key == 'bajo':
        cpt_tr_texto = PARRAFO_CPT_TR['bajo y E normal o alto' if e_key == 'bajo' else 'bajo y E bajo']
    else:
        cpt_tr_texto = PARRAFO_CPT_TR['normal']
    _add_paragraph(doc, cpt_tr_texto, **fmt)
    _add_paragraph(doc, PARRAFO_CPT_O[clasificaciones['CPT_O']], **fmt)
    _add_paragraph(doc, PARRAFO_CPT_C[clasificaciones['CPT_C']], **fmt)
    _add_paragraph(doc, PARRAFO_CPT_CON[clasificaciones['CPT_CON']], **fmt)
    var_nivel = clasificaciones['CPT_VAR']
    var_condicion = clasificaciones.get('CPT_VAR_condicion', 'nada')
    texto_var = (
        PARRAFO_CPT_VAR.get((var_nivel, var_condicion))
        if var_nivel == 'alto'
        else PARRAFO_CPT_VAR.get(var_nivel)
    )
    _add_paragraph(doc, texto_var, **fmt)
    _add_bars_section(
        doc,
        f'Perfil {nombre}',
        [
            ('CON', resultados.get('PT_CPT_CON')),
            ('VAR', resultados.get('PT_CPT_VAR')),
            ('O', resultados.get('PT_CPT_O')),
            ('C', resultados.get('PT_CPT_C')),
            ('TR', resultados.get('PT_CPT_TR')),
        ],
    )


def _add_four_figures_section(doc: Document, resultados: dict, clasificaciones: dict, fmt: dict) -> None:
    nombre = resultados['display_names']['FourFigures']
    _add_heading(doc, f"{nombre} - control y flexibilidad cognitiva")
    _add_paragraph(doc, _safe_dict_text(PARRAFO_FourFigures_TR, _paragraph_key_for_tr(clasificaciones, 'FourFigures')), **fmt)
    _add_paragraph(doc, _safe_dict_text(PARRAFO_FourFigures_A, clasificaciones.get('FourFigures_A')), **fmt)
    _add_paragraph(doc, _safe_dict_text(PARRAFO_FourFigures_C, _paragraph_key_for_c(clasificaciones, 'FourFigures')), **fmt)
    _add_paragraph(
        doc,
        _safe_dict_text(
            PARRAFO_FourFigures_P4_A_obtenido_vs_esperado,
            clasificaciones.get('FourFigures_P4_A_obtenido_vs_esperado'),
        ),
        **fmt,
    )
    _add_bars_section(
        doc,
        f'Perfil {nombre}',
        [
            ('A', resultados.get('PT_FourFigures_A')),
            ('C', resultados.get('PT_FourFigures_C')),
            ('TR', resultados.get('PT_FourFigures_TR')),
            ('P4 real vs esperada', resultados.get('PT_FourFigures_P4_A_obtenido_vs_esperado')),
        ],
    )


def _add_digits_section(doc: Document, resultados: dict, clasificaciones: dict, fmt: dict) -> None:
    _add_heading(doc, PARRAFOS_FIJOS['titulo_DigitsMemorization'])
    _add_paragraph(doc, _safe_dict_text(PARRAFO_DigitsMemorization, clasificaciones.get('DigitsMemorization_promedio')), **fmt)
    _add_bars_section(
        doc,
        'Perfil de memoria operativa',
        [
            ('Directo', resultados.get('PT_DigitsMemorization_directo')),
            ('Inverso', resultados.get('PT_DigitsMemorization_inverso')),
            ('Creciente', resultados.get('PT_DigitsMemorization_creciente')),
            ('Promedio', resultados.get('PT_DigitsMemorization_promedio')),
        ],
    )


def _add_dualtask_section(doc: Document, resultados: dict, clasificaciones: dict, fmt: dict) -> None:
    _add_heading(doc, PARRAFOS_FIJOS['titulo_DualTask'])
    _add_paragraph(doc, _safe_dict_text(PARRAFO_DUALTASK_General_PSV_y_A, clasificaciones.get('DUALTASK_General_PSV_y_A')), **fmt)
    if 'DUALTASK_si_inestable' in clasificaciones:
        _add_paragraph(doc, _safe_dict_text(PARRAFO_DUALTASK_si_inestable, clasificaciones.get('DUALTASK_si_inestable')), **fmt)
    if 'DUALTASK_Rendimiento_General_cuando_concurrencia' in clasificaciones:
        _add_paragraph(
            doc,
            _safe_dict_text(
                PARRAFO_DUALTASK_Rendimiento_General_cuando_concurrencia,
                clasificaciones.get('DUALTASK_Rendimiento_General_cuando_concurrencia'),
            ),
            **fmt,
        )
    _add_paragraph(
        doc,
        _safe_dict_text(PARRAFO_DUALTASK_PSV_cuando_concurrencia, clasificaciones.get('DUALTASK_PSV_cuando_concurrencia')),
        **fmt,
    )
    _add_paragraph(doc, PARRAFOS_FIJOS['introduccion_analisis_tareas_DualTask'], **fmt)
    _add_paragraph(doc, _safe_dict_text(PARRAFO_DUALTASK_PSV, clasificaciones.get('DUALTASK_PSV')), **fmt)
    _add_paragraph(doc, _safe_dict_text(PARRAFO_DUALTASK_A, clasificaciones.get('DUALTASK_A')), **fmt)
    _add_paragraph(doc, _safe_dict_text(PARRAFO_DUALTASK_C, clasificaciones.get('DUALTASK_C')), **fmt)
    _add_paragraph(doc, _safe_dict_text(PARRAFO_DUALTASK_O, clasificaciones.get('DUALTASK_O')), **fmt)

    tr_key = clasificaciones['DUALTASK_TR']
    c_key = clasificaciones['DUALTASK_C']
    if tr_key == 'bajo':
        dual_tr_text = PARRAFO_DUALTASK_TR['TR bajo y C bajo' if c_key == 'alto' else 'TR bajo y C normal o alto']
    elif tr_key == 'alto':
        dual_tr_text = PARRAFO_DUALTASK_TR[f"TR alto y C {'bajo' if c_key == 'alto' else ('alto' if c_key == 'bajo' else 'normal')}"]
    else:
        dual_tr_text = PARRAFO_DUALTASK_TR['TR normal']
    _add_paragraph(doc, dual_tr_text, **fmt)

    tr_a_vs_c = clasificaciones.get('DUALTASK_TR_A_vs_C')
    if tr_a_vs_c and c_key in {'normal', 'bajo'}:
        key = f"C {'alto' if c_key == 'bajo' else 'normal'} y TR_A_vs_C {tr_a_vs_c}"
        if key in PARRAFO_DUALTASK_TR_A_vs_C:
            _add_paragraph(doc, PARRAFO_DUALTASK_TR_A_vs_C[key], **fmt)

    _add_paragraph(doc, _safe_dict_text(PARRAFO_DUALTASK_Fatiga, clasificaciones.get('DUALTASK_Fatiga')), **fmt)
    _add_bars_section(
        doc,
        'Perfil Dual Task',
        [
            ('PSV', resultados.get('PT_DUALTASK_PSV')),
            ('A', resultados.get('PT_DUALTASK_A')),
            ('C', resultados.get('PT_DUALTASK_C')),
            ('O', resultados.get('PT_DUALTASK_O')),
            ('TR', resultados.get('PT_DUALTASK_TR')),
        ],
    )

    _add_heading(doc, 'Recomendaciones específicas', size=11)
    _add_paragraph(doc, PARRAFOS_CONDICIONALES_OPCIONALES_DUALTASK['intro'], **fmt)
    for flag, text_key in [
        ('DUALTASK_inestable_negativo_o_muy_inestable', 'PARRAFO_DUALTASK_final_inestable_negativo_o_muy_inestable'),
        ('DUALTASK_inestable_mejor_T1_y_T2_positivo', 'PARRAFO_DUALTASK_final_inestable_mejor_T1_y_T2_positivo'),
        ('DUALTASK_inestable_mejor_T1_y_T2_negativo', 'PARRAFO_DUALTASK_final_inestable_mejor_T1_y_T2_negativo'),
        ('DUALTASK_inestable_mejor_T2_y_T1_positivo', 'PARRAFO_DUALTASK_final_inestable_mejor_T2_y_T1_positivo'),
        ('DUALTASK_inestable_mejor_T2_y_T1_negativo', 'PARRAFO_DUALTASK_final_inestable_mejor_T2_y_T1_negativo'),
        ('DUALTASK_concurrencia_peorT1_malT2', 'PARRAFO_DUALTASK_final_concurrencia_peorT1_malT2'),
        ('DUALTASK_PSV_bajo', 'PARRAFO_DUALTASK_final_PSV_bajo'),
    ]:
        if clasificaciones.get(flag):
            _add_paragraph(doc, PARRAFOS_CONDICIONALES_OPCIONALES_DUALTASK[text_key], **fmt)
    if clasificaciones.get('DUALTASK_Fatiga') != 'no F':
        _add_paragraph(doc, PARRAFOS_CONDICIONALES_OPCIONALES_DUALTASK['PARRAFO_DUALTASK_final_fatiga'], **fmt)


def _add_summary(doc: Document, resultados: dict, clasificaciones: dict, fmt: dict) -> None:
    _add_heading(doc, PARRAFOS_FIJOS['titulo_sintesis_final'])
    altos = []
    bajos = []
    for test in resultados.get('report_tests', []):
        for indice in test['indices']:
            nivel = clasificaciones.get(indice['key'])
            if nivel == 'alto':
                altos.append(f"{test['display_name']} {indice['label']}")
            elif nivel == 'bajo':
                bajos.append(f"{test['display_name']} {indice['label']}")
    if altos:
        doc.add_paragraph(f"Fortalezas relativas: {', '.join(altos[:6])}.")
    if bajos:
        doc.add_paragraph(f"Aspectos con mayor dificultad relativa: {', '.join(bajos[:6])}.")
    doc.add_paragraph(
        "Las PT incluidas en este informe son provisionales y se han calculado con una plantilla técnica pendiente de sustituir por baremos reales."
    )


def crear_informe_docx(resultados, clasificaciones, nombre_caso="caso", script_dir=None):
    if script_dir is None:
        script_dir = os.path.dirname(os.path.abspath(__file__))

    doc = Document()
    for section in doc.sections:
        section.top_margin = Inches(1)
        section.bottom_margin = Inches(1)
        section.left_margin = Inches(1)
        section.right_margin = Inches(1)

    nombre_completo = resultados.get('nombre_completo') or nombre_caso
    nombre = resultados.get('nombre') or nombre_caso
    fmt = {'nombre': nombre, 'nombre_completo': nombre_completo}

    agregar_portada(doc, nombre_completo, resultados)
    doc.add_page_break()

    _add_heading(doc, PARRAFOS_FIJOS['titulo_general_prueba'])
    _add_paragraph(doc, PARRAFOS_FIJOS['objetivo_prueba'], **fmt)
    _add_heading(doc, PARRAFOS_FIJOS['titulo_procedimiento'])
    _add_paragraph(doc, PARRAFOS_FIJOS['descripcion_procedimiento0'], **fmt)
    if 'ACS' in resultados['available_tests']:
        _add_paragraph(doc, PARRAFOS_FIJOS['descripcion_procedimiento1.1'], **fmt)
    if 'ANT' in resultados['available_tests']:
        _add_paragraph(doc, PARRAFOS_FIJOS['descripcion_procedimiento2.1'], **fmt)
        _add_paragraph(doc, PARRAFOS_FIJOS['descripcion_procedimiento2.2'], **fmt)
    if 'CPT' in resultados['available_tests']:
        _add_paragraph(doc, PARRAFOS_FIJOS['descripcion_procedimiento3.1'], **fmt)
    if 'FourFigures' in resultados['available_tests']:
        _add_paragraph(doc, PARRAFOS_FIJOS['descripcion_procedimiento4.1'], **fmt)
    if 'DUALTASK' in resultados['available_tests']:
        _add_paragraph(doc, PARRAFOS_FIJOS['descripcion_procedimiento5.1'], **fmt)
    _add_heading(doc, PARRAFOS_FIJOS['titulo_indices'])
    _add_paragraph(doc, PARRAFOS_FIJOS['descripcion_indices'], **fmt)

    doc.add_page_break()
    _add_heading(doc, PARRAFOS_FIJOS['titulo_resultados'].format(**fmt), size=13)
    _add_paragraph(doc, PARRAFOS_FIJOS['texto_resultados'], **fmt)
    _add_results_table(doc, resultados, clasificaciones)

    imagen_cpt = os.path.join(script_dir, 'grafico_CPT_final.png')
    if _image_is_valid(imagen_cpt):
        doc.add_page_break()
        _add_heading(doc, 'Gráfico CPT/D2', size=11)
        doc.add_picture(imagen_cpt, width=Inches(6.5))

    doc.add_page_break()
    _add_heading(doc, PARRAFOS_FIJOS['titulo_resultados_especificos'])

    if 'ACS' in resultados['available_tests']:
        _add_acs_section(doc, resultados, clasificaciones, fmt)
    if 'ANT' in resultados['available_tests']:
        _add_ant_section(doc, resultados, clasificaciones, fmt)
    if 'CPT' in resultados['available_tests']:
        _add_cpt_section(doc, resultados, clasificaciones, fmt)
    if 'FourFigures' in resultados['available_tests']:
        _add_four_figures_section(doc, resultados, clasificaciones, fmt)
    if 'DigitsMemorization' in resultados['available_tests']:
        _add_digits_section(doc, resultados, clasificaciones, fmt)
    if 'DUALTASK' in resultados['available_tests']:
        _add_dualtask_section(doc, resultados, clasificaciones, fmt)

    _add_summary(doc, resultados, clasificaciones, fmt)
    return doc


def guardar_informe(doc, ruta_salida):
    os.makedirs(os.path.dirname(ruta_salida), exist_ok=True)
    doc.save(ruta_salida)
