import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
import random



# Opciones de navegación
options =  webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

driver_path = 'C:\\Users\\Teo\\GoogleScrap\\chromedriver_win32\\chromedriver.exe'

url = "https://motionarray.com/account/login"

driver = webdriver.Chrome(driver_path, chrome_options=options)

driver.get( url )
r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")
'''results = soup.find_all("div", {"class": "s-item__info clearfix"})'''
u = range(1, 30)
moves = [Keys.DOWN,Keys.UP]

#Aceptamos las cookies
WebDriverWait(driver, 5) \
.until(EC.element_to_be_clickable((By.XPATH,
                                     '//*[@id="adroll_reject"]'))) \
.click()

#Nos logueamos y entramos en la web
correo = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div[2]/form/ul/li[1]/input")
correo.send_keys("nitro85@gmail.com")

contraseña = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div[2]/form/ul/li[2]/input")
contraseña.send_keys("XXLxxl123!")

WebDriverWait(driver, 5) \
.until(EC.element_to_be_clickable((By.XPATH,
                                     '//*[@id="site-app"]/div[2]/div[2]/div[2]/form/ul/li[4]/button'))) \
.click()

#Aceptamos cookies y quitamos publicidad
WebDriverWait(driver, 5) \
    .until(EC.element_to_be_clickable((By.XPATH,
                                       '//*[@id="cookiescript_buttons"]'))) \
    .click()

WebDriverWait(driver, 5) \
    .until(EC.element_to_be_clickable((By.XPATH,
                                       '//*[@id="browse"]/div[5]/div/button'))) \
    .click()

#Hacemos click y seleccionamos Davinci templates
WebDriverWait(driver, 1) \
    .until(EC.element_to_be_clickable((By.XPATH,
                                       '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[8]/li/div[1]/div/label'))) \
    .click()

#Seleccionamos Titles


WebDriverWait(driver, 5) \
    .until(EC.element_to_be_clickable((By.XPATH,
                                       '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[8]/li/ul/li[1]/div/label/span[2]'))) \
    .click()
time.sleep(5)
def scrapea9objetos(a, b):

    i = range(a, b)
    for j in i:
        print('He entrado en:')
        print(j)
        WebDriverWait(driver, 4) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '//*[@id="right-column"]/div[1]/div['+str(j)+']/div[2]/h2/a'))) \
            .click()
        time.sleep(4)
        print(j)
        driver.back()

def scrollhaciaabajo():

    for y in u:
        driver.find_element_by_css_selector('body').send_keys(Keys.DOWN)

def funcionalidad():

    while True:
        try:
            scrapea9objetos(1, 10)
            scrollhaciaabajo()
        except:
            print("ROTOOO")
            break
        try:
            scrapea9objetos(10, 19)
            scrollhaciaabajo()
        except:
            print("ROTOOO")
            break
        try:
            scrapea9objetos(19, 28)
            scrollhaciaabajo()
        except:
            print("ROTOOO")
            break
        try:
            scrapea9objetos(28, 37)
            scrollhaciaabajo()
        except:
            print("ROTOOO")
            break
        try:
            scrapea9objetos(37, 46)
            scrollhaciaabajo()
        except:
            print("ROTOOO")
            break
        try:
            scrapea9objetos(46, 55)
            scrollhaciaabajo()
        except:
            print("ROTOOO")
            break
        try:
            scrapea9objetos(55, 61)
        except:
            print("ROTOOO")
            break


def pasarpagina():
    WebDriverWait(driver, 4) \
        .until(EC.element_to_be_clickable((By.XPATH,
                                           '//*[@id="right-column"]/div[2]/ul/li[9]'))) \
        .click()

#scrap de titles

''''
#Pagina1
funcionalidad()
pasarpagina()
print('Ha pasado a la pagina 2')
#Pagina2
funcionalidad()
pasarpagina()
#Pagina3
funcionalidad()
pasarpagina()
#Pagina4
funcionalidad()
pasarpagina()
#Pagina5
funcionalidad()
pasarpagina()
#Pagina6
funcionalidad()
pasarpagina()
#Pagina7
funcionalidad()
pasarpagina()
'''

