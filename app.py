from bs4 import BeautifulSoup
import requests 

url = 'https://www.mercadolibre.com.ar/c/autos-motos-y-otros#menu=categories'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

results = soup.find_all('img')

imagenes_https = [img['src'] for img in results if img.has_attr('src') and img['src'].startswith('https')]
print(imagenes_https)


