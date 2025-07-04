class SiteBuilder:
    """Простой конструктор статических сайтов с поддержкой модулей."""

    def __init__(self):
        self.pages = []
        self.modules = []

    # ------------------------------------------------------------------
    # Загрузка модулей
    # ------------------------------------------------------------------
    def load_modules(self, *module_names: str) -> None:
        """Загружает модули по их именам из пакета ``siform.modules``."""

        for name in module_names:
            module = self._import_module(name)
            self.modules.append(module)

    def _import_module(self, name: str):
        module_path = f"siform.modules.{name}"
        mod = __import__(module_path, fromlist=["Module"])
        if not hasattr(mod, "Module"):
            raise ImportError(f"Модуль {name} не содержит класса Module")
        return mod.Module()

    def add_page(self, title: str, content: str) -> None:
        """Добавляет страницу в сборку."""
        self.pages.append((title, content))

    def build(self) -> dict:
        """Возвращает структуру сайта в виде словаря {имя_файла: html}."""
        # Перед сборкой даём модулям возможность изменить билдер
        for module in self.modules:
            if hasattr(module, "apply"):
                module.apply(self)

        result = {}
        for title, content in self.pages:
            filename = f"{title.lower().replace(' ', '_')}.html"
            html = (
                f"<html><head><title>{title}</title></head>"
                f"<body>{content}</body></html>"
            )
            result[filename] = html
        return result