#Deselecciona Title y selecciona logos
WebDriverWait(driver, 5) \
    .until(EC.element_to_be_clickable((By.XPATH,
                                       '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[8]/li/ul/li[1]/div/label/span[2]'))) \
    .click()

WebDriverWait(driver, 5) \
    .until(EC.element_to_be_clickable((By.XPATH,
                                       '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[8]/li/ul/li[2]/div/label'))) \
    .click()

time.sleep(5)
#Recorremos todas las paginas otra vez descargando de LOGOS
'''
#Pagina1
print('Ha pasado a Logos')
funcionalidad()
pasarpagina()
#Pagina2
funcionalidad()
pasarpagina()
#Pagina3
funcionalidad()
pasarpagina()
#Pagina4
funcionalidad()
pasarpagina()
#Pagina5
funcionalidad()
pasarpagina()
#Pagina6
funcionalidad()
pasarpagina()
'''

#Deselecciona Logos y selecciona Photo/Video
WebDriverWait(driver, 5) \
    .until(EC.element_to_be_clickable((By.XPATH,
                                       '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[8]/li/ul/li[2]/div/label'))) \
    .click()

WebDriverWait(driver, 5) \
    .until(EC.element_to_be_clickable((By.XPATH,
                                       '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[8]/li/ul/li[3]/div/label'))) \
    .click()
time.sleep(5)
#Scrap de Photos/Videos

'''
#Recorremos las paginas
#Pagina1
print('Ha pasado a Photos/Videos')
funcionalidad()
pasarpagina()
#Pagina2
funcionalidad()
pasarpagina()
#Pagina3
funcionalidad()
pasarpagina()
#Pagina4
funcionalidad()
pasarpagina()
'''

#Deselecciona Photo/Video y selecciona Transitions
WebDriverWait(driver, 5) \
    .until(EC.element_to_be_clickable((By.XPATH,
                                       '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[8]/li/ul/li[3]/div/label'))) \
    .click()

WebDriverWait(driver, 5) \
    .until(EC.element_to_be_clickable((By.XPATH,
                                       '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[8]/li/ul/li[4]/div/label'))) \
    .click()
time.sleep(5)

#Scrap de Transitions

'''
#Recorremos las paginas
#Pagina1
print('Ha pasado a Transitions')
funcionalidad()
pasarpagina()
#Pagina2
funcionalidad()
pasarpagina()
'''

#Deselecciona Transitions y selecciona Slideshows
WebDriverWait(driver, 5) \
    .until(EC.element_to_be_clickable((By.XPATH,
                                       '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[8]/li/ul/li[4]/div/label'))) \
    .click()

WebDriverWait(driver, 5) \
    .until(EC.element_to_be_clickable((By.XPATH,
                                       '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[8]/li/ul/li[5]/div/label'))) \
    .click()
time.sleep(5)

#Scrap Slideshow
#Recorremos las paginas

'''
#Pagina1
print('Ha pasado Slideshows')
funcionalidad()
pasarpagina()
#Pagina2
funcionalidad()
pasarpagina()
#Pagina3
funcionalidad()
pasarpagina()
'''

#Deselecciona Slideshows y selecciona Intros
WebDriverWait(driver, 5) \
    .until(EC.element_to_be_clickable((By.XPATH,
                                       '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[8]/li/ul/li[5]/div/label'))) \
    .click()

WebDriverWait(driver, 5) \
    .until(EC.element_to_be_clickable((By.XPATH,
                                       '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[8]/li/ul/li[6]/div/label'))) \
    .click()
time.sleep(5)

