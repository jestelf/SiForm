"""Модуль для генерации простой галереи изображений."""

from typing import Iterable


def build_gallery(images: Iterable[str]) -> str:
    """Возвращает HTML с изображениями."""
    tags = "".join(f'<img src="{src}" />' for src in images)
    return f'<div class="gallery">{tags}</div>'
