from siform import SiteBuilder


def test_module_loading():
    builder = SiteBuilder()
    builder.load_modules("navigation", "gallery")
    result = builder.build()
    assert "навигация.html" in result
    assert "галерея.html" in result
