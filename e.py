import requests
from bs4 import BeautifulSoup
import os

# URL que utilizamos para obtener las imagenes
url = "https://www.mercadolibre.com.ar/c/autos-motos-y-otros#menu=categories"

def obtener_imagenes_https(url):
    # Realizar la solicitud HTTP
    response = requests.get(url)
    
    # Verificar si la solicitud fue exitosa
    if response.status_code == 200:
        # Crear un directorio para guardar las imágenes
        if not os.path.exists('imagenes'):
            os.makedirs('imagenes')
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        imagenes = soup.find_all('img')
        
        imagenes_https = [img['src'] for img in imagenes if img.has_attr('src') and img['src'].startswith('https')]
        
        # Descargar las imágenes
        for i, img_url in enumerate(imagenes_https):
            img_response = requests.get(img_url)
            if img_response.status_code == 200:
                with open(f'imagenes/imagen_{i}.jpg', 'wb') as f:
                    f.write(img_response.content)
                print(f"Imagen {i} descargada con éxito")
            else:
                print(f"Error al descargar la imagen {i}: {img_response.status_code}")
        
        return imagenes_https
    else:
        # Si la solicitud no fue exitosa, imprimir el mensaje de error
        print("Error al obtener la página:", response.status_code)
        return []

imagenes_https = obtener_imagenes_https(url)
print(imagenes_https)
