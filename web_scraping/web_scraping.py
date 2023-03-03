import bs4
import requests

# crear url sin numero de pagina
url_base = 'https://books.toscrape.com/catalogue/page-{}.html'

# Lista de titulos con 4 o 5 estrellas
titulos_rating_alto = []

# Iterar paginas
for paginas in range(1, 51):

    # Crear sopa en cada pagina
    url_pagina = url_base.format(paginas)
    resultado = requests.get(url_pagina)
    sopa = bs4.BeautifulSoup(resultado.text, 'lxml')


    # Seleccionar datos de los libros
    libros = sopa.select('.product_pod')


    # Iterar libros

    for libro in libros:

        # Chequear que tengan 4 o 5 estrellas
        if len(libro.select('.star-rating.Four')) != 0 or len(libro.select('.star-rating.Five')):

            # Guardar titulo en variable
            titulo_libro = libro.select('a')[1]['title']
            
            # Agregar libro a la lista
            titulos_rating_alto.append(titulo_libro)

# Ver libos 4 y 5 estrellas en consola
for t in titulos_rating_alto:
    print(t)