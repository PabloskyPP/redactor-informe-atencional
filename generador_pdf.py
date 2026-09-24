"""
Módulo para convertir el informe DOCX a PDF.
"""
from __future__ import annotations

import os
import subprocess
import sys
import tempfile
from io import BytesIO
from typing import Iterator, List, Tuple
from urllib.parse import unquote
from xml.sax.saxutils import escape

from PIL import Image
from docx import Document
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx.oxml.table import CT_Tbl
from docx.oxml.text.paragraph import CT_P
from docx.table import Table
from docx.text.paragraph import Paragraph
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.pdfgen import canvas
from reportlab.platypus import Image as RLImage
from reportlab.platypus import Paragraph as RLParagraph
from reportlab.platypus import SimpleDocTemplate, Spacer, Table as RLTable, TableStyle
from pypdf import PdfReader, PdfWriter

REL_NS = '{http://schemas.openxmlformats.org/officeDocument/2006/relationships}embed'


def _normalizar_ruta(ruta):
    """Convierte una ruta posiblemente codificada como URL en ruta Windows."""
    return os.path.abspath(os.path.normpath(unquote(os.fspath(ruta))))


def convertir_docx_a_pdf(ruta_docx, ruta_pdf=None):
    """
    Convierte un archivo Word (.docx) a PDF usando LibreOffice en modo headless
    
    Args:
        ruta_docx: Ruta al archivo .docx de entrada
        ruta_pdf: Ruta opcional para el archivo PDF de salida.
                  Si no se especifica, se generará en la misma ubicación con extensión .pdf
    
    Returns:
        str: Ruta al archivo PDF generado
        
    Raises:
        FileNotFoundError: Si el archivo .docx no existe
        RuntimeError: Si la conversión falla
    """
    ruta_docx = _normalizar_ruta(ruta_docx)

    # Verificar que el archivo .docx existe
    if not os.path.exists(ruta_docx):
        raise FileNotFoundError(f"No se encuentra el archivo: {ruta_docx}")
    
    # Si no se especifica ruta de salida, usar la misma ubicación
    if ruta_pdf is None:
        ruta_pdf = os.path.splitext(ruta_docx)[0] + '.pdf'
    else:
        ruta_pdf = _normalizar_ruta(ruta_pdf)
    
    # Obtener el directorio de salida
    directorio_salida = os.path.dirname(ruta_pdf)
    if not directorio_salida:
        directorio_salida = os.path.dirname(ruta_docx)
    
    # Asegurar que el directorio de salida existe
    os.makedirs(directorio_salida, exist_ok=True)

    try:
        if sys.platform != 'win32':
            print("    La conversión a PDF requiere Microsoft Word en Windows.")
            return False

        try:
            import win32com.client
        except ImportError:
            print("    pywin32 no está instalado. Instala con: pip install pywin32")
            return False

        # Crear instancia de Word
        word = win32com.client.Dispatch('Word.Application')
        word.Visible = False
        doc = None

        # Abrir el documento
        doc = word.Documents.Open(
            ruta_docx,
            ConfirmConversions=False,
            ReadOnly=True,
            AddToRecentFiles=False,
        )

        # Guardar como PDF (formato 17 es PDF)
        doc.SaveAs(ruta_pdf, FileFormat=17)

        return os.path.exists(ruta_pdf)

    except subprocess.TimeoutExpired:
        print("Error: La conversión de DOCX a PDF excedió el tiempo límite")
        return False
    except Exception as e:
        print(f"Error al convertir DOCX a PDF: {e}")
        return False
    finally:
        if 'doc' in locals() and doc is not None:
            try:
                doc.Close(False)
            except Exception:
                pass
        if 'word' in locals():
            try:
                word.Quit()
            except Exception:
                pass



def crear_pdf_desde_imagen(ruta_imagen, ruta_pdf_salida):
    """
    Crea un PDF con una sola página conteniendo la imagen
    
    Args:
        ruta_imagen: Ruta a la imagen PNG
        ruta_pdf_salida: Ruta donde guardar el PDF
        
    Returns:
        bool: True si se creó correctamente, False en caso contrario
    """
    try:
        # Abrir la imagen para obtener sus dimensiones
        img = Image.open(ruta_imagen)
        img_width, img_height = img.size
        
        # Calcular el tamaño de página A4 en puntos (1 punto = 1/72 pulgadas)
        page_width, page_height = A4
        
        # Calcular la escala para ajustar la imagen a la página manteniendo proporción
        # Dejar un pequeño margen
        margen = 20
        escala_ancho = (page_width - 2 * margen) / img_width
        escala_alto = (page_height - 2 * margen) / img_height
        escala = min(escala_ancho, escala_alto)
        
        # Dimensiones finales de la imagen
        final_width = img_width * escala
        final_height = img_height * escala
        
        # Calcular posición para centrar la imagen
        x = (page_width - final_width) / 2
        y = (page_height - final_height) / 2
        
        # Crear el PDF con la imagen
        c = canvas.Canvas(ruta_pdf_salida, pagesize=A4)
        c.drawImage(
            ruta_imagen,
            x, y,
            width=final_width,
            height=final_height,
            preserveAspectRatio=True
        )
        c.showPage()
        c.save()
        
        return True
        
    except Exception as e:
        print(f"Error al crear PDF desde imagen: {e}")
        return False