#Scrap Intros
#Recorremos las paginas
'''
#Pagina1
print('Ha pasado a Intros')
funcionalidad()
pasarpagina()
#Pagina2
funcionalidad()
pasarpagina()
#Pagina3
funcionalidad()
pasarpagina()
#Pagina4
funcionalidad()
pasarpagina()
#Pagina5
funcionalidad()
pasarpagina()
'''
#Deselecciona Intros y selecciona Luts
WebDriverWait(driver, 5) \
    .until(EC.element_to_be_clickable((By.XPATH,
                                       '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[8]/li/ul/li[6]/div/label'))) \
    .click()

WebDriverWait(driver, 5) \
    .until(EC.element_to_be_clickable((By.XPATH,
                                       '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[8]/li/ul/li[7]/div/label'))) \
    .click()
time.sleep(5)

#Scrap Luts
#Recorremos las paginas
'''
#Pagina1
print('Ha pasado a Luts')
funcionalidad()
pasarpagina()
'''

#Deselecciona Luts y selecciona Effects
WebDriverWait(driver, 5) \
    .until(EC.element_to_be_clickable((By.XPATH,
                                       '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[8]/li/ul/li[7]/div/label'))) \
    .click()

WebDriverWait(driver, 5) \
    .until(EC.element_to_be_clickable((By.XPATH,
                                       '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[8]/li/ul/li[8]/div/label'))) \
    .click()
time.sleep(5)

#Scrap Effects
#Recorremos las paginas
'''
#Pagina1
funcionalidad()
pasarpagina()
print('Ha pasado a Effects')
#Pagina2
funcionalidad()
pasarpagina()
#Pagina3
funcionalidad()
pasarpagina()
#Pagina4
funcionalidad()
pasarpagina()
#Pagina5
funcionalidad()
pasarpagina()
#Pagina6
funcionalidad()
pasarpagina()
#Pagina7
funcionalidad()
pasarpagina()
#Pagina8
funcionalidad()
pasarpagina()
#Pagina9
funcionalidad()
pasarpagina()
#Pagina10
funcionalidad()
pasarpagina()
#Pagina11
funcionalidad()
pasarpagina()
#Pagina12
funcionalidad()
pasarpagina()
#Pagina13
funcionalidad()
pasarpagina()
#Pagina14
funcionalidad()
pasarpagina()
#Pagina15
funcionalidad()
pasarpagina()
#Pagina16
funcionalidad()
pasarpagina()
#Pagina17
funcionalidad()
pasarpagina()
#Pagina18
funcionalidad()
pasarpagina()
#Pagina19
funcionalidad()
pasarpagina()
'''

#Deseleccionamos Effects
WebDriverWait(driver, 5) \
    .until(EC.element_to_be_clickable((By.XPATH,
                                       '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[8]/li/ul/li[8]/div/label'))) \
    .click()
time.sleep(5)

#Deseleccionamos Davinci Templates
WebDriverWait(driver, 1) \
    .until(EC.element_to_be_clickable((By.XPATH,
                                       '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[8]/li/div[1]/div/label'))) \
    .click()

#Seleccionamos Davinci Macros
WebDriverWait(driver, 5) \
    .until(EC.element_to_be_clickable((By.XPATH,
                                       '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[9]/li/div[1]/div/label/span[2]'))) \
    .click()
time.sleep(5)

#Seleccionamos Titles
WebDriverWait(driver, 5) \
    .until(EC.element_to_be_clickable((By.XPATH,
                                       '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[9]/li/ul/li[1]/div/label'))) \
    .click()
time.sleep(5)

