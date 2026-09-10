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
from docx.oxml.ns import qn, nsdecls
from docx.oxml import OxmlElement, parse_xml
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

    titulo_res = doc.add_paragraph()
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
    tabla = doc.add_table(rows=2, cols=8)

    # Aplicar estilo simple con bordes negros y encabezado con fondo gris claro
    tabla.style = 'Table Grid'
    
    # Aplicar fondo gris claro al encabezado (filas 0 y 1)
    for row_idx in [0, 1]:
        for cell in tabla.rows[row_idx].cells:
            cell._element.get_or_add_tcPr().append(parse_xml(r'<w:shd {} w:fill="D9D9D9"/>'.format(nsdecls('w'))))
    
    # ========== FILA 0: Encabezados principales ==========
    hdr_cells = tabla.rows[0].cells
    hdr_cells[0].text = ''
    hdr_cells[1].text = 'Arousal'
    hdr_cells[2].text = 'Atención Sostenida'
    hdr_cells[3].text = 'Control Ejecutivo'
    hdr_cells[5].text = 'Flexibilidad Cognitiva'
    hdr_cells[6].text = 'Memoria operativa'
    hdr_cells[7].text = 'Velocidad de procesamiento'
    
    # Hacer merge horizontal de las celdas 3 y 4 en la fila 0 para "Control Ejecutivo"
    # Usando vMerge para combinar con la fila siguiente
    tcPr = hdr_cells[3]._element.get_or_add_tcPr()
    tcMer = OxmlElement('w:gridSpan')
    tcMer.set(qn('w:val'), '2')
    tcPr.append(tcMer)
    
    # Eliminar el contenido de la celda 4 ya que está mergeada
    hdr_cells[4].text = ''
    
    # ========== FILA 1: Subrencabezados para Control Ejecutivo ==========
    sub_hdr = tabla.rows[1].cells
    sub_hdr[0].text = ''
    sub_hdr[1].text = ''
    sub_hdr[2].text = ''
    sub_hdr[3].text = 'Atención Selectiva'
    sub_hdr[4].text = 'Control Inhibitorio (impulsividad)'
    sub_hdr[5].text = ''
    sub_hdr[6].text = ''
    sub_hdr[7].text = ''
    
    # Hacer merge vertical de las celdas que no tienen subrencabezados
    # Para las columnas: 1 (Arousal), 2 (Atención Sostenida), 5 (Flexibilidad), 6 (Memoria), 7 (Velocidad)
    for col_idx in [1, 2, 5, 6, 7]:
        # Agregar vMerge restart a la fila 0
        tcPr_start = hdr_cells[col_idx]._element.get_or_add_tcPr()
        vMerge_start = OxmlElement('w:vMerge')
        vMerge_start.set(qn('w:val'), 'restart')
        tcPr_start.append(vMerge_start)
        
        # Agregar vMerge continue a la fila 1
        tcPr_end = sub_hdr[col_idx]._element.get_or_add_tcPr()
        vMerge_end = OxmlElement('w:vMerge')
        tcPr_end.append(vMerge_end)

    # Centrar el texto en las celdas del encabezado
    for row_idx in [0, 1]:
        for cell in tabla.rows[row_idx].cells:
            for paragraph in cell.paragraphs:
                paragraph.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER

                
    
    # Agregar filas de datos
    tabla.add_row()  # Fila 2 para ANT
    tabla.add_row()  # Fila 3 para CPT
    
    # Función auxiliar para crear tabla anidada en celda [0]
    def _crear_tabla_anidada_prueba(celda_destino, nombre_prueba):
        """
        Crea una tabla anidada dentro de una celda con:
        - Izquierda: nombre de la prueba
        - Derecha: 3 filas con 'Índice', 'PD', 'Rendimiento'
        """
        # Crear tabla anidada: 2 columnas x 3 filas
        tabla_anidada = celda_destino.add_table(rows=3, cols=2)
        tabla_anidada.style = 'Table Grid'
        
        # Columna izquierda: nombre de la prueba (mergear verticalmente)
        for i in range(3):
            tabla_anidada.rows[i].cells[0].text = nombre_prueba if i == 0 else ''
        
        # Mergear las celdas de la columna izquierda
        cell_0_0 = tabla_anidada.rows[0].cells[0]._tc
        tcPr = cell_0_0.get_or_add_tcPr()
        vMerge = OxmlElement('w:vMerge')
        vMerge.set(qn('w:val'), 'restart')
        tcPr.append(vMerge)
        
        for i in range(1, 3):
            cell_i_0 = tabla_anidada.rows[i].cells[0]._tc
            tcPr = cell_i_0.get_or_add_tcPr()
            vMerge = OxmlElement('w:vMerge')
            tcPr.append(vMerge)
        
        # Columna derecha: Índice, PD, Rendimiento
        tabla_anidada.rows[0].cells[1].text = 'Índice'
        tabla_anidada.rows[1].cells[1].text = 'PD'
        tabla_anidada.rows[2].cells[1].text = 'Rendimiento'
        
        # Centrar texto
        for row in tabla_anidada.rows:
            for cell in row.cells:
                for para in cell.paragraphs:
                    para.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
        
        return tabla_anidada
    
    # Función auxiliar para llenar tabla anidada en celda de datos
    def _llenar_tabla_anidada_datos(celda_destino, nombre_indice, valor_pd, valor_rendimiento):
        """
        Crea una tabla anidada dentro de una celda de datos con:
        - Fila 1: Nombre del índice
        - Fila 2: Valor PD
        - Fila 3: Valor Rendimiento
        """
        tabla_anidada = celda_destino.add_table(rows=3, cols=1)
        tabla_anidada.style = 'Table Grid'
        
        tabla_anidada.rows[0].cells[0].text = str(nombre_indice)
        tabla_anidada.rows[1].cells[0].text = str(valor_pd)
        tabla_anidada.rows[2].cells[0].text = str(valor_rendimiento)
        
        # Centrar texto
        for row in tabla_anidada.rows:
            for cell in row.cells:
                for para in cell.paragraphs:
                    para.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
        
        return tabla_anidada
    
    # Función auxiliar para llenar tabla anidada con múltiples índices
    def _llenar_tabla_anidada_multiples_indices(celda_destino, indices_datos):
        """
        Crea una tabla anidada dentro de una celda con múltiples índices lado a lado.
        
        Args:
            celda_destino: Celda donde insertar la tabla anidada
            indices_datos: Lista de tuplas (nombre_indice, valor_pd, valor_rendimiento)
        
        Estructura (3 filas × N columnas):
        - Fila 0: Nombres de índices (A, TR, O, etc.)
        - Fila 1: Valores PD
        - Fila 2: Valores Rendimiento
        """
        tabla_anidada = celda_destino.add_table(rows=3, cols=len(indices_datos))
        tabla_anidada.style = 'Table Grid'
        
        for col_idx, (nombre_indice, valor_pd, valor_rendimiento) in enumerate(indices_datos):
            tabla_anidada.rows[0].cells[col_idx].text = str(nombre_indice)
            tabla_anidada.rows[1].cells[col_idx].text = str(valor_pd)
            tabla_anidada.rows[2].cells[col_idx].text = str(valor_rendimiento)
        
        # Centrar texto en todas las celdas
        for row in tabla_anidada.rows:
            for cell in row.cells:
                for para in cell.paragraphs:
                    para.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
        
        return tabla_anidada
    
    # Asignación de contenido celdads para cada fila

    # Fila 2: prueba ANT
    row_ant = tabla.rows[2].cells
    _crear_tabla_anidada_prueba(row_ant[0], 'ANT')
    
    # Columna 1: Arousal (Red de Alerta)
    _llenar_tabla_anidada_datos(
        row_ant[1],
        'Red de Alerta',
        str(round(resultados.get('PD_ANT_TR_alerta', 0), 4)),
        str(clasificaciones.get('ANT_TR_alerta', '-'))
    )
    
    # Columna 2: Atención Sostenida - Múltiples índices (A y TR)
    _llenar_tabla_anidada_multiples_indices(
        row_ant[2],
        [
            ('Dif. A* 1º vs 3º',
             str(round(resultados.get('PD_ANT_A_principio_vs_final', 0), 4)),
             str(clasificaciones.get('ANT_A_principio_vs_final', '-'))),
            ('Dif. TR* 1º vs 3º',
             str(round(resultados.get('PD_ANT_TR_principio_vs_final', 0), 4)),
             str(clasificaciones.get('ANT_TR_principio_vs_final', '-')))
        ]
    )

