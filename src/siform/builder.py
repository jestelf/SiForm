class SiteBuilder:
    """Простой конструктор статических сайтов."""

    def __init__(self):
        self.pages = []

    def add_page(self, title: str, content: str) -> None:
        """Добавляет страницу в сборку."""
        self.pages.append((title, content))

    def build(self) -> dict:
        """Возвращает структуру сайта в виде словаря {имя_файла: html}."""
        result = {}
        for title, content in self.pages:
            filename = f"{title.lower().replace(' ', '_')}.html"
            html = (
                f"<html><head><title>{title}</title></head>"
                f"<body>{content}</body></html>"
            )
            result[filename] = html
        return result