#Scrap Title (Macros)
#Recorremos las paginas
'''
#Pagina1
funcionalidad()
pasarpagina()
print('Ha pasado a Effects')
#Pagina2
funcionalidad()
pasarpagina()
#Pagina3
funcionalidad()
pasarpagina()
#Pagina4
funcionalidad()
pasarpagina()
#Pagina5
funcionalidad()
pasarpagina()
#Pagina6
funcionalidad()
pasarpagina()
#Pagina7
funcionalidad()
pasarpagina()
#Pagina8
funcionalidad()
pasarpagina()
#Pagina9
funcionalidad()
pasarpagina()
#Pagina10
funcionalidad()
pasarpagina()
#Pagina11
funcionalidad()
pasarpagina()
#Pagina12
funcionalidad()
pasarpagina()
#Pagina13
funcionalidad()
pasarpagina()
#Pagina14
funcionalidad()
pasarpagina()
#Pagina15
funcionalidad()
pasarpagina()
#Pagina16
funcionalidad()
pasarpagina()
#Pagina17
funcionalidad()
pasarpagina()
#Pagina18
funcionalidad()
pasarpagina()
#Pagina19
funcionalidad()
pasarpagina()
#Pagina20
funcionalidad()
pasarpagina()
#Pagina21
funcionalidad()
pasarpagina()
'''

#Deselecciona Title y selecciona Transitions
WebDriverWait(driver, 5) \
    .until(EC.element_to_be_clickable((By.XPATH,
                                       '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[9]/li/ul/li[1]/div/label'))) \
    .click()

WebDriverWait(driver, 5) \
    .until(EC.element_to_be_clickable((By.XPATH,
                                       '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[9]/li/ul/li[2]/div/label/span[2]'))) \
    .click()
time.sleep(5)

#Scrap Logo (Macros)
#Recorremos las paginas
''''
#Pagina1
funcionalidad()
pasarpagina()
print('Ha pasado a Effects')
#Pagina2
funcionalidad()
pasarpagina()
#Pagina3
funcionalidad()
pasarpagina()
#Pagina4
funcionalidad()
pasarpagina()
#Pagina5
funcionalidad()
pasarpagina()
#Pagina6
funcionalidad()
pasarpagina()
#Pagina7
funcionalidad()
pasarpagina()
#Pagina8
funcionalidad()
pasarpagina()
#Pagina9
funcionalidad()
pasarpagina()
#Pagina10
funcionalidad()
pasarpagina()
#Pagina11
funcionalidad()
pasarpagina()
#Pagina12
funcionalidad()
pasarpagina()
#Pagina13
funcionalidad()
pasarpagina()
#Pagina14
funcionalidad()
pasarpagina()
#Pagina15
funcionalidad()
pasarpagina()
#Pagina16
funcionalidad()
pasarpagina()
#Pagina17
funcionalidad()
pasarpagina()
#Pagina18
funcionalidad()
pasarpagina()
#Pagina19
funcionalidad()
pasarpagina()
#Pagina20
funcionalidad()
pasarpagina()
'''

#Deselecciona Transitions y selecciona Logo
WebDriverWait(driver, 5) \
    .until(EC.element_to_be_clickable((By.XPATH,
                                       '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[9]/li/ul/li[2]/div/label/span[2]'))) \
    .click()

WebDriverWait(driver, 5) \
    .until(EC.element_to_be_clickable((By.XPATH,
                                       '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[9]/li/ul/li[3]/div/label'))) \
    .click()
time.sleep(5)

#Scrap Transitions (Macros)
#Recorremos las paginas
''''
#Pagina1
funcionalidad()
pasarpagina()
print('Ha pasado a Effects')
#Pagina2
funcionalidad()
pasarpagina()
#Pagina3
funcionalidad()
pasarpagina()
#Pagina4
funcionalidad()
pasarpagina()
#Pagina5
funcionalidad()
pasarpagina()
#Pagina6
funcionalidad()
pasarpagina()
#Pagina7
funcionalidad()
pasarpagina()
#Pagina8
funcionalidad()
pasarpagina()
#Pagina9
funcionalidad()
pasarpagina()
#Pagina10
funcionalidad()
pasarpagina()
#Pagina11
funcionalidad()
pasarpagina()
#Pagina12
funcionalidad()
pasarpagina()
#Pagina13
funcionalidad()
pasarpagina()
#Pagina14
funcionalidad()
pasarpagina()
#Pagina15
funcionalidad()
pasarpagina()
#Pagina16
funcionalidad()
pasarpagina()
#Pagina17
funcionalidad()
pasarpagina()
#Pagina18
funcionalidad()
pasarpagina()
#Pagina19
funcionalidad()
pasarpagina()
'''