# Copilot. Los índices de C y Red ejecutiva son comunes a la atención selectiva y el control inhibitorio, anidar de esta manera dentro de la columna control ejecutivo.
    # Columna 3: Control Ejecutivo - Atención Selectiva - Múltiples índices (Red de orientación, C y Red ejecutiva)
    _llenar_tabla_anidada_datos(
        row_ant[3],
        [
            ('Red de orientación',
             str(round(resultados.get('ANT_TR_orientacion', 0), 4)),
             str(clasificaciones.get('ANT_TR_orientacion', '-'))),
            ('Dif. TR 1º vs 3º',
             str(round(resultados.get('PD_ANT_C', 0), 4)),
             str(clasificaciones.get('ANT_C', '-'))),
            ('Red ejecutiva',
             str(round(resultados.get('ANT_TR_ejecutiva', 0), 4)),
             str(clasificaciones.get('ANT_TR_ejecutiva', '-')))
        ]
    )
    
    # Columna 4: Control Ejecutivo - Control Inhibitorio (vacío para ANT)
    _llenar_tabla_anidada_datos(
        row_ant[4],
        [
            ('Dif. TR 1º vs 3º',
             str(round(resultados.get('PD_ANT_C', 0), 4)),
             str(clasificaciones.get('ANT_C', '-'))),
            ('Red ejecutiva',
             str(round(resultados.get('ANT_TR_ejecutiva', 0), 4)),
             str(clasificaciones.get('ANT_TR_ejecutiva', '-')))
        ]
    )
    
    # Columna 5: Flexibilidad Cognitiva
    _llenar_tabla_anidada_datos(
        row_ant[5],
        'Flexibilidad',
        str(resultados.get('PT_TR_alerta', 0)),
        '-'
    )
    
    # Columna 6: Memoria operativa
    _llenar_tabla_anidada_datos(
        row_ant[6],
        'Memoria',
        str(resultados.get('PT_TR_orientacion', 0)),
        '-'
    )
    
    # Columna 7: Velocidad de procesamiento - Múltiples índices (O y TR)
    _llenar_tabla_anidada_multiples_indices(
        row_ant[7],
        [
            ('O*',
             str(round(resultados.get('PD_ANT_O', 0), 4)),
             str(clasificaciones.get('ANT_O', '-'))),
            ('TR',
             str(round(resultados.get('ANT_TR', 0), 4)),
             str(clasificaciones.get('ANT_TR', '-')))
        ]
    )
    
    # Fila 3: prueba CPT o D2 según cual se recupere del excel
    row_cpt = tabla.rows[3].cells
    # Añadir condicional texto según prueba recuperada del excel
    _crear_tabla_anidada_prueba(row_cpt[0], 'CPT' o 'D2')
    
    # Columna 1: Arousal
    _llenar_tabla_anidada_datos(
        row_cpt[1],
        'CON*',
        str(resultados.get('PD_CPT_CON', 0)),
        str(clasificaciones.get('CPT_CON', '-'))
    )
    
    # Columna 2: Atención Sostenida: VAR
    _llenar_tabla_anidada_multiples_indices(
        row_cpt[2],
        'VAR*',
        str(resultados.get('PD_CPT_VAR', 0)),
        str(clasificaciones.get('CPT_VAR', '-'))
        # Aquí se podría añadir una subcelda adicional: dif. sign A o TR 1º y 3º tercio = sing o no (color amarillo)
    )
    
    # Columna 3: Control ejecutivo - Atención Selectiva
    _llenar_tabla_anidada_datos(
        row_cpt[3],
        'O',
        str(round(resultados.get('PD_CPT_O', 0), 4)),
        str(clasificaciones.get('CPT_O', '-'))
    )
    
    # Columna 4: Control Ejecutivo - Control Inhibitorio (Fatiga A)
    _llenar_tabla_anidada_datos(
        row_cpt[4],
        'C*',
        str(resultados.get('PD_CPT_C', 0)),
        str(clasificaciones.get('CPT_C', '-'))
    )
    
    # Columna 5: Flexibilidad Cognitiva
    _llenar_tabla_anidada_datos(
        row_cpt[5],
        '',
        '',
        '',
    )
    
    # Columna 6: Memoria operativa
    _llenar_tabla_anidada_datos(
        row_cpt[6],
        '',
        '',
        '',
    )
    
    # Columna 7: Velocidad de procesamiento (R como número de elementos procesados, fijado en base al último elemento de la serie respondido)
    _llenar_tabla_anidada_datos(
        row_cpt[7],
        'R*',
        str(resultados.get('PD_CPT_R', 0)),
        str(clasificaciones.get('CPT_R', '-'))
    )


    # Fila 4: prueba FourFigures o FiveDigits, según la prueba que haya en el excel
    row_cpt = tabla.rows[3].cells
    # Copilot. Añadir condicional a prueba recuperada del excel
    _crear_tabla_anidada_prueba(row_cpt[0], 'FourFigures' o 'FiveDigits')
    
    # Columna 1: Arousal
    _llenar_tabla_anidada_datos(
        row_cpt[1],
        'A',
        str(resultados.get('PD_FourFigures_A', 0)),
        str(clasificaciones.get('FourFIgures_A', '-'))
    )
    
    # Columna 2: Atención Sostenida: VAR
    _llenar_tabla_anidada_multiples_indices(
        row_cpt[2],
        '',
        '',
        '',
    )
    
    # Columna 3 y 4: Control ejecutivo
    _llenar_tabla_anidada_datos(
        row_cpt[3],
        'C',
        str(resultados.get('PD_FourFigures_C', 0)),
        str(clasificaciones.get('FourFIgures_C', '-'))
    )
    
    # Columna 5: Flexibilidad Cognitiva
    _llenar_tabla_anidada_datos(
        row_cpt[5],
        'Dif. A P4 obtenida vs esperada*',
        str(resultados.get('PD_FourFigures_Dif_A_P4', 0)),
        # Aquí alto y color verde si la diferencia es positiva, y rojo si es negativa. No color si normal
        str(clasificaciones.get('FourFIgures_Dif_A_P4', '-'))
    )
    
    # Columna 6: Memoria operativa
    _llenar_tabla_anidada_datos(
        row_cpt[6],
        '',
        '',
        '',
    )
    
    # Columna 7: Velocidad de procesamiento (R como número de elementos procesados, fijado en base al último elemento de la serie respondido)
    _llenar_tabla_anidada_datos(
        row_cpt[7],
        'TR',
        str(resultados.get('PD_FourFigures_TR', 0)),
        str(clasificaciones.get('FourFigures_TR', '-'))
    )
    
    # Centrar el texto en todas las celdas de datos
    for row_idx in range(2, 4):
        for cell_idx in range(1, 8):  # Comenzar desde celda 1 (0 ya tiene tabla anidada)
            cell = tabla.rows[row_idx].cells[cell_idx]
            for paragraph in cell.paragraphs:
                paragraph.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER


    # Fila 5: prueba Dual-Task
    row_cpt = tabla.rows[3].cells
    # Copilot. Añadir condicional
    _crear_tabla_anidada_prueba(row_cpt[0], 'Dual-Task')
    
    # Columna 1: Arousal
    _llenar_tabla_anidada_datos(
        row_cpt[1],
        'O',
        str(resultados.get('PD_DUALTASK_O', 0)),
        str(clasificaciones.get('DUALTAS_O', '-'))
    )
    
    # Columna 2: Atención Sostenida - Múltiples índices (PSV T2, A y TR T1)
    _llenar_tabla_anidada_multiples_indices(
        row_cpt[2],
        [
            ('Dif. PSV* 1º y 3º tercio',
             str(round(resultados.get('PD_DUALTASK_PSV', 0), 4)),
             str(clasificaciones.get('DUALTASK_PSV', '-'))),
            ('Dif. A* 1º y 3º tercio',
             str(round(resultados.get('PD_DUALTASK_A', 0), 4)),
             str(clasificaciones.get('DUALTASK_A', '-'))),
            ('Dif. TR* 1º y 3º tercio',
             str(round(resultados.get('PD_DUALTASK_TR', 0), 4)),
             str(clasificaciones.get('DUALTASK_TR', '-')))
        ]
    )
    
    # Columna 3 y 4: Control ejecutivo
    _llenar_tabla_anidada_datos(
        row_cpt[3],
        'C',
        str(resultados.get('PD_DUALTASK_C', 0)),
        str(clasificaciones.get('DUALTASK_C', '-'))
    )
    
    # Columna 5: Flexibilidad Cognitiva
    _llenar_tabla_anidada_datos(
        row_cpt[5],
        '',
        '',
        '',
    )
    
    # Columna 6: Memoria operativa
    _llenar_tabla_anidada_datos(
        row_cpt[6],
        '',
        '',
        '',
    )
    
    # Columna 7: Velocidad de procesamiento
    _llenar_tabla_anidada_datos(
        row_cpt[7],
        'TR',
        str(resultados.get('PD_DUALTASK_TR', 0)),
        str(clasificaciones.get('DUALTASK_TR', '-'))
    )

    
    # Fila 6: prueba DIgitsMemorization
    row_cpt = tabla.rows[3].cells
    # Copilot. Añadir condicional
    _crear_tabla_anidada_prueba(row_cpt[0], 'Memorización de Dígitos')
    
    # Columna 1: Arousal
    _llenar_tabla_anidada_datos(
        row_cpt[1],
        '',
        '',
        '',
    )
    
    # Columna 2: Atención Sostenida
    _llenar_tabla_anidada_multiples_indices(
        row_cpt[2],
        '',
        '',
        '',
    )
    
    # Columna 3 y 4: Control ejecutivo
    _llenar_tabla_anidada_datos(
        row_cpt[3],
        '',
        '',
        '',
    )
    
    # Columna 5: Flexibilidad Cognitiva
    _llenar_tabla_anidada_datos(
        row_cpt[5],
        '',
        '',
        '',
    )
    
    # Columna 6: Memoria operativa - Múltiples Índices (PD_directo y PD_inverso)
    _llenar_tabla_anidada_datos(
        row_cpt[6]
        [
            ('PD directo*',
             str(round(resultados.get('PD_DigitsMemorization_directo', 0), 4)),
             str(clasificaciones.get('DigitsMemorization_directo', '-'))),
            ('PD inverso',
             str(round(resultados.get('PD_DigitsMemorization_inverso', 0), 4)),
             str(clasificaciones.get('DigitsMemorization_inverso', '-')))
        ]
    )
    
    # Columna 7: Velocidad de procesamiento
    _llenar_tabla_anidada_datos(
        row_cpt[7],
        '',
        '',
        '',
    )
    
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
