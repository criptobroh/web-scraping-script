import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Obtener la clave de autorización desde las variables de entorno
API_KEY = os.getenv("BUBBLE_API_KEY")

# URL de la página que quieres scrape
url = "https://example.com"

# Hacer una solicitud HTTP GET
response = requests.get(url)

# Comprobar el estado de la solicitud
if response.status_code == 200:
    # Parsear el contenido HTML con BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extraer los textos de <h1> y <p> como listas
    h1_texts = [title.text.strip() for title in soup.find_all('h1')]
    p_texts = [paragraph.text.strip() for paragraph in soup.find_all('p')]

    # Endpoint de Bubble
    bubble_endpoint = "https://nocoda.ai/version-test/api/1.1/wf/python"

    # Datos que enviarás a Bubble
    payload = {
        "h1_list": h1_texts,
        "p_list": p_texts
    }

    # Encabezados para la solicitud, incluyendo la autorización
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }

    # Hacer la solicitud POST al endpoint
    response = requests.post(bubble_endpoint, json=payload, headers=headers)

    # Verificar si la solicitud fue exitosa
    if response.status_code == 200:
        print("Datos enviados correctamente a Bubble.")
    else:
        print(f"Error al enviar datos a Bubble: {response.status_code}")
        print(response.text)

else:
    print(f"Error al acceder a la página: {response.status_code}")
