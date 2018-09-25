Bot de login automático en FB con la librería Selenium para Python en Mac
===

## 1. Instalamos el driver de Chrome o Firefox

1.1 Podemos descargar el *Chrome Driver* desde <a href="http://chromedriver.chromium.org/downloads">aquí</a> y lo descomprimimos.

1.2 Movemos el *chromedriver* a */usr/local/bin*

Como alternativa podemos hacer:

```
brew install chromedriver
```

siempre y cuando tengamos instalado el gestor de dependencias *brew*.

**Nota:**

Si nos otros queremos mantener *chromedriver* en nuestra carpeta Documentos o alguna carpeta personal debemos exportar el PATH.

```
export PATH=$PATH:/path/to/chromedriver/folder

```

o podemos pasarle directamente la ruta a nuestra instancia de Chrome desde código.

## 2. Código

```python
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
```

## 3. Ejecutamos periodicamente con un comando BASH

Para ejecutarlo bastara:
	
```
python script.py
```

si queremos que se repita la ejecución cada n segundos:

```
watch -n 60 'python loginSele.py' 
```

Nota: Para mac debemos instalar el comando *watch* bastara un *brew install watch*

## Fuente

* <a href="https://www.seleniumhq.org/">Selenium Official Page</a>

* <a href="https://stackoverflow.com/questions/44870294/selenium-chromedriver-in-relative-path-for-mac-and-python?rq=1">Selenium chromedriver in relative path for mac and python
</a>

* <a href="https://www.kenst.com/2015/03/installing-chromedriver-on-mac-osx/">Installing ChromeDriver on macOS</a>

* <a href="https://www.youtube.com/watch?v=Hw21qZs7xkA">Youtube: Facebook Auto Poster Using Python & Selenium Webdriver</a>



