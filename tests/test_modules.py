from importlib import import_module


def test_navigation_module():
    navigation = import_module('siform.navigation')
    html = navigation.build_navigation([('Главная', '/'), ('О нас', '/about')])
    assert html.startswith('<ul>')
    assert '<a href="/about">' in html


def test_gallery_module():
    gallery = import_module('siform.gallery')
    html = gallery.build_gallery(['img1.png', 'img2.png'])
    assert 'class="gallery"' in html
    assert '<img src="img1.png"' in html
