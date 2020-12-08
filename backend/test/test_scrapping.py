
from src.content_page.content_html import get_html_content
#* FUNTIONS WEB SCRAPPING MODULE IMPORT
# from src.scrapping.scrapping import  get_scrapping_content, find_content, get_all_labels, remove_label, get_content_attribute

#* HTML_STRING: Contiene el string del html de comida1.html para realizar los casos test correctamente
html_string = get_html_content('https://mateogarciag.github.io/Project-dual-website/comida1.html')

def test_get_scrapping_content():
    
    assert get_scrapping_content('') == None
    assert get_scrapping_content(get_html_content('https://mateogarciag.github.io/Project-dual-website/comida1.html')) == {'titulo': ' MENÚ: ', 'descriptionMenu': ' Desde los rincones más profundos del espacio, este menú está hecho de ', 'stock': 30, 'price': 'PRECIO: 10,00', 'ingredients': ['Carne de Marte', 'Lechuga de Jupiter', 'Tomate de Pluton'], 'category': ' Comida Chatarra '}
    # assert get_scrapping_content(get_html_content('https://mateogarciag.github.io/Project-dual-website/comida2.html')) == {
    #     "name": "Alien Burguer",
    #     "price": 10.00,
    #     "stock": 30,
    #     "descriptionMenu": "Desde los rincones más profundos del espacio, este menú está hecho de",
    #     "ingredients": ['Carne de Marte', 'Lechuga de Jupiter', 'Tomate de Pluton'],
    #     "category": 'Comida Chatarra'
    # }
    # assert get_scrapping_content(get_html_content('https://mateogarciag.github.io/Project-dual-website/comida3.html')) == {
    #     "name": "Alien Burguer",
    #     "price": 10.00,
    #     "stock": 30,
    #     "descriptionMenu": "Desde los rincones más profundos del espacio, este menú está hecho de",
    #     "ingredients": ['Carne de Marte', 'Lechuga de Jupiter', 'Tomate de Pluton'],
    #     "category": 'Comida Chatarra'
    # }
    # assert get_scrapping_content(get_html_content('https://mateogarciag.github.io/Project-dual-website/comida4.html')) == {
    #     "name": "Alien Burguer",
    #     "price": 10.00,
    #     "stock": 30,
    #     "descriptionMenu": "Desde los rincones más profundos del espacio, este menú está hecho de",
    #     "ingredients": ['Carne de Marte', 'Lechuga de Jupiter', 'Tomate de Pluton'],
    #     "category": 'Comida Chatarra'
    # }
    


def test_find_content():
    
    assert find_content(html_string, 'input', id_label='stock-menu',attribute='value') == ['30']
    assert find_content(html_string, 'p', class_label='descripcion-menu') == [' Desde los rincones más profundos del espacio, este menú está hecho de ']
    assert find_content(html_string, 'p', class_label='tipo-menu') == [' Comida Chatarra ']
    assert find_content(html_string, 'img', attribute='src') == ['resources/img/calidad/logo.png', 'resources/svg/simbolo_eliminar_44.svg', '../resources/svg/escritoriomenu_icono2.ico', 'resources/img/menu/comida1.png', 'resources/img/social_media/fb.png', 'resources/img/social_media/twitter2.png', 'resources/img/social_media/instagramm.png', 'resources/img/calidad/logo_rickMorty.JPG']
    assert find_content(html_string, 'div', id_label='cancel') == [' <img src="resources/svg/simbolo_eliminar_44.svg" alt=""> ']
    assert find_content(html_string, 'button', class_label='section-calidad-boton') == [' <a href="compra.html">PEDIR</a> ']


