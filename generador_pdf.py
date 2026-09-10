"""
Módulo para convertir el informe DOCX a PDF.
"""
from __future__ import annotations

import os
from io import BytesIO
from typing import Iterator, List, Tuple

from docx import Document
from docx.document import Document as DocxDocument
from docx.oxml.table import CT_Tbl
from docx.oxml.text.paragraph import CT_P
from docx.table import Table
from docx.text.paragraph import Paragraph
from reportlab.lib.pagesizes import A4
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfgen import canvas

REL_NS = '{http://schemas.openxmlformats.org/officeDocument/2006/relationships}embed'
PAGE_WIDTH, PAGE_HEIGHT = A4
MARGIN = 40
FONT_NAME = 'Helvetica'
FONT_SIZE = 11
LINE_HEIGHT = 16


def _iter_block_items(parent: DocxDocument) -> Iterator[Tuple[str, object]]:
    for child in parent.element.body.iterchildren():
        if isinstance(child, CT_P):
            yield 'paragraph', Paragraph(child, parent)
        elif isinstance(child, CT_Tbl):
            yield 'table', Table(child, parent)


def _extract_docx_content(ruta_docx: str) -> List[Tuple[str, object]]:
    doc = Document(ruta_docx)
    content: List[Tuple[str, object]] = []

    for kind, block in _iter_block_items(doc):
        if kind == 'paragraph':
            text = block.text.strip()
            if text:
                content.append(('text', text))
            for blip in block._p.xpath('.//a:blip'):
                rid = blip.get(REL_NS)
                if rid and rid in doc.part.related_parts:
                    content.append(('image', BytesIO(doc.part.related_parts[rid].blob)))
        else:
            content.append(('text', ''))
            for row in block.rows:
                values = [cell.text.strip().replace('\n', ' | ') for cell in row.cells]
                if any(values):
                    content.append(('text', " || ".join(values)))
    return content


def _wrap_text(text: str, max_width: float) -> List[str]:
    if not text:
        return [""]
    words = text.split()
    lines = [words[0]]
    for word in words[1:]:
        candidate = f"{lines[-1]} {word}"
        if stringWidth(candidate, FONT_NAME, FONT_SIZE) <= max_width:
            lines[-1] = candidate
        else:
            lines.append(word)
    return lines


def generar_pdf_desde_docx(ruta_docx, ruta_pdf=None, verbose=True):
    """
    Genera un PDF estructurado a partir del DOCX ya creado.
    """
    if not os.path.exists(ruta_docx):
        raise FileNotFoundError(f"No se encuentra el archivo: {ruta_docx}")

    if ruta_pdf is None:
        ruta_pdf = os.path.splitext(ruta_docx)[0] + '.pdf'
    output_dir = os.path.dirname(ruta_pdf)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)

    pdf = canvas.Canvas(ruta_pdf, pagesize=A4)
    pdf.setFont(FONT_NAME, FONT_SIZE)
    y = PAGE_HEIGHT - MARGIN
    max_text_width = PAGE_WIDTH - (2 * MARGIN)

    def ensure_space(height_needed: float):
        nonlocal y
        if y - height_needed < MARGIN:
            pdf.showPage()
            pdf.setFont(FONT_NAME, FONT_SIZE)
            y = PAGE_HEIGHT - MARGIN

    for kind, payload in _extract_docx_content(ruta_docx):
        if kind == 'text':
            for line in _wrap_text(str(payload), max_text_width):
                ensure_space(LINE_HEIGHT)
                pdf.drawString(MARGIN, y, line)
                y -= LINE_HEIGHT
            y -= 4
            continue

        image_reader = ImageReader(payload)
        img_width, img_height = image_reader.getSize()
        max_width = PAGE_WIDTH - (2 * MARGIN)
        max_height = PAGE_HEIGHT - (2 * MARGIN)
        scale = min(max_width / img_width, max_height / img_height, 1.0)
        draw_width = img_width * scale
        draw_height = img_height * scale

        ensure_space(draw_height + 8)
        pdf.drawImage(
            image_reader,
            MARGIN,
            y - draw_height,
            width=draw_width,
            height=draw_height,
            preserveAspectRatio=True,
            mask='auto',
        )
        y -= draw_height + 12

    pdf.save()

    if verbose:
        print(f"    PDF generado en: {ruta_pdf}")
    return os.path.exists(ruta_pdf)
