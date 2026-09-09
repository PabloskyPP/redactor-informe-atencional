"""
Módulo para generar el informe vocacional en formato DOCX.
"""
import os
import math
import io
from datetime import datetime

from docx import Document
from docx.shared import Pt, Inches, RGBColor, Emu, Cm
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
from PIL import Image, ImageDraw, ImageFont

from textos import (
    PARRAFOS_FIJOS,
    PARRAFO_ANT_TR,

)

# ---------------------------------------------------------------------------
# Utilidades generales
# ---------------------------------------------------------------------------

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
    """Añade un párrafo con texto en negrita."""
    p   = doc.add_paragraph()
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


# ---------------------------------------------------------------------------
# Portada
# ---------------------------------------------------------------------------


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
        run_fa = info.add_run(f"Fecha de aplicación: {datos['fecha_aplicacion']}\n")
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
         "ANT, CPT, FourFigures y DUAL-TASK."
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
        section.top_margin    = Inches(1)
        section.bottom_margin = Inches(1)
        section.left_margin   = Inches(1)
        section.right_margin  = Inches(1)

    nombre_completo = resultados.get('nombre_completo') or nombre_caso
    nombre          = resultados.get('nombre')          or nombre_caso
    fmt             = {'nombre': nombre, 'nombre_completo': nombre_completo}

    datos_portada = {
        'edad':             resultados.get('edad'),
        'fecha_aplicacion': resultados.get('fecha_aplicacion'),
    }

    top3_riasec = resultados.get('top3_riasec', [])
    top3_im     = resultados.get('top3_inteligencia_multiple', [])

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
    doc.add_paragraph(PARRAFOS_FIJOS['descripcion_procedimiento2.2'])
    doc.add_paragraph(PARRAFOS_FIJOS['descripcion_procedimiento3.1'])
    doc.add_paragraph(PARRAFOS_FIJOS['descripcion_procedimiento4.1'])
    doc.add_paragraph(PARRAFOS_FIJOS['descripcion_procedimiento5.1'])

    doc.add_paragraph()
    doc.add_paragraph(PARRAFOS_FIJOS['descripcion_indices'].format(**fmt))

    # ------------------------------------------------------------------ #
    # 3. RESULTADOS                                                        #
    # ------------------------------------------------------------------ #
    doc.add_page_break()

    titulo_res = doc.add_parag    _add_bold_paragraph(doc, PARRAFOS_FIJOS['titulo_indices'])
