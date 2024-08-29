from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import requests
from bs4 import BeautifulSoup

# URL inicial
url_inicial = 'https://pangea.orange.es'

# Realizar la solicitud inicial
response = requests.get(url_inicial, allow_redirects=True)

# Captura la URL redirigida
url_redirigida = response.url

# Configurar Selenium con el WebDriver
driver = webdriver.Chrome()  # Asegúrate de que ChromeDriver esté en tu PATH
# Navegar a la página de login
driver.get(url_redirigida)  # Cambia 'https://example.com/login' por la URL real

# Encontrar los campos de entrada del formulario
username_field = driver.find_element(By.ID, 'temp-username')
password_field = driver.find_element(By.ID, 'temp-password')

# Ingresar los datos de login
username_field.send_keys('divemcom')
password_field.send_keys('Junio.2024')

# Ejecutar el formulario de captcha y luego el script submitform()
driver.execute_script("captchaSubmitForm(document.forms['loginData'])")
driver.execute_script("submitform()")

# Esperar la redirección y capturar la URL final
second_url = driver.current_url
print("URL después de la 1era redirección:", second_url)

time.sleep(5)  
cookies = driver.get_cookies()

#####
# SECOND URL
#####

driver.get(second_url)  # Cambia second_url 
# Aplicar las cookies de la primera sesión a la nueva página
for cookie in cookies:
    driver.add_cookie(cookie)

# Refrescar la página después de agregar las cookies
driver.refresh()

time.sleep(5)  # Ajustar según sea necesario

# Encontrar los campos de entrada del formulario
username_field = driver.find_element(By.ID, 'username')
password_field = driver.find_element(By.ID, 'password')

# Ingresar los datos de login
username_field.send_keys('divemcom')
password_field.send_keys('Junio.2024')

# Ejecutar el formulario de captcha y luego el script submitform()
driver.execute_script("submitform()")
time.sleep(5)  

# Esperar la redirección y capturar la URL final
final_url = driver.current_url
print("URL después de la 2da redirección:", final_url)

response = requests.get(final_url, allow_redirects=True)
# Captura la URL redirigida
print(response.text)

time.sleep(10)  

# Imprimir el contenido de la página final
print("driver.page_source")
print("driver.page_source")
print("driver.page_source")

print(driver.page_source)

# Cerrar el navegador
# driver.quit()
