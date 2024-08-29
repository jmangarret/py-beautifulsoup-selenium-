import requests
from bs4 import BeautifulSoup

# URL inicial
url_inicial = 'https://pangea.orange.es'

# Realizar la solicitud inicial
response = requests.get(url_inicial, allow_redirects=True)

# Captura la URL redirigida
url_redirigida = response.url
print("URL redirigida:", url_redirigida)

# Obtener el contenido de la página de login
response = requests.get(url_redirigida)
soup = BeautifulSoup(response.content, 'html.parser')

# Encontrar el formulario de login
form = soup.find('form')

# Extraer los campos del formulario
login_data = {
    'username': 'divemcom',
    'password': 'Junio.2024',
    # Añadir otros campos necesarios aquí
}

# Extraer la URL de acción del formulario
login_url = form['action']
if not login_url.startswith('http'):
    login_url = url_redirigida + login_url

# Realizar la solicitud POST para iniciar sesión
response_login = requests.post(login_url, data=login_data, cookies=response.cookies)

# Validar si el status code es 200
if response.status_code == 200:
    print("Solicitud POST exitosa. Status code:", response.status_code)
else:
    print(f"Error en la solicitud POST. Status code: {response.status_code}")

#
# Paso 2: Enviar el formulario al segundo endpoint
#

url_step2 = 'https://applogin.orange.es/oam-custom/pages/login.jsp'

response_step2 = requests.get(url_step2)

# Encontrar el formulario de login
form = soup.find('form')

# Extraer los campos del formulario
login_data = {
    'username': 'divemcom',
    'password': 'Junio.2024',
    # Añadir otros campos necesarios aquí
}

# Extraer la URL de acción del formulario
login_url = form['action']
# Realizar la solicitud POST para iniciar sesión
response_step2 = requests.post(login_url, data=login_data, cookies=response.cookies)

# Validar si el status code es 200
if response_step2.status_code == 200:
    print("Solicitud 2 POST exitosa. Status code:", response_step2.status_code)
else:
    print(f"Error en la solicitud 2 POST. Status code: {response_step2.status_code}")

print("URL final 2 después de la redirección:", response_step2.url)

# Imprimir el contenido del response final
print("Contenido del response final 2:")
print(response_step2.text)
