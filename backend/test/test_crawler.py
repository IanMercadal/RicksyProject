from src.crawler.crawling import get_next_target, get_all_links, crawl_web
from src.content_page.content_html import get_html_content



def test_get_next_target():
    
    assert get_next_target(get_html_content('https://mateogarciag.github.io/Project-dual-website/menu.html')) == ('https://mateogarciag.github.io/Project-dual-website/index.html', 842)
    assert get_next_target(get_html_content('https://mateogarciag.github.io/Project-dual-website/comida1.html')) == ('https://mateogarciag.github.io/Project-dual-website/index.html', 543)
    assert get_next_target(get_html_content('https://mateogarciag.github.io/Project-dual-website/comida2.html')) == ('https://mateogarciag.github.io/Project-dual-website/index.html', 816)
    assert get_next_target(get_html_content('https://mateogarciag.github.io/Project-dual-website/contactos.html')) == ('https://mateogarciag.github.io/Project-dual-website/index.html', 844)

def test_get_all_links():
    
    assert get_all_links(get_html_content('https://mateogarciag.github.io/Project-dual-website/contactos.html')) == ['https://mateogarciag.github.io/Project-dual-website/index.html', 'https://mateogarciag.github.io/Project-dual-website/menu.html', 'https://mateogarciag.github.io/Project-dual-website/calidad.html', 'https://mateogarciag.github.io/Project-dual-website/contactos.html', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
    
    assert get_all_links(get_html_content('https://mateogarciag.github.io/Project-dual-website/index.html')) == ['https://mateogarciag.github.io/Project-dual-website/index.html', 'https://mateogarciag.github.io/Project-dual-website/menu.html', 'https://mateogarciag.github.io/Project-dual-website/calidad.html', 'https://mateogarciag.github.io/Project-dual-website/contactos.html', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
    
    assert get_all_links(get_html_content('https://mateogarciag.github.io/Project-dual-website/compra.html')) == ['https://mateogarciag.github.io/Project-dual-website/index.html', 'https://mateogarciag.github.io/Project-dual-website/menu.html', 'https://mateogarciag.github.io/Project-dual-website/calidad.html', 'https://mateogarciag.github.io/Project-dual-website/contactos.html', 'https://mateogarciag.github.io/Project-dual-website/index.html', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']

def test_crawl_web():
    
    assert crawl_web('https://mateogarciag.github.io/Project-dual-website') == ['https://mateogarciag.github.io/Project-dual-website/calidad_menu5.html', 'https://mateogarciag.github.io/Project-dual-website/calidad_menu4.html', 'https://mateogarciag.github.io/Project-dual-website/calidad_menu3.html', 'https://mateogarciag.github.io/Project-dual-website/calidad_menu2.html', 'https://mateogarciag.github.io/Project-dual-website/calidad_menu1.html', 'https://mateogarciag.github.io/Project-dual-website/comida9.html', 'https://mateogarciag.github.io/Project-dual-website/comida8.html', 'https://mateogarciag.github.io/Project-dual-website/comida7.html', 'https://mateogarciag.github.io/Project-dual-website/comida6.html', 'https://mateogarciag.github.io/Project-dual-website/comida5.html', 'https://mateogarciag.github.io/Project-dual-website/comida4.html', 'https://mateogarciag.github.io/Project-dual-website/comida3.html', 'https://mateogarciag.github.io/Project-dual-website/comida2.html', 'https://mateogarciag.github.io/Project-dual-website/comida1.html']


##PARA LA FUNCIÓN GET_ALL_LINKS
##1er, en caso de que la lista con links esté vacia.
##2ndo, colocar todos los links directamente en un caso test
##3er, preimer elemento de la lista de los links no esté vacío o sea el que esperemos