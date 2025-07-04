from siform import SiteBuilder


def test_build_single_page():
    builder = SiteBuilder()
    builder.add_page("Главная", "Привет, мир!")
    result = builder.build()
    assert "главная.html" in result
    assert "Привет, мир!" in result["главная.html"]