raph()
    titulo_res.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
    run_tr = titulo_res.add_run(PARRAFOS_FIJOS['titulo_resultados'].format(**fmt))
    run_tr.bold = True
    run_tr.font.size = Pt(13)

    doc.add_paragraph()
    doc.add_paragraph(PARRAFOS_FIJOS['texto_resultados'].format(**fmt))



    # ========================================================================
    # INSERTAR Tabla resultados
    # ========================================================================
    
    # Título de resultados
    titulo_resultados = doc.add_paragraph()
    titulo_resultados.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
    run = titulo_resultados.add_run(PARRAFOS_FIJOS['titulo_resultados'].format(nombre_completo=nombre_completo))
    run.bold = True
    run.font.size = Pt(11)
    doc.add_paragraph()  # Espacio
    
    doc.add_paragraph(PARRAFOS_FIJOS['texto__resultados'].format(nombre=nombre, nombre_completo=nombre_completo))

    # Tabla PDs, PTs y clasificaciones
    tabla = doc.add_table(rows=4, cols=10)

    # Aplicar estilo simple con bordes negros y encabezado con fondo gris claro
    tabla.style = 'Table Grid'
    # Aplicar fondo gris claro al encabezado
    for cell in tabla.rows[0].cells:
        cell._element.get_or_add_tcPr().append(parse_xml(r'<w:shd {} w:fill="D9D9D9"/>'.format(nsdecls('w'))))
    
    # Encabezados
    hdr_cells = tabla.rows[0].cells
    hdr_cells[0].text = ''
    hdr_cells[0.1].text = 'Pruebas'
    hdr_cells[0].2.text = 'Índices'
    hdr_cells[1].text = 'Arousal'
    hdr_cells[2].text = 'Atención Sostenida'
    hdr_cells[4].text = 'Control Ejecutivo'
    hdr_cells[4.1].text = 'Atención Selectiva'
    hdr_cells[4.2].text = 'Control Inhibitorio'
    hdr_cells[5].text = 'Flexibilidad Cognitiva'
    hdr_cells[6].text = 'Memoria operativa'
    hdr_cells[7].text = 'Velocidad de procesamiento'
    hdr_cells[8].text = 'Hiperactividad'


    # Centrar el texto en las celdas del encabezado
    for cell in hdr_cells:
        for paragraph in cell.paragraphs:
            paragraph.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
            
    # Fila 1: prueba ANT
    row1 = tabla.rows[1].cells
    row1[0].text = ''
    row1[0.1].text = 'ANT'
    row1[0.1.1].text = 'Punt. Directa'
    row1[0.1.2].text = 'Punt. Típica'
    row1[0.1.3].text = 'Rendimiento'
    row1[1].text = str(round(resultados.get('PD_A', 0), 4))
    row1[2].text = str(round(resultados.get('PD_C', 0), 4))
    row1[3].text = str(round(resultados.get('PD_O', 0), 4))
    row1[4].text = str(round(resultados.get('PD_F_A', 0), 4))
    row1[5].text = str(round(resultados.get('PD_F_TR', 0), 4))
    row1[6].text = str(round(resultados.get('PD_TR', 0), 4))
    row1[7].text = str(round(resultados.get('PD_TR_alerta', 0), 4))
    row1[8].text = str(round(resultados.get('PD_TR_orientacion', 0), 4))
    row1[9].text = str(round(resultados.get('PD_TR_ejecutivo', 0), 4))
    
    # Fila 2: prueba CPT
    row2 = tabla.rows[2].cells
    row1[0].text = ''
    row1[0.1].text = 'CPT'
    row1[0.1.1].text = 'Punt. Directa'
    row1[0.1.2].text = 'Punt. Típica'
    row1[0.1.3].text = 'Rendimiento'
    row2[1].text = str(resultados.get('PT_A', 0))
    row2[2].text = str(resultados.get('PT_C', 0))
    row2[3].text = str(resultados.get('PT_O', 0))
    row2[4].text = str(resultados.get('PT_F_A', 0))
    row2[5].text = str(resultados.get('PT_TR', 0))
    row2[6].text = str(resultados.get('PT_F_TR', 0))
    row2[7].text = str(resultados.get('PT_TR_alerta', 0))
    row2[8].text = str(resultados.get('PT_TR_orientacion', 0))
    row2[9].text = str(resultados.get('PT_TR_ejecutivo', 0))
    
    # Fila 3: prueba FourFigures
    row3 = tabla.rows[3].cells
    row1[0].text = ''
    row1[0].text = ''
    row1[0.1].text = 'FourFigures'
    row1[0.1.1].text = 'Punt. Directa'
    row1[0.1.2].text = 'Punt. Típica'
    row1[0.1.3].text = 'Rendimiento'
    row3[1].text = str(resultados.get('Clasificacion_A', '-'))
    row3[2].text = str(resultados.get('Clasificacion_C', '-'))
    row3[3].text = str(resultados.get('Clasificacion_O', '-'))
    row3[4].text = str(resultados.get('Clasificacion_F_A', '-'))
    row3[5].text = str(resultados.get('Clasificacion_F_TR', '-'))
    row3[6].text = str(resultados.get('Clasificacion_TR', '-'))
    row3[7].text = str(resultados.get('Clasificacion_TR_alerta', '-'))
    row3[8].text = str(resultados.get('Clasificacion_TR_orientacion', '-'))
    row3[9].text = str(resultados.get('Clasificacion_TR_ejecutivo', '-'))
    
    # Fila 4: prueba Dual-Task
    row3 = tabla.rows[3].cells
    row1[0].text = ''
    row1[0].text = ''
    row1[0.1].text = 'Dual-Task'
    row1[0.1.1].text = 'Punt. Directa'
    row1[0.1.2].text = 'Punt. Típica'
    row1[0.1.3].text = 'Rendimiento'
    row3[1].text = str(resultados.get('Clasificacion_A', '-'))
    row3[2].text = str(resultados.get('Clasificacion_C', '-'))
    row3[3].text = str(resultados.get('Clasificacion_O', '-'))
    row3[4].text = str(resultados.get('Clasificacion_F_A', '-'))
    row3[5].text = str(resultados.get('Clasificacion_F_TR', '-'))
    row3[6].text = str(resultados.get('Clasificacion_TR', '-'))
    row3[7].text = str(resultados.get('Clasificacion_TR_alerta', '-'))
    row3[8].text = str(resultados.get('Clasificacion_TR_orientacion', '-'))
    row3[9].text = str(resultados.get('Clasificacion_TR_ejecutivo', '-'))
    

    # Colorear celdas según el rendimiento
    # Verde si es alto, rojo si es bajo (columnas: Aciertos, Alerta, Orientación, Ejecutivo)
    green_if_high = [1, 4, 5, 9]
    # Rojo si es alto, verde si es bajo (columnas: Comisiones, Omisiones, Fatiga precisión, Fatiga velocidad, Velocidad)
    red_if_high = [2, 3, 4, 5, 6, 7, 8]
    
    for idx in green_if_high:
        clasificacion = str(row3[idx].text).lower()
        if clasificacion == 'alto':
            row3[idx]._element.get_or_add_tcPr().append(parse_xml(r'<w:shd {} w:fill="90EE90"/>'.format(nsdecls('w'))))
        elif clasificacion == 'bajo':
            row3[idx]._element.get_or_add_tcPr().append(parse_xml(r'<w:shd {} w:fill="FF6B6B"/>'.format(nsdecls('w'))))
    
    for idx in red_if_high:
        clasificacion = str(row3[idx].text).lower()
        if clasificacion == 'alto':
            row3[idx]._element.get_or_add_tcPr().append(parse_xml(r'<w:shd {} w:fill="FF6B6B"/>'.format(nsdecls('w'))))
        elif clasificacion == 'bajo':
            row3[idx]._element.get_or_add_tcPr().append(parse_xml(r'<w:shd {} w:fill="90EE90"/>'.format(nsdecls('w'))))

    # Centrar el texto en las celdas de las filas 1, 2 y 3
    for row in [row1, row2, row3]:
        for cell in row:
            for paragraph in cell.paragraphs:
                paragraph.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
    
    doc.add_paragraph()  # Espacio



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

    # Ordenar factores de mayor a menor PCT
    orden = sorted(factores_info.keys(),
                   key=lambda k: resultados.get(f'PCT_{k}', 0), reverse=True)

    destino = tabla_destino_cell if tabla_destino_cell is not None else doc

    titulo = destino.add_paragraph("Tu perfil completo")
    titulo.runs[0].bold = True
    titulo.runs[0].font.size = Pt(11)
    _no_space_before_after(titulo)

    for clave in orden:
        info = factores_info[clave]
        pct  = resultados.get(f'PCT_{clave}', 0)
        r, g, b = info['color']
        hex_color = _rgb_to_hex(info['color'])

        # --- Párrafo de encabezado: nombre + porcentaje ---
        p_header = destino.add_paragraph()
        _no_space_before_after(p_header)
        run_letra = p_header.add_run(f"[{clave}] {info['nombre']}  ")
        run_letra.bold = True
        run_letra.font.size = Pt(9)
        run_pct = p_header.add_run(f"{pct}%")
        run_pct.font.size  = Pt(9)
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
        run_empty.font.color.rgb = RGBColor(200, 200, 200)
        run_empty.font.size      = Pt(9)

        # Pequeño espacio
        sep = destino.add_paragraph()
        _no_space_before_after(sep)



    # ================================================================== #
    # Secciones particulares de cada prueba                                                           #
    # ================================================================== #

    _add_bold_paragraph(doc, PARRAFOS_FIJOS['titulo_resultados_específicos'])



    # ================================================================== #
    # 3.0 ACS                                                           #
    # ================================================================== #
    p_tit_r = doc.add_paragraph("ACS - cuestionario de control atencionals")
    _add_bold_paragraph(doc, PARRAFOS_FIJOS['titulo_ACS'])
    _add_bold_paragraph(doc, PARRAFOS_FIJOS['texto_resultados_ACS'])

    # Normalizar nivel para selección de párrafo
    tr_nivel = normalizar_nivel(clasificaciones['ACS_atenciongeneral'])
    doc.add_paragraph(PARRAFO_ACS_atenciongeneral[tr_nivel])

    # Gráficas, barras ACS.
    #Revisar recuperación de datos de esta función en estos tres índices
    _add_bars_section(doc, ACS_INFO, resultados_ACS_atenciongeneral, tabla_destino_cell=None)

    tr_nivel = normalizar_nivel(clasificaciones['ACS_foco'])
    doc.add_paragraph(PARRAFO_ACS_foco[tr_nivel])
    #Revisar recuperación de datos de esta función
    _add_bars_section(doc, ACS_INFO, resultados_ACS_foco, tabla_destino_cell=None)

    tr_nivel = normalizar_nivel(clasificaciones['ACS_cambio'])
    doc.add_paragraph(PARRAFO_ACS_cambio[tr_nivel])
    #Revisar recuperación de datos de esta función
    _add_bars_section(doc, ACS_INFO, resultados_ACS_cambio, tabla_destino_cell=None)


    # ================================================================== #
    # 3.1 ANT                                                           #
    # ================================================================== #
  
    doc.add_paragraph()

    #Elegir uno de ambos títulos 
    p_tit_r = doc.add_paragraph("ANT - prueba de eficiencia de redes neuronales atencionales")
    _add_bold_paragraph(doc, PARRAFOS_FIJOS['titulo_ANT'])

    p_tit_r.runs[0].bold      = True
    p_tit_r.runs[0].underline = True

    # VELOCIDAD DE PROCESAMIENTO
    p_tr_titulo = doc.add_paragraph()
    run = p_tr_titulo.add_run("🔹 Velocidad de procesamiento / Tiempo de respuesta (TR)")
    run.bold = True
    run.font.size = Pt(11)

    # Normalizar nivel para selección de párrafo
    tr_nivel = normalizar_nivel(clasificaciones['ANT_TR'])
    
    doc.add_paragraph(PARRAFO_ANT_TR[tr_nivel])


    # ACIERTOS
    p_a_titulo = doc.add_paragraph()
    run = p_c_titulo.add_run("🔹 Número de aciertos (A)")
    run.bold = True
    run.font.size = Pt(11)
    
    # Normalizar nivel para selección de párrafo
    a_nivel = normalizar_nivel(clasificaciones['ANT_A'])
    
    doc.add_paragraph(PARRAFO_ANT_C[a_nivel])


    # ERRORES DE COMISIÓN
    p_c_titulo = doc.add_paragraph()
    run = p_c_titulo.add_run("🔹 Errores de comisión (C)")
    run.bold = True
    run.font.size = Pt(11)
    
    # Normalizar nivel para selección de párrafo
    c_nivel = normalizar_nivel(clasificaciones['ANT_C'])
    
    doc.add_paragraph(PARRAFO_ANT_C[c_nivel])
    
    # ERRORES DE OMISIÓN
    p_o_titulo = doc.add_paragraph()
    run = p_o_titulo.add_run("🔹 Precisión y errores de omisión (O)")
    run.bold = True
    run.font.size = Pt(11)
    
    # Normalizar nivel para selección de párrafo
    o_nivel = normalizar_nivel(clasificaciones['ANT_O'])
    
    doc.add_paragraph(PARRAFO_ANT_O[o_nivel])
    
    # FATIGA
    p_f_titulo = doc.add_paragraph()
    run = p_f_titulo.add_run("🔹 Atención Sostenida / Fatiga")
    run.bold = True
    run.font.size = Pt(11)
    
    # Normalizar nivel para selección de párrafo
    con_nivel = normalizar_nivel(clasificaciones['ANT_F'])
    
    doc.add_paragraph(PARRAFO_ANT_F[con_nivel])

    # REDES NEURONALES (ALERTA, ORIENTACIÓN, EJECUTIVA)
    p_f_titulo = doc.add_paragraph()
    run = p_f_titulo.add_run("🔹 Redes neuronales atencionales")
    run.bold = True
    run.font.size = Pt(11)
    
    # Normalizar nivel para selección de párrafo
    con_nivel = normalizar_nivel(clasificaciones['ANT_TR_alerta'])
    con_nivel = normalizar_nivel(clasificaciones['ANT_TR_orientacion'])
    con_nivel = normalizar_nivel(clasificaciones['ANT_TR_ejecutivo'])

    doc.add_paragraph(PARRAFO_ANT_alerta[con_nivel])
    # Revisar esta función de añadir grafico barras para estos tres índices
    _add_bars_section(doc, ANT_INFO, resultados_ANT_TR_alerta, tabla_destino_cell=None)
    doc.add_paragraph(PARRAFO_ANT_orientacion[con_nivel])
    _add_bars_section(doc, ANT_INFO, resultados_ANT_TR_orientacion, tabla_destino_cell=None)
    doc.add_paragraph(PARRAFO_ANT_ejecutivo[con_nivel])
    _add_bars_section(doc, ANT_INFO, resultados_ANT_TR_ejecutivo, tabla_destino_cell=None)



    # ================================================================== #
    # 3.2  CPT                                         # o D2 si el caso
    # ================================================================== #
    doc.add_page_break()
    p_tit_im = doc.add_paragraph()
    p_tit_r = doc.add_paragraph("CPT - prueba de rendimiento continuo")
    p_tit_im.runs[0].bold      = True
    p_tit_im.runs[0].underline = True

