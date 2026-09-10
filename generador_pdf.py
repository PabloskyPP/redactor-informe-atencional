"""
Módulo para convertir el informe DOCX a PDF.
"""
from __future__ import annotations

import os
import textwrap
from typing import List

from docx import Document
from PIL import Image, ImageDraw, ImageFont


def _load_font(size: int):
    for path in [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
    ]:
        if os.path.exists(path):
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()


def _extract_docx_lines(ruta_docx: str) -> List[str]:
    doc = Document(ruta_docx)
    lines: List[str] = []
    for paragraph in doc.paragraphs:
        text = paragraph.text.strip()
        if text:
            lines.append(text)
    for table in doc.tables:
        lines.append("")
        for row in table.rows:
            values = [cell.text.strip().replace('\n', ' | ') for cell in row.cells]
            if any(values):
                lines.append(" || ".join(values))
    return lines
def _render_lines_to_pages(lines: List[str]) -> List[Image.Image]:
    width, height = 1240, 1754
    margin = 80
    line_height = 28
    font = _load_font(18)

    pages: List[Image.Image] = []
    img = Image.new('RGB', (width, height), 'white')
    draw = ImageDraw.Draw(img)
    y = margin

    def _new_page():
        new_img = Image.new('RGB', (width, height), 'white')
        return new_img, ImageDraw.Draw(new_img), margin

    for raw_line in lines:
        wrapped = textwrap.wrap(raw_line, width=95) or [""]
        for line in wrapped:
            if y + line_height > height - margin:
                pages.append(img)
                img, draw, y = _new_page()
            draw.text((margin, y), line, fill='black', font=font)
            y += line_height
        y += 8

    pages.append(img)
    return pages


def generar_pdf_desde_docx(ruta_docx, ruta_pdf=None, verbose=True):
    """
    Genera un PDF básico a partir del DOCX ya creado.
    """
    if not os.path.exists(ruta_docx):
        raise FileNotFoundError(f"No se encuentra el archivo: {ruta_docx}")

    if ruta_pdf is None:
        ruta_pdf = os.path.splitext(ruta_docx)[0] + '.pdf'
    output_dir = os.path.dirname(ruta_pdf)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)

    lines = _extract_docx_lines(ruta_docx)
    pages = _render_lines_to_pages(lines)

    first, rest = pages[0], pages[1:]
    first.save(ruta_pdf, save_all=True, append_images=rest)

    if verbose:
        print(f"    PDF generado en: {ruta_pdf}")
    return os.path.exists(ruta_pdf)