#Deselecciona Logo y selecciona Backgrounds
WebDriverWait(driver, 5) \
    .until(EC.element_to_be_clickable((By.XPATH,
                                       '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[9]/li/ul/li[3]/div/label'))) \
    .click()

WebDriverWait(driver, 5) \
    .until(EC.element_to_be_clickable((By.XPATH,
                                       '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[9]/li/ul/li[4]/div/label'))) \
    .click()
time.sleep(5)

#Scrap Backgrounds (Macros)
#Recorremos las paginas
''''
#Pagina1
funcionalidad()
pasarpagina()
print('Ha pasado a Effects')
#Pagina2
funcionalidad()
pasarpagina()
#Pagina3
funcionalidad()
pasarpagina()
#Pagina4
funcionalidad()
pasarpagina()
#Pagina5
funcionalidad()
pasarpagina()
#Pagina6
funcionalidad()
pasarpagina()
#Pagina7
funcionalidad()
pasarpagina()
#Pagina8
funcionalidad()
pasarpagina()
#Pagina9
funcionalidad()
pasarpagina()
#Pagina10
funcionalidad()
pasarpagina()
#Pagina11
funcionalidad()
pasarpagina()
#Pagina12
funcionalidad()
pasarpagina()
#Pagina13
funcionalidad()
pasarpagina()
#Pagina14
funcionalidad()
pasarpagina()
#Pagina15
funcionalidad()
pasarpagina()
#Pagina16
funcionalidad()
pasarpagina()
#Pagina17
funcionalidad()
pasarpagina()
#Pagina18
funcionalidad()
pasarpagina()
#Pagina19
funcionalidad()
pasarpagina()
'''

#Deselecciona Backgrounds y selecciona Overlays
WebDriverWait(driver, 5) \
    .until(EC.element_to_be_clickable((By.XPATH,
                                       '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[9]/li/ul/li[4]/div/label'))) \
    .click()

WebDriverWait(driver, 5) \
    .until(EC.element_to_be_clickable((By.XPATH,
                                       '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[9]/li/ul/li[5]/div/label'))) \
    .click()
time.sleep(5)

#Scrap Overlays (Macros)
#Recorremos las paginas
''''
#Pagina1
funcionalidad()
pasarpagina()
print('Ha pasado a Effects')
#Pagina2
funcionalidad()
pasarpagina()
#Pagina3
funcionalidad()
pasarpagina()
#Pagina4
funcionalidad()
pasarpagina()
#Pagina5
funcionalidad()
pasarpagina()
#Pagina6
funcionalidad()
pasarpagina()
#Pagina7
funcionalidad()
pasarpagina()
#Pagina8
funcionalidad()
pasarpagina()
#Pagina9
funcionalidad()
pasarpagina()
#Pagina10
funcionalidad()
pasarpagina()
#Pagina11
funcionalidad()
pasarpagina()
#Pagina12
funcionalidad()
pasarpagina()
#Pagina13
funcionalidad()
pasarpagina()
#Pagina14
funcionalidad()
pasarpagina()
#Pagina15
funcionalidad()
pasarpagina()
#Pagina16
funcionalidad()
pasarpagina()
#Pagina17
funcionalidad()
pasarpagina()
#Pagina18
funcionalidad()
pasarpagina()
#Pagina19
funcionalidad()
pasarpagina()
'''

#Deseleccionar Overlays
WebDriverWait(driver, 5) \
    .until(EC.element_to_be_clickable((By.XPATH,
                                       '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[9]/li/ul/li[5]/div/label'))) \
    .click()
time.sleep(5)

#Deseleccionamos Macros
WebDriverWait(driver, 5) \
    .until(EC.element_to_be_clickable((By.XPATH,
                                       '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[9]/li/div[1]/div/label/span[2]'))) \
    .click()
time.sleep(5)