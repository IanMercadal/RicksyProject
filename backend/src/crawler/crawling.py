# import requests

# r = requests.get("https://mateogarciag.github.io/Project-dual-website")
# the_html = r.text


import requests

def get_html_content(url):
    
    #* PRECONDITIONAL
    assert isinstance(url, str) == True
    
    content_page = ''
    mensaje = ''
    
    if url != '':
        
        try:
            
            if '.' in url:
                page = requests.get(url)
            
            else:
                raise requests.exceptions.InvalidURL

        except requests.exceptions.InvalidURL as req:
            mensaje = 'Invalid URL, try another'
            
        except requests.exceptions.MissingSchema as no_http:
            mensaje = f'There\'s no protocol HTTP/s in URL, Invalid URL \'{url}\': No schema supplied. Perhaps you mean: \'https://{url}\''
            
        except requests.exceptions.HTTPError as error_http:
            mensaje = f'There was a HTPP Error'
            
        except requests.exceptions.ConnectionError as con_error:
            mensaje = f'There was a Conection Error'
            
        except Exception as exc:
            mensaje = exc.args
        
        else:
            
            #* POSTCONDITIONAL
            assert page.status_code == 200
            
            content_page = page.text
            
            return content_page

    else:
        return None
    
    return mensaje

#* 
def get_next_target(the_html):

    # assert isinstance(the_html, str)

    start_link = (the_html).find('<a href=')
    if start_link == -1:
        return None, 0
    start_quote = the_html.find('"', start_link)
    end_quote = the_html.find('"', start_quote + 1)
    url = the_html[start_quote + 1:end_quote]
    
    #* POSTCONDITIONAL
    assert isinstance(url, str)
    assert isinstance(end_quote, int)

    return url, end_quote
    
def get_all_links(the_html):
    links = []
    #* PRECONDITIONAL
    assert isinstance(links, list)
    
    while True:
        url, endpos = get_next_target(the_html)
        if url:
            links.append(url)
            the_html = the_html[endpos:]
        else:
            break
    
    #* POSTCONDITIONAL
    assert links is not []
    
    return links

def union(p, q):
    for e in q:
        if e not in p:
            p.append(e)

#* seed: lINK
def crawl_web(seed):
    tocrawl = [seed]            
    crawled = []
    no_menus = ['#','https://mateogarciag.github.io/Project-dual-website/contactos.html', 'https://mateogarciag.github.io/Project-dual-website/compra.html', 'https://mateogarciag.github.io/Project-dual-website/index.html', 'https://mateogarciag.github.io/Project-dual-website', 'https://mateogarciag.github.io/Project-dual-website/calidad.html', 'https://mateogarciag.github.io/Project-dual-website/menu.html']
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled:
            union(tocrawl, get_all_links(get_html_content(page)))
            crawled.append(page)
            
    new_crawled = []
    for link in crawled:
        if link in no_menus:
            continue
        else:
            new_crawled.append(link)
            
    return new_crawled

if __name__ == "__main__":
    pass

# links_index = get_all_links(get_html_content(page))
# htmls = crawl_web('https://mateogarciag.github.io/Project-dual-website/comida1.html')
# print(htmls)

# example_html_string = get_html_content('https://mateogarciag.github.io/Project-dual-website/menu.html')

# first_a = crawl_web('https://mateogarciag.github.io/Project-dual-website')

# print(first_a)

# html_string = get_html_content('https://mateogarciag.github.io/Project-dual-website/menu.html')

# links = get_all_links(html_string)

# print(links)

# r = requests.get("https://mateogarciag.github.io/Project-dual-website")