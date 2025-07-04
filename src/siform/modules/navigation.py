class Module:
    """Пример модуля навигации."""

    def apply(self, builder):
        # Добавляем простую страницу навигации
        builder.add_page("Навигация", "<nav>Главная | Галерея</nav>")
