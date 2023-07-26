import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import requests

def get_text(url):
    
    articles = []
    response = requests.get(url)
    html_content = response.text

    soup = BeautifulSoup(html_content, 'html.parser')
    articulo = soup.get_text()
    articles.append({'url': url, 'text': articulo})
    return articles

# Path
archivo = "abremes_url.txt"

# Read lines and store them in a list
with open(archivo, 'r') as file:
    urls = file.readlines()

urls = [linea.strip() for linea in urls]

textos = []
for a in urls[57:]:
    try:
        articulos = get_text(a)
        textos += articulos
    except AttributeError:
        print('Fallo en la petición', a)
        continue
    except requests.exceptions.Timeout:
        # Manejar el error de time-out
        print(f"Time-out en la solicitud a {url}. Continuando con la siguiente URL.")
        continue
    except requests.exceptions.TooManyRedirects as e:
        print(f"Error de redireccionamiento: {e}")
        continue
    except requests.exceptions.RequestException as e:
        print(f"Error de solicitud: {e}")
        continue
        
scrap = pd.DataFrame(textos)
scrap.to_csv("../data/abremes_texts_scrapping.csv")