from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import datetime

## Desactivamos mensaje activar notifiaciones
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(chrome_options=chrome_options)

## Accedemos a Facebook
#driver.get('https://www.facebook.com/login.php?login_attempt=1&lwv=110')
driver.get('https://www.facebook.com/')

## Ingresamos Usuario
emailelement = driver.find_element(By.XPATH, './/*[@id="email"]')
emailelement.send_keys('ingresa_tu_usuario_aqui')

## Ingresamos la contraasena
passelement = driver.find_element(By.XPATH, './/*[@id="pass"]')
passelement.send_keys('ingresa_tu_contrasena_aqui')

## Hacemos Login
element = driver.find_element(By.XPATH, './/*[@id="loginbutton"]')
element.click()

## Escribimos un mensaje
status = driver.find_element(By.XPATH, "//*[@name='xhpc_message']")
time.sleep(5)
hora_l = "Ahora son las: "+str(datetime.datetime.now())
status.send_keys(hora_l)
time.sleep(5)

## Publicamos el mensaje
buttons = driver.find_elements_by_tag_name('button')
time.sleep(5)
for button in buttons:
	if button.text == 'Compartir':
		button.click()