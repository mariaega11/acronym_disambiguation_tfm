import argparse
import requests

from sys import argv
from bs4 import BeautifulSoup
from math import ceil 


def load_arguments(parser):
    concepto = vars(parser.parse_args(argv[1:]))["c"]
    return concepto


def search(concepto):

    # URL de origen que se 
    url = "https://pubmed.ncbi.nlm.nih.gov/?term={}".format(concepto)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    num_registros = soup.find('div', class_="results-amount").find('span').text.replace(",", "")

    print("Numero de articulos: {}".format(num_registros))

    num_paginas = ceil(int(num_registros)/10)

    #Bucle generando una lista con todos los articulos
    lista_articulos = list()
    for i in range(1,num_paginas+1):
        url_busqueda = url + "&page={}".format(i)
        page = requests.get(url_busqueda)
        soup = BeautifulSoup(page.content, 'html.parser')

        for articulo in soup.find_all('article', class_="full-docsum"):
            lista_articulos.append(articulo.find('a', href=True, class_='docsum-title')['href'])

    #Bucle en el que se mete en cada articulo y obtiene el abstract
    informacion = list()
    for url_articulo in lista_articulos:
        page = requests.get("https://pubmed.ncbi.nlm.nih.gov/" + url_articulo)
        soup = BeautifulSoup(page.content, 'html.parser')

        try:
            informacion.append(soup.find('div', {"id": "enc-abstract"}).text.replace("\n", " "))

        except AttributeError:
            pass

    print("Numero de abstract obtenidos: {} para la palabra: {}".format(len(informacion), conceto))
    return informacion

if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Desarrollo que scrapea con BeautifulSoup la pagina www.savalnet.cl")
    parser.add_argument("-c", help="concepto a buscar")

    concepto = load_arguments(parser)

    search(concepto)