# Párrafos condicionales CPT

    # VELOCIDAD DE PROCESAMIENTO
    p_tr_titulo = doc.add_paragraph()
    run = p_tr_titulo.add_run("🔹 Velocidad de procesamiento / Tiempo de respuesta (TR)")
    run.bold = True
    run.font.size = Pt(11)
    
    # Normalizar nivel para selección de párrafo
    tr_nivel = normalizar_nivel(clasificaciones['CPT_TR'])
    
    doc.add_paragraph(PARRAFO_CPT_TR[tr_nivel])
    
    # ERRORES DE COMISIÓN
    p_c_titulo = doc.add_paragraph()
    run = p_c_titulo.add_run("🔹 Comisiones (C)")
    run.bold = True
    run.font.size = Pt(11)
    
    # Normalizar nivel para selección de párrafo
    c_nivel = normalizar_nivel(clasificaciones['CPT_C'])
    
    doc.add_paragraph(PARRAFO_CPT_C[c_nivel])

    # ERRORES DE OMISIÓN
    p_o_titulo = doc.add_paragraph()
    run = p_o_titulo.add_run("🔹 Omisiones (O)")
    run.bold = True
    run.font.size = Pt(11)
    
    # Normalizar nivel para selección de párrafo
    o_nivel = normalizar_nivel(clasificaciones['CPT_O'])
    
    doc.add_paragraph(PARRAFO_CPT_O[o_nivel])
    
    # CONCENTRACIÓN
    p_con_titulo = doc.add_paragraph()
    run = p_con_titulo.add_run("🔹 Concentración (CON)")
    run.bold = True
    run.font.size = Pt(11)
    
    # Normalizar nivel para selección de párrafo
    con_nivel = normalizar_nivel(clasificaciones['CPT_CON'])
    
    doc.add_paragraph(PARRAFOS_CPT_CON[con_nivel])

    # VARIABILIDAD
    p_var_titulo = doc.add_paragraph()
    run = p_var_titulo.add_run("🔹 Variabilidad del rendimiento (VAR)")
    run.bold = True
    run.font.size = Pt(11)
    
    # Seleccionar párrafo VAR según condición especial
    var_key = clasificaciones['CPT_VAR']
    if clasificaciones.get('VAR_especial', False) and var_key in ['alto', 'muy alto']:
        var_key = var_key + '_especial'
    
    doc.add_paragraph(PARRAFO_CPT_VAR[var_key].format(nombre=nombre))

    doc.add_paragraph()  # Espacio



