"""Пакет siform предоставляет инструменты для генерации статических сайтов."""

from .builder import SiteBuilder
from .navigation import build_navigation
from .gallery import build_gallery

__all__ = ["SiteBuilder", "build_navigation", "build_gallery"]