def test_get_all_labels():
    
    assert get_all_labels(html_string, 'h3') == ['<h3 class="titulo-menu"> MENÚ: </h3>', '<h3>Lorem Ipsum</h3>']
    assert get_all_labels(html_string, 'img') == ['<img class="logotipo" src="resources/img/calidad/logo.png" alt="">', '<img src="resources/svg/simbolo_eliminar_44.svg" alt="">', '<img src="../resources/svg/escritoriomenu_icono2.ico" alt="">', 
    '<img src="resources/img/menu/comida1.png" alt="">', '<img class="iconos" src="resources/img/social_media/fb.png" alt="">', '<img class="iconos" src="resources/img/social_media/twitter2.png">', '<img class="iconos" src="resources/img/social_media/instagramm.png" alt="">', '<img src="resources/img/calidad/logo_rickMorty.JPG">']
    
    assert get_all_labels(html_string, 'p') == ['<p class="descripcion-menu"> Desde los rincones más profundos del espacio, este menú está hecho de </p>', '<p class="precio"> PRECIO: 10,00$ </p>', '<p class="ingredientes-menu"> Ingredientes: <ul> <li>Carne de Marte</li> <li>Lechuga de Jupiter</li> <li>Tomate de Pluton</li> </ul> </p>', '<p class="tipo-menu"> Comida Chatarra </p>']
    
    assert get_all_labels(html_string, 'a') == ['<a href="index.html" class="titulo"> <img class="logotipo" src="resources/img/calidad/logo.png" alt=""> <h1> JummyFood </h1> </a>', '<a href="menu.html">Menús</a>', '<a href="calidad.html">Calidad</a>', '<a href="contactos.html">Contacto</a>', '<a href="compra.html">PEDIR</a>', '<a href=""> <img class="iconos" src="resources/img/social_media/fb.png" alt=""> </a>', '<a href=""> <img class="iconos" src="resources/img/social_media/twitter2.png"> </a>', '<a href=""> <img class="iconos" src="resources/img/social_media/instagramm.png" alt=""> </a>', '<a href="#" alt="">Políticas de Empresa </a>', '<a href="#" alt="">Derechos de autor </a>', '<a href="#" alt="">Licencia inventada del año 2013 </a>', '<a href="#" alt="">Lorem Lorem Ipsum Ipsum </a>', '<a href="#" alt="">Ipsum ipsum lorem lorem </a>', '<a href="#" alt="">Lorem Ipsum Ipsum Lorem </a>', '<a href="#"> <img src="resources/img/calidad/logo_rickMorty.JPG"> </a>']
    
def test_remove_label():
    
    assert remove_label('<p class="descripcion-menu"> Desde los rincones más profundos del espacio, este menú está hecho de </p>', 'p', class_label='descripcion-menu') == ' Desde los rincones más profundos del espacio, este menú está hecho de '
    assert  remove_label('<h3 class="titulo-menu"> MENÚ: </h3>', 'h3', class_label='titulo-menu') == ' MENÚ: '
    assert remove_label('<li>Tomate de Pluton</li>', 'li') == 'Tomate de Pluton'
    assert remove_label('<img class="logotipo" src="resources/img/calidad/logo.png" alt="">', 'img') == 'This label has not its close label, it\'s one label type'
    assert remove_label('<a href="#"> <img src="resources/img/calidad/logo_rickMorty.JPG"> </a>', 'a') == ' <img src="resources/img/calidad/logo_rickMorty.JPG"> '
    assert remove_label('<h3 class="titulo-menu"> MENÚ: </h3>', 'h3', class_label='cualquier-clase') == 'There is no class or id with that value on this label'
    
def test_get_content_attribute():
    
    assert get_content_attribute('src', '<img class="logotipo" src="resources/img/calidad/logo.png" alt="">') == 'resources/img/calidad/logo.png'
    assert get_content_attribute('value', '<input type="hidden" name="stock-menu" value="30">') == '30'
    assert get_content_attribute('href', '<a href="#" alt="">') == '#'
    assert get_content_attribute('href', '<img class="logotipo" src="resources/img/calidad/logo.png" alt="">') == 'There is no any type of attribute in label/s'
    assert get_content_attribute('', '<img class="logotipo" src="resources/img/calidad/logo.png" alt="">') == 'There is no any type of attribute in label/s'
    