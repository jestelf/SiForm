class Module:
    """Пример модуля галереи изображений."""

    def apply(self, builder):
        # Добавляем страницу галереи
        builder.add_page("Галерея", "<h1>Галерея</h1><img src='image1.jpg'>")
