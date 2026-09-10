"""
Módulo para convertir el informe DOCX a PDF.
"""
from __future__ import annotations

import os
import zipfile
from io import BytesIO
from typing import Iterator, List, Tuple

from docx import Document
from docx.document import Document as DocxDocument
from docx.oxml.table import CT_Tbl
from docx.oxml.text.paragraph import CT_P
from docx.table import Table
from docx.text.paragraph import Paragraph
from PIL import Image, ImageDraw, ImageFont


def _load_font(size: int):
    for path in [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
    ]:
        if os.path.exists(path):
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()


def _iter_block_items(parent: DocxDocument) -> Iterator[Tuple[str, object]]:
    parent_elm = parent.element.body
    for child in parent_elm.iterchildren():
        if isinstance(child, CT_P):
            yield 'paragraph', Paragraph(child, parent)
        elif isinstance(child, CT_Tbl):
            yield 'table', Table(child, parent)


def _extract_docx_images(ruta_docx: str) -> List[Image.Image]:
    images: List[Image.Image] = []
    with zipfile.ZipFile(ruta_docx) as archive:
        media_names = sorted(
            name for name in archive.namelist()
            if name.startswith('word/media/')
        )
        for name in media_names:
            with archive.open(name) as handle:
                images.append(Image.open(BytesIO(handle.read())).convert('RGB'))
    return images


def _extract_docx_content(ruta_docx: str) -> List[Tuple[str, object]]:
    doc = Document(ruta_docx)
    pending_images = iter(_extract_docx_images(ruta_docx))
    content: List[Tuple[str, object]] = []

    for kind, block in _iter_block_items(doc):
        if kind == 'paragraph':
            text = block.text.strip()
            if text:
                content.append(('text', text))
            if 'w:drawing' in block._p.xml:
                try:
                    content.append(('image', next(pending_images)))
                except StopIteration:
                    pass
        else:
            content.append(('text', ''))
            for row in block.rows:
                values = [cell.text.strip().replace('\n', ' | ') for cell in row.cells]
                if any(values):
                    content.append(('text', " || ".join(values)))

    for image in pending_images:
        content.append(('image', image))
    return content


def _wrap_text(draw: ImageDraw.ImageDraw, text: str, font, max_width: int) -> List[str]:
    if not text:
        return [""]

    words = text.split()
    lines: List[str] = []
    current = words[0]

    for word in words[1:]:
        candidate = f"{current} {word}"
        bbox = draw.textbbox((0, 0), candidate, font=font)
        if (bbox[2] - bbox[0]) <= max_width:
            current = candidate
        else:
            lines.append(current)
            current = word
    lines.append(current)
    return lines
def _render_content_to_pages(content: List[Tuple[str, object]]) -> List[Image.Image]:
    width, height = 1240, 1754
    margin = 80
    font = _load_font(18)

    pages: List[Image.Image] = []
    img = Image.new('RGB', (width, height), 'white')
    draw = ImageDraw.Draw(img)
    y = margin
    page_has_content = False

    def _new_page():
        new_img = Image.new('RGB', (width, height), 'white')
        return new_img, ImageDraw.Draw(new_img), margin, False

    max_text_width = width - (2 * margin)

    for kind, payload in content:
        if kind == 'image':
            image = payload.copy()
            image.thumbnail((max_text_width, height - (2 * margin)))
            if page_has_content:
                pages.append(img)
                img, draw, y, page_has_content = _new_page()
            img.paste(image, (margin, y))
            page_has_content = True
            pages.append(img)
            img, draw, y, page_has_content = _new_page()
            continue

        raw_line = str(payload)
        wrapped = _wrap_text(draw, raw_line, font, max_text_width)
        for line in wrapped:
            bbox = draw.textbbox((0, 0), line or "Ag", font=font)
            line_height = (bbox[3] - bbox[1]) + 8
            if y + line_height > height - margin:
                pages.append(img)
                img, draw, y, page_has_content = _new_page()
            draw.text((margin, y), line, fill='black', font=font)
            y += line_height
            page_has_content = True
        y += 4

    if page_has_content or not pages:
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

    content = _extract_docx_content(ruta_docx)
    pages = _render_content_to_pages(content)

    first, rest = pages[0], pages[1:]
    first.save(ruta_pdf, save_all=True, append_images=rest)

    if verbose:
        print(f"    PDF generado en: {ruta_pdf}")
    return os.path.exists(ruta_pdf)