# Párrafos condicionales FourFigures o FiveDigits


    doc.add_paragraph()

#Elegir uno de ambos títulos 
    p_tit_r = doc.add_paragraph("FourFigures")
    _add_bold_paragraph(doc, PARRAFOS_FIJOS['titulo_FourFigures'])

    p_tit_r.runs[0].bold      = True
    p_tit_r.runs[0].underline = True

    # VELOCIDAD DE PROCESAMIENTO
    p_tr_titulo = doc.add_paragraph()
    run = p_tr_titulo.add_run("🔹 Velocidad de procesamiento / Tiempo de respuesta (TR)")
    run.bold = True
    run.font.size = Pt(11)

    # Normalizar nivel para selección de párrafo
    tr_nivel = normalizar_nivel(clasificaciones['FourFigures_TR'])
    
    doc.add_paragraph(PARRAFO_FourFigures_TR[tr_nivel])


    # ACIERTOS
    p_a_titulo = doc.add_paragraph()
    run = p_c_titulo.add_run("🔹 Número de aciertos (A)")
    run.bold = True
    run.font.size = Pt(11)
    
    # Normalizar nivel para selección de párrafo
    a_nivel = normalizar_nivel(clasificaciones['FourFigures_A'])
    
    doc.add_paragraph(PARRAFO_FourFigures_C[a_nivel])


    # ERRORES DE COMISIÓN
    p_c_titulo = doc.add_paragraph()
    run = p_c_titulo.add_run("🔹 Errores de comisión (C)")
    run.bold = True
    run.font.size = Pt(11)
    
    # Normalizar nivel para selección de párrafo
    c_nivel = normalizar_nivel(clasificaciones['FourFigures_C'])
    
    doc.add_paragraph(PARRAFO_FourFigures_C[c_nivel])
    

    # ERRORES DE COMISIÓN
    p_c_titulo = doc.add_paragraph()
    run = p_c_titulo.add_run("🔹 Errores de comisión (C)")
    run.bold = True
    run.font.size = Pt(11)
    
    # Normalizar nivel para selección de párrafo
    c_nivel = normalizar_nivel(clasificaciones['FourFigures_P4_A_obtenido_vs_esperado'])
    
    doc.add_paragraph(PARRAFO_FourFigures_P4_A_obtenido_vs_esperado[c_nivel])


    # ============================================
    # Párrafos condicionales DigitsMemorization

    # ERRORES DE COMISIÓN
    p_c_titulo = doc.add_paragraph()
    run = p_c_titulo.add_run("🔹 Memoria operativa o de trabajo")
    run.bold = True
    run.font.size = Pt(11)
    
    # Normalizar nivel para selección de párrafo
    c_nivel = normalizar_nivel(clasificaciones['DigitsMemorization_PDpromedio'])
    
    doc.add_paragraph(PARRAFO_DigitsMemorization
[c_nivel])

    # ============================================

    # Párrafos condicionales DUAL-TASK


    # Rendimiento general 
    p_tr_titulo = doc.add_paragraph()
    run = p_tr_titulo.add_run("🔹 Rendimiento general")
    run.bold = True
    run.font.size = Pt(11)
    
    # Normalizar nivel para selección de párrafo
    tr_nivel = normalizar_nivel(clasificaciones['DUALTASK_General_PSV_y_A'])
    
    doc.add_paragraph(PARRAFO_DUALTASK_General_PSV_y_A[tr_nivel])
    doc.add_paragraph(PARRAFO_DUALTASK_si_inestable[tr_nivel])


    # Memoria de trabajo
    p_tr_titulo = doc.add_paragraph()
    run = p_tr_titulo.add_run("🔹 Memoria de trabajo o memoria operativa")
    run.bold = True
    run.font.size = Pt(11)
    
    # Normalizar nivel para selección de párrafo
    tr_nivel = normalizar_nivel(clasificaciones['DUALTASK_Rendimiento_General_cuando_concurrencia'])
    
    doc.add_paragraph(PARRAFO_DUALTASK_Rendimiento_General_cuando_concurrencia[tr_nivel])


    # Estilo atencional multitarea
    p_tr_titulo = doc.add_paragraph()
    run = p_tr_titulo.add_run("🔹 Estilo atencional multitarea")
    run.bold = True
    run.font.size = Pt(11)
    
    # Normalizar nivel para selección de párrafo
    tr_nivel = normalizar_nivel(clasificaciones['DUALTASK_PSV_cuando_concurrencia'])
    
    doc.add_paragraph(PARRAFO_DUALTASK_PSV_cuando_concurrencia[tr_nivel])


    # Empiezan párrafos análisis pormenorizado índices tareas por individual.
    doc.add_paragraph(PARRAFOS_FIJOS['introduccion_analisis_tareas_DualTask'].format(nombre=nombre, nombre_completo=nombre_completo))


    # Precisión seguimiento visomotor y movimiento fino
    p_tr_titulo = doc.add_paragraph()
    run = p_tr_titulo.add_run("🔹 Precisión seguimiento visomotor y movimiento fino (PSV)")
    run.bold = True
    run.font.size = Pt(11)
    
    # Normalizar nivel para selección de párrafo
    tr_nivel = normalizar_nivel(clasificaciones['DUALTASK_PSV'])
    
    doc.add_paragraph(PARRAFO_DUALTASK_PSV[tr_nivel])


    # VELOCIDAD DE PROCESAMIENTO
    p_tr_titulo = doc.add_paragraph()
    run = p_tr_titulo.add_run("🔹 Velocidad de procesamiento / Tiempo de respuesta (TR)")
    run.bold = True
    run.font.size = Pt(11)
    
    # Normalizar nivel para selección de párrafo
    tr_nivel = normalizar_nivel(clasificaciones['DUALTASK_TR'])
    
    doc.add_paragraph(PARRAFO_DUALTASK_TR[tr_nivel])
    
    # ERRORES DE COMISIÓN
    p_c_titulo = doc.add_paragraph()
    run = p_c_titulo.add_run("🔹 Comisiones (C)")
    run.bold = True
    run.font.size = Pt(11)
    
    # Normalizar nivel para selección de párrafo
    c_nivel = normalizar_nivel(clasificaciones['DUALTASK_C'])
    
    doc.add_paragraph(PARRAFO_DUALTASK_C[c_nivel])
    doc.add_paragraph(PARRAFO_DUALTASK_TR_A_vs_C[c_nivel])


    # ERRORES DE OMISIÓN
    p_o_titulo = doc.add_paragraph()
    run = p_o_titulo.add_run("🔹 Omisiones (O)")
    run.bold = True
    run.font.size = Pt(11)
    
    # Normalizar nivel para selección de párrafo
    o_nivel = normalizar_nivel(clasificaciones['DUALTASK_O'])
    
    doc.add_paragraph(PARRAFO_DUALTASK_O[o_nivel])
    
    # FATIGA
    p_con_titulo = doc.add_paragraph()
    run = p_con_titulo.add_run("🔹 Atención sostenida / Fatiga")
    run.bold = True
    run.font.size = Pt(11)
    
    # Normalizar nivel para selección de párrafo
    con_nivel = normalizar_nivel(clasificaciones['DUALTASK_F'])
    
    doc.add_paragraph(PARRAFOS_DUALTASK_Fatiga[con_nivel])

    # AUTOMATIZACIÓN
    p_var_titulo = doc.add_paragraph()
    run = p_var_titulo.add_run("🔹 Automatización")
    run.bold = True
    run.font.size = Pt(11)

    # Normalizar nivel para selección de párrafo
    con_nivel = normalizar_nivel(clasificaciones['DUALTASK_automatización'])
    
    doc.add_paragraph(PARRAFOS_DUALTASK_automatización[con_nivel])


    # Párrafos DUAL-TASK finales opcionales: recomendaciones de tratamiento          #
    p_var_titulo = doc.add_paragraph()
    run = p_var_titulo.add_run("🔹 Recomendación")
    run.bold = True
    run.font.size = Pt(11)

    nivel_general_dt = clasificaciones.get('DUALTASK_General_PSV_y_A')
    nivel_psv        = normalizar_nivel(clasificaciones['DUALTASK_PSV'])
    nivel_t2         = normalizar_nivel(clasificaciones['DUALTASK_A'])
    nivel_c          = normalizar_nivel(clasificaciones['DUALTASK_C'])
    concurrencia     = clasificaciones.get('DUALTASK_PSV_cuando_concurrencia', '')
    fatiga_nivel     = clasificaciones.get('DUALTASK_F')
    tr_a_vs_c        = clasificaciones.get('DUALTASK_TR_A_vs_C')  # 'positivo', 'negativo' o None si no es significativo

    hay_parrafos_finales = (
        nivel_general_dt in ('Inestable y negativo', 'Muy inestable')
        or (nivel_psv == 'alto' and nivel_t2 == 'normal')
        or (nivel_psv in ('normal', 'alto') and nivel_t2 == 'bajo')
        or (nivel_t2 == 'alto' and nivel_psv == 'normal')
        or (nivel_t2 in ('normal', 'alto') and nivel_psv == 'bajo')
        or (concurrencia.startswith('deterioro') and nivel_t2 == 'bajo')
        or nivel_psv == 'bajo'
        or (nivel_c in ('normal', 'alto') and tr_a_vs_c is not None)
        or (fatiga_nivel is not None and fatiga_nivel != 'no F')
    )

    if hay_parrafos_finales:
        doc.add_paragraph()
        _add_bold_paragraph(doc, "4. Recomendaciones")
        doc.add_paragraph(PARRAFO_DUALTASK_final_intro['intro'])

        # T1 y T2 muy dispares, con resultado global negativo o muy inestable
        if nivel_general_dt in ('Inestable y negativo', 'Muy inestable'):
            doc.add_paragraph(PARRAFO_DUALTASK_final_inestable_negativo_o_muy_inestable['si'])

        # T1 alto y T2 normal
        if nivel_psv == 'alto' and nivel_t2 == 'normal':
            doc.add_paragraph(PARRAFO_DUALTASK_final_inestable_mejor_T1_y_T2_positivo['si'])

        # T1 normal o alto y T2 bajo
        if nivel_psv in ('normal', 'alto') and nivel_t2 == 'bajo':
            doc.add_paragraph(PARRAFO_DUALTASK_final_inestable_mejor_T1_y_T2_negativo['si'])

        # T2 alto y T1 normal
        if nivel_t2 == 'alto' and nivel_psv == 'normal':
            doc.add_paragraph(PARRAFO_DUALTASK_final_inestable_mejor_T2_y_T1_positivo['si'])

        # T2 normal o alto y T1 bajo
        if nivel_t2 in ('normal', 'alto') and nivel_psv == 'bajo':
            doc.add_paragraph(PARRAFO_DUALTASK_final_inestable_mejor_T2_y_T1_negativo['si'])

        # Deterioro de T1 en concurrencia junto con mal rendimiento en T2
        if concurrencia.startswith('deterioro') and nivel_t2 == 'bajo':
            doc.add_paragraph(PARRAFO_DUALTASK_final_concurrencia_peorT1_malT2['si'])

        # T1 (PSV) bajo
        if nivel_psv == 'bajo':
            doc.add_paragraph(PARRAFO_DUALTASK_final_PSV_bajo['si'])

        # C en T2 normal o alto, con diferencia significativa entre TR de aciertos y comisiones
        if nivel_c in ('normal', 'alto') and tr_a_vs_c is not None:
            clave = 'impulsividad' if tr_a_vs_c == 'positivo' else 'distraibilidad'
            doc.add_paragraph(PARRAFO_DUALTASK_final_dif_TR_A_y_C[clave])

        # Algún índice de fatiga significativo (PSV, A o TR)
        if fatiga_nivel is not None and fatiga_nivel != 'no F':
            doc.add_paragraph(PARRAFO_DUALTASK_final_fatiga['si'])


    # ================================================================== #
    # Párrafo síntesis final         #
    # ================================================================== #

