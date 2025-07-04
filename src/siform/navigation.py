"""Модуль для генерации блока навигации."""

from typing import Iterable, Tuple


def build_navigation(items: Iterable[Tuple[str, str]]) -> str:
    """Возвращает HTML со списком ссылок."""
    links = "".join(f'<li><a href="{href}">{text}</a></li>' for text, href in items)
    return f"<ul>{links}</ul>"
