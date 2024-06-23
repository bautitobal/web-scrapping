from bs4 import BeautifulSoup
import requests
import re

website = input("Por favor, ingresa la URL a scraping de 'subslikescript.com': ")

result = requests.get(website)
content = result.text

# Parsear el contenido HTML de la página con BeautifulSoup.
soup = BeautifulSoup(content, 'html.parser')

box = soup.find('article', class_='main-article')

if box:
    # Obtenemos el título
    title = box.find('h1').get_text()
    
    transcript = box.find('div', class_="full-script").get_text(strip=True, separator=' ')
    
    # Esto sólo para el testing, dejarlo comentado.
    # print(title)
    # print(transcript[:500]) 

    title_log = title.replace(' - full transcript', '')
    
    filename = re.sub(r'[\\/*?:"<>|]', "", title)
    
    with open(f'{filename}.txt', 'w', encoding='utf-8') as file:
        file.write(transcript)
        print(f'La data sobre "{title_log}" ha sido scrapped correctamente.')
else:
    print("No se pudo encontrar el artículo principal en la página proporcionada.")