# Párrafo final de prueba

    p_con_titulo = doc.add_paragraph()
    run = p_con_titulo.add_run("SÍNTESIS FINAL")
    run.bold = True
    run.font.size = Pt(15)

    doc.add_paragraph(PARRAFOS_FIJOS['título_sintesis_final'])

    # Normalizar nivel para selección de párrafo
    con_nivel = normalizar_nivel(clasificaciones['PARRAFO_sintesis_arousal'])
    
    doc.add_paragraph(PARRAFO_sintesis_arousal[con_nivel])

    # Normalizar nivel para selección de párrafo
    con_nivel = normalizar_nivel(clasificaciones['PARRAFO_sintesis_atencionsostenida '])
    
    doc.add_paragraph(PARRAFO_sintesis_atencionsostenida [con_nivel])

    # Normalizar nivel para selección de párrafo
    con_nivel = normalizar_nivel(clasificaciones['PARRAFO_sintesis_controlejecutivo'])
    
    doc.add_paragraph(PARRAFO_sintesis_controlejecutivo[con_nivel])

    # Normalizar nivel para selección de párrafo
    con_nivel = normalizar_nivel(clasificaciones['PARRAFO_sintesis_flexibilidadcognitiva'])
    
    doc.add_paragraph(PARRAFO_sintesis_flexibilidadcognitiva[con_nivel])

    # Normalizar nivel para selección de párrafo
    con_nivel = normalizar_nivel(clasificaciones['PARRAFO_sintesis_memoriatrabajo'])
    
    doc.add_paragraph(PARRAFO_sintesis_memoriatrabajo[con_nivel])

    # Normalizar nivel para selección de párrafo
    con_nivel = normalizar_nivel(clasificaciones['PARRAFO_sintesis_velocidadprocesamiento'])
    
    doc.add_paragraph(PARRAFO_sintesis_velocidadprocesamiento[con_nivel])

    # Normalizar nivel para selección de párrafo
    con_nivel = normalizar_nivel(clasificaciones['PARRAFO_sintesis_final'])
    
    doc.add_paragraph(PARRAFO_sintesis_final[con_nivel])



def guardar_informe(doc, ruta_salida):
    """
    Guarda el documento generado.

    Args:
        doc:         Documento Word.
        ruta_salida: Ruta donde guardar el archivo.
    """
    doc.save(ruta_salida)
    print(f"Informe generado exitosamente en: {ruta_salida}")