def insertar_imagen_en_pagina_3(ruta_pdf_original, ruta_imagen, ruta_pdf_salida):
    """
    Inserta una imagen como página 10 en un PDF existente.
    
    El resultado será:
    - Página 1: contenido original
    - Página 2: contenido original
    - Páginas 3-9: contenido original
    - Página 10: imagen grafico_CPT_final
    - Página 11+: resto del contenido original
    
    Args:
        ruta_pdf_original: Ruta al PDF original (generado desde DOCX)
        ruta_imagen: Ruta a la imagen PNG a insertar
        ruta_pdf_salida: Ruta donde guardar el PDF final
        
    Returns:
        bool: True si se insertó correctamente, False en caso contrario
    """
    try:
        # Leer el PDF original
        lector_original = PdfReader(ruta_pdf_original)
        num_paginas = len(lector_original.pages)
        
        # Crear PDF temporal con la imagen
        with tempfile.NamedTemporaryFile(suffix='.pdf', delete=False) as tmp_file:
            pdf_imagen_temp = tmp_file.name
        
        if not crear_pdf_desde_imagen(ruta_imagen, pdf_imagen_temp):
            return False
        
        # Leer el PDF con la imagen
        lector_imagen = PdfReader(pdf_imagen_temp)
        pagina_imagen = lector_imagen.pages[0]
        
        # Crear el PDF de salida
        escritor = PdfWriter()
        
        # Copiar las primeras 9 páginas del PDF original.
        for i in range(min(9, num_paginas)):  # Aquí se cambia inserción pág grafico_CPT
            escritor.add_page(lector_original.pages[i])
        
        # Insertar la página con la imagen (página 10).
        escritor.add_page(pagina_imagen)
        
        # Copiar el resto de las páginas originales (desde la página 10).
        for i in range(9, num_paginas):      # También quí se cambia inserción pág grafico_CPT
            escritor.add_page(lector_original.pages[i])
        
        # Guardar el PDF final
        with open(ruta_pdf_salida, 'wb') as archivo_salida:
            escritor.write(archivo_salida)
        
        # Limpiar archivo temporal
        try:
            os.unlink(pdf_imagen_temp)
        except:
            pass
        
        return True
        
    except Exception as e:
        print(f"Error al insertar imagen CPT en página 10: {e}")
        return False


def generar_pdf_desde_docx(ruta_docx, ruta_pdf=None, verbose=True):
    """
    Función de alto nivel para generar un PDF desde un archivo Word
    
    Args:
        ruta_docx: Ruta al archivo .docx de entrada
        ruta_pdf: Ruta opcional para el archivo PDF de salida
        verbose: Si True, imprime mensajes de progreso
    
    Returns:
        str: Ruta al archivo PDF generado
    """
    try:
        # Resolver ruta de salida
        if ruta_pdf is None:
            ruta_pdf = os.path.splitext(ruta_docx)[0] + '.pdf'

        print("    Convirtiendo DOCX a PDF...")
        if not convertir_docx_a_pdf(ruta_docx, ruta_pdf):
            print("    Error al convertir DOCX a PDF")
            return False

        ruta_docx_normalizada = _normalizar_ruta(ruta_docx)
        directorios_grafico = [
            os.path.dirname(ruta_docx_normalizada),
            os.path.dirname(os.path.dirname(ruta_docx_normalizada)),
            os.path.dirname(os.path.abspath(__file__)),
        ]
        ruta_imagen = next(
            (
                os.path.join(directorio, 'grafico_CPT_final.png')
                for directorio in directorios_grafico
                if os.path.exists(os.path.join(directorio, 'grafico_CPT_final.png'))
            ),
            None,
        )

        if ruta_imagen:
            fd, ruta_pdf_con_imagen = tempfile.mkstemp(suffix='.pdf')
            os.close(fd)
            try:
                if insertar_imagen_en_pagina_3(
                    ruta_pdf, ruta_imagen, ruta_pdf_con_imagen
                ):
                    os.replace(ruta_pdf_con_imagen, ruta_pdf)
                else:
                    print("    Advertencia: no se pudo insertar el gráfico CPT en la página 10")
            finally:
                if os.path.exists(ruta_pdf_con_imagen):
                    os.unlink(ruta_pdf_con_imagen)

        if verbose:
            print(f"    PDF generado en: {ruta_pdf}")
        return ruta_pdf

    except Exception as e:
        if verbose:
            print(f"   X Error al generar PDF: {e}", file=sys.stderr)
        raise