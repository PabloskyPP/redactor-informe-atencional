"""
Módulo para convertir el informe DOCX a PDF.
"""
from __future__ import annotations

import os
from io import BytesIO
from typing import Iterator, List, Tuple
from xml.sax.saxutils import escape

from docx import Document
from docx.document import Document as DocxDocument
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx.oxml.table import CT_Tbl
from docx.oxml.text.paragraph import CT_P
from docx.table import Table
from docx.text.paragraph import Paragraph
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import Image as RLImage
from reportlab.platypus import Paragraph as RLParagraph
from reportlab.platypus import SimpleDocTemplate, Spacer, Table as RLTable, TableStyle

REL_NS = '{http://schemas.openxmlformats.org/officeDocument/2006/relationships}embed'


def _iter_block_items(parent: DocxDocument) -> Iterator[Tuple[str, object]]:
    for child in parent.element.body.iterchildren():
        if isinstance(child, CT_P):
            yield 'paragraph', Paragraph(child, parent)
        elif isinstance(child, CT_Tbl):
            yield 'table', Table(child, parent)


def _paragraph_style(block: Paragraph) -> ParagraphStyle:
    styles = getSampleStyleSheet()
    name = (getattr(block.style, 'name', '') or '').lower()
    alignment = block.alignment

    if 'title' in name:
        style = ParagraphStyle('DocTitle', parent=styles['Title'], alignment=1)
    elif 'heading' in name:
        style = ParagraphStyle('DocHeading', parent=styles['Heading2'])
    else:
        style = ParagraphStyle('DocBody', parent=styles['BodyText'], leading=15)

    if alignment == WD_PARAGRAPH_ALIGNMENT.CENTER:
        style.alignment = 1
    elif alignment == WD_PARAGRAPH_ALIGNMENT.RIGHT:
        style.alignment = 2
    else:
        style.alignment = 0
    return style


def _paragraph_markup(block: Paragraph) -> str:
    parts = []
    for run in block.runs:
        text = escape(run.text).replace('\n', '<br/>')
        if not text:
            continue
        if run.bold and run.italic:
            text = f'<b><i>{text}</i></b>'
        elif run.bold:
            text = f'<b>{text}</b>'
        elif run.italic:
            text = f'<i>{text}</i>'
        parts.append(text)
    return ''.join(parts) or escape(block.text).replace('\n', '<br/>')


def _extract_story(ruta_docx: str):
    doc = Document(ruta_docx)
    story = []

    for kind, block in _iter_block_items(doc):
        if kind == 'paragraph':
            markup = _paragraph_markup(block).strip()
            if markup:
                story.append(RLParagraph(markup, _paragraph_style(block)))
                story.append(Spacer(1, 0.18 * cm))
            for blip in block._p.xpath('.//a:blip'):
                rid = blip.get(REL_NS)
                if rid and rid in doc.part.related_parts:
                    image_part = doc.part.related_parts[rid]
                    image = RLImage(BytesIO(image_part.blob))
                    image._restrictSize(17 * cm, 24 * cm)
                    story.append(image)
                    story.append(Spacer(1, 0.25 * cm))
        else:
            rows = []
            for row in block.rows:
                rows.append([cell.text.strip().replace('\n', '\n') for cell in row.cells])
            if rows:
                table = RLTable(rows, repeatRows=1)
                table.setStyle(TableStyle([
                    ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
                    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                    ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
                    ('FONTSIZE', (0, 0), (-1, -1), 8),
                    ('LEADING', (0, 0), (-1, -1), 10),
                    ('LEFTPADDING', (0, 0), (-1, -1), 4),
                    ('RIGHTPADDING', (0, 0), (-1, -1), 4),
                    ('TOPPADDING', (0, 0), (-1, -1), 3),
                    ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
                ]))
                story.append(table)
                story.append(Spacer(1, 0.25 * cm))
    return story


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

    story = _extract_story(ruta_docx)
    pdf = SimpleDocTemplate(
        ruta_pdf,
        pagesize=A4,
        leftMargin=1.5 * cm,
        rightMargin=1.5 * cm,
        topMargin=1.5 * cm,
        bottomMargin=1.5 * cm,
    )
    pdf.build(story)

    if verbose:
        print(f"    PDF generado en: {ruta_pdf}")
    return os.path.exists(ruta_pdf)
