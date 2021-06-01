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

driver_path = 'D:\\Forks\\GoogleScrap\\chromedriver_win32\\chromedriver.exe'

url = "https://motionarray.com/account/login"

driver = webdriver.Chrome(driver_path, chrome_options=options)

driver.get( url )
r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")
'''results = soup.find_all("div", {"class": "s-item__info clearfix"})'''
u = range(1, 30)
moves = [Keys.DOWN,Keys.UP]


                                            #Declaración de variables
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

def pasarpagina2():
    WebDriverWait(driver, 4) \
        .until(EC.element_to_be_clickable((By.XPATH,
                                           '//*[@id="right-column"]/div[2]/ul/li[10]'))) \
        .click()


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
print('Ha pasado a Titles')
'''
#Pagina1
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
print('Ha pasado a Logos')

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
print('Ha pasado a Photos/Videos')

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
print('Ha pasado a Transitions')

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
print('Ha pasado Slideshows')

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
print('Ha pasado a Intros')
#Scrap Intros
#Recorremos las paginas

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
print('Ha pasado a Luts')


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
print('Ha pasado a Effects')


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
print('Ha pasado a Titles')

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
print('Ha pasado a Transitions')

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
print('Ha pasado a Logo')


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
print('Ha pasado a Backgrounds')


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
print('Ha pasado a Overlays')


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

#Seleccionamos STOCK PHOTOS
WebDriverWait(driver, 5) \
    .until(EC.element_to_be_clickable((By.XPATH,
                                       '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[10]/li/div[1]/div/label'))) \
    .click()
time.sleep(5)

#Seleccionamos ABSTRACT & TEXTURES
WebDriverWait(driver, 5) \
    .until(EC.element_to_be_clickable((By.XPATH,
                                       '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[10]/li/ul/li[1]/div/label'))) \
    .click()
time.sleep(5)

print('Ha pasado a ABSTRACT & TEXTURES')

#Deselecciona ABSTRACT & TEXTURES y selecciona AGRICULTURE
WebDriverWait(driver, 5) \
    .until(EC.element_to_be_clickable((By.XPATH,
                                       '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[10]/li/ul/li[1]/div/label'))) \
    .click()

WebDriverWait(driver, 5) \
    .until(EC.element_to_be_clickable((By.XPATH,
                                       '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[10]/li/ul/li[2]/div/label'))) \
    .click()
time.sleep(5)

print('Ha pasado a AGRICULTURE')

#Deselecciona AGRICULTURE y selecciona ANIMALS & WILDLIFE
WebDriverWait(driver, 5) \
    .until(EC.element_to_be_clickable((By.XPATH,
                                       '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[10]/li/ul/li[2]/div/label'))) \
    .click()

WebDriverWait(driver, 5) \
    .until(EC.element_to_be_clickable((By.XPATH,
                                       '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[10]/li/ul/li[3]/div/label'))) \
    .click()
time.sleep(5)

print('Ha pasado a ANIMALS & WILDLIFE')

#Deselecciona ANIMALS & WILDLIFE y selecciona ARCHITECTURE
WebDriverWait(driver, 5) \
    .until(EC.element_to_be_clickable((By.XPATH,
                                       '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[10]/li/ul/li[3]/div/label'))) \
    .click()

WebDriverWait(driver, 5) \
    .until(EC.element_to_be_clickable((By.XPATH,
                                       '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[10]/li/ul/li[4]/div/label'))) \
    .click()
time.sleep(5)

print('Ha pasado a ARCHITECTURE')

#Deselecciona ARCHITECTURE y selecciona BACKGROUNDS
WebDriverWait(driver, 5) \
    .until(EC.element_to_be_clickable((By.XPATH,
                                       '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[10]/li/ul/li[4]/div/label'))) \
    .click()

WebDriverWait(driver, 5) \
    .until(EC.element_to_be_clickable((By.XPATH,
                                       '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[10]/li/ul/li[5]/div/label'))) \
    .click()
time.sleep(5)

print('Ha pasado a BACKGROUNDS')

#Deselecciona BACKGROUNDS y selecciona BUSINESS & FINANCE
WebDriverWait(driver, 5) \
    .until(EC.element_to_be_clickable((By.XPATH,
                                       '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[10]/li/ul/li[5]/div/label'))) \
    .click()

WebDriverWait(driver, 5) \
    .until(EC.element_to_be_clickable((By.XPATH,
                                       '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[10]/li/ul/li[6]/div/label'))) \
    .click()
time.sleep(5)

print('Ha pasado a BUSINESS & FINANCE')

#Deselecciona BUSINESS & FINANCE y selecciona CITY & URBAN
WebDriverWait(driver, 5) \
    .until(EC.element_to_be_clickable((By.XPATH,
                                       '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[10]/li/ul/li[6]/div/label'))) \
    .click()

WebDriverWait(driver, 5) \
    .until(EC.element_to_be_clickable((By.XPATH,
                                       '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[10]/li/ul/li[7]/div/label'))) \
    .click()
time.sleep(5)

print('Ha pasado a CITY & URBAN')

#Deselecciona CITY & URBAN y selecciona CREATIVITY & DESIGN
WebDriverWait(driver, 5) \
    .until(EC.element_to_be_clickable((By.XPATH,
                                       '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[10]/li/ul/li[7]/div/label'))) \
    .click()

WebDriverWait(driver, 5) \
    .until(EC.element_to_be_clickable((By.XPATH,
                                       '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[10]/li/ul/li[8]/div/label'))) \
    .click()
time.sleep(5)

print('Ha pasado a CREATIVITY & DESIGN')

#Deselecciona CREATIVITY & DESIGN y selecciona CULTURE
WebDriverWait(driver, 5) \
    .until(EC.element_to_be_clickable((By.XPATH,
                                       '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[10]/li/ul/li[8]/div/label'))) \
    .click()

WebDriverWait(driver, 5) \
    .until(EC.element_to_be_clickable((By.XPATH,
                                       '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[10]/li/ul/li[9]/div/label'))) \
    .click()
time.sleep(5)

print('Ha pasado a CULTURE')

#Deselecciona CULTURE y selecciona EDUCATION
WebDriverWait(driver, 5) \
    .until(EC.element_to_be_clickable((By.XPATH,
                                       '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[10]/li/ul/li[9]/div/label'))) \
    .click()

WebDriverWait(driver, 5) \
    .until(EC.element_to_be_clickable((By.XPATH,
                                       '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[10]/li/ul/li[10]/div/label'))) \
    .click()
time.sleep(5)

print('Ha pasado a EDUCATION')

#Deselecciona EDUCATION y selecciona FAMILY
WebDriverWait(driver, 5) \
    .until(EC.element_to_be_clickable((By.XPATH,
                                       '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[10]/li/ul/li[10]/div/label'))) \
    .click()

WebDriverWait(driver, 5) \
    .until(EC.element_to_be_clickable((By.XPATH,
                                       '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[10]/li/ul/li[11]/div/label'))) \
    .click()
time.sleep(5)

print('Ha pasado a FAMILY')

#Deselecciona FAMILY y selecciona FASHION
WebDriverWait(driver, 5) \
    .until(EC.element_to_be_clickable((By.XPATH,
                                       '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[10]/li/ul/li[11]/div/label'))) \
    .click()

WebDriverWait(driver, 5) \
    .until(EC.element_to_be_clickable((By.XPATH,
                                       '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[10]/li/ul/li[12]/div/label'))) \
    .click()
time.sleep(5)

print('Ha pasado a FASHION')

#Deselecciona FASHION y selecciona FOOD & DRINK
WebDriverWait(driver, 5) \
    .until(EC.element_to_be_clickable((By.XPATH,
                                       '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[10]/li/ul/li[12]/div/label'))) \
    .click()

WebDriverWait(driver, 5) \
    .until(EC.element_to_be_clickable((By.XPATH,
                                       '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[10]/li/ul/li[13]/div/label'))) \
    .click()
time.sleep(5)

print('Ha pasado a FOOD & DRINK')

#Deselecciona FOOD & DRINK y selecciona HEALTH & FITNESS
WebDriverWait(driver, 5) \
    .until(EC.element_to_be_clickable((By.XPATH,
                                       '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[10]/li/ul/li[13]/div/label'))) \
    .click()

WebDriverWait(driver, 5) \
    .until(EC.element_to_be_clickable((By.XPATH,
                                       '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[10]/li/ul/li[14]/div/label'))) \
    .click()
time.sleep(5)

print('Ha pasado a HEALTH & FITNESS')

#Deselecciona HEALTH & FITNESS y selecciona HEALTHCARE
WebDriverWait(driver, 5) \
    .until(EC.element_to_be_clickable((By.XPATH,
                                       '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[10]/li/ul/li[14]/div/label'))) \
    .click()

WebDriverWait(driver, 5) \
    .until(EC.element_to_be_clickable((By.XPATH,
                                       '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[10]/li/ul/li[15]/div/label'))) \
    .click()
time.sleep(5)

print('Ha pasado a HEALTHCARE')

#Deselecciona HEALTHCARE y selecciona HOLIDAYS & SEASONAL
WebDriverWait(driver, 5) \
    .until(EC.element_to_be_clickable((By.XPATH,
                                       '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[10]/li/ul/li[15]/div/label'))) \
    .click()

WebDriverWait(driver, 5) \
    .until(EC.element_to_be_clickable((By.XPATH,
                                       '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[10]/li/ul/li[16]/div/label'))) \
    .click()
time.sleep(5)

print('Ha pasado a HOLIDAYS & SEASONAL')

#Deselecciona HOLIDAYS & SEASONAL y selecciona HOME
WebDriverWait(driver, 5) \
    .until(EC.element_to_be_clickable((By.XPATH,
                                       '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[10]/li/ul/li[16]/div/label'))) \
    .click()

WebDriverWait(driver, 5) \
    .until(EC.element_to_be_clickable((By.XPATH,
                                       '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[10]/li/ul/li[17]/div/label'))) \
    .click()
time.sleep(5)

print('Ha pasado a HOME')

#Deselecciona HOME y selecciona INDUSTRIAL
WebDriverWait(driver, 5) \
    .until(EC.element_to_be_clickable((By.XPATH,
                                       '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[10]/li/ul/li[17]/div/label'))) \
    .click()

WebDriverWait(driver, 5) \
    .until(EC.element_to_be_clickable((By.XPATH,
                                       '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[10]/li/ul/li[18]/div/label'))) \
    .click()
time.sleep(5)

print('Ha pasado a INDUSTRIAL')

#Deselecciona INDUSTRIAL y selecciona LIFESTYLE
WebDriverWait(driver, 5) \
    .until(EC.element_to_be_clickable((By.XPATH,
                                       '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[10]/li/ul/li[18]/div/label'))) \
    .click()

WebDriverWait(driver, 5) \
    .until(EC.element_to_be_clickable((By.XPATH,
                                       '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[10]/li/ul/li[19]/div/label'))) \
    .click()
time.sleep(5)

print('Ha pasado a LIFESTYLE')

#Deselecciona LIFESTYLE y selecciona MUSIC
WebDriverWait(driver, 5) \
    .until(EC.element_to_be_clickable((By.XPATH,
                                       '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[10]/li/ul/li[19]/div/label'))) \
    .click()

WebDriverWait(driver, 5) \
    .until(EC.element_to_be_clickable((By.XPATH,
                                       '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[10]/li/ul/li[20]/div/label'))) \
    .click()
time.sleep(5)

print('Ha pasado a MUSIC')

#Deselecciona MUSIC y selecciona NATURE & OUTDOORS
WebDriverWait(driver, 5) \
    .until(EC.element_to_be_clickable((By.XPATH,
                                       '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[10]/li/ul/li[20]/div/label'))) \
    .click()

WebDriverWait(driver, 5) \
    .until(EC.element_to_be_clickable((By.XPATH,
                                       '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[10]/li/ul/li[21]/div/label'))) \
    .click()
time.sleep(5)

print('Ha pasado a NATURE & OUTDOORS')

#Deselecciona NATURE & OUTDOORS y selecciona PEOPLE
WebDriverWait(driver, 5) \
    .until(EC.element_to_be_clickable((By.XPATH,
                                       '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[10]/li/ul/li[21]/div/label'))) \
    .click()

WebDriverWait(driver, 5) \
    .until(EC.element_to_be_clickable((By.XPATH,
                                       '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[10]/li/ul/li[22]/div/label'))) \
    .click()
time.sleep(5)

print('Ha pasado a PEOPLE')

#Deselecciona PEOPLE y selecciona SCIENCE & TECHNOLOGY
WebDriverWait(driver, 5) \
    .until(EC.element_to_be_clickable((By.XPATH,
                                       '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[10]/li/ul/li[22]/div/label'))) \
    .click()

WebDriverWait(driver, 5) \
    .until(EC.element_to_be_clickable((By.XPATH,
                                       '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[10]/li/ul/li[23]/div/label'))) \
    .click()
time.sleep(5)

print('Ha pasado a SCIENCE & TECHNOLOGY')

#Deselecciona SCIENCE & TECHNOLOGY y selecciona SPORTS & RECREATION
WebDriverWait(driver, 5) \
    .until(EC.element_to_be_clickable((By.XPATH,
                                       '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[10]/li/ul/li[23]/div/label'))) \
    .click()

WebDriverWait(driver, 5) \
    .until(EC.element_to_be_clickable((By.XPATH,
                                       '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[10]/li/ul/li[24]/div/label'))) \
    .click()
time.sleep(5)

print('Ha pasado a SPORTS & RECREATION')

#Deselecciona SPORTS & RECREATION y selecciona TRANSPORTATION
WebDriverWait(driver, 5) \
    .until(EC.element_to_be_clickable((By.XPATH,
                                       '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[10]/li/ul/li[24]/div/label'))) \
    .click()

WebDriverWait(driver, 5) \
    .until(EC.element_to_be_clickable((By.XPATH,
                                       '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[10]/li/ul/li[25]/div/label'))) \
    .click()
time.sleep(5)

print('Ha pasado a TRANSPORTATION')

#Deselecciona TRANSPORTATION y selecciona TRAVEL
WebDriverWait(driver, 5) \
    .until(EC.element_to_be_clickable((By.XPATH,
                                       '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[10]/li/ul/li[25]/div/label'))) \
    .click()

WebDriverWait(driver, 5) \
    .until(EC.element_to_be_clickable((By.XPATH,
                                       '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[10]/li/ul/li[26]/div/label'))) \
    .click()
time.sleep(5)

print('Ha pasado a TRAVEL')

#Deselecciona TRAVEL y selecciona VINTAGE
WebDriverWait(driver, 5) \
    .until(EC.element_to_be_clickable((By.XPATH,
                                       '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[10]/li/ul/li[26]/div/label'))) \
    .click()

WebDriverWait(driver, 5) \
    .until(EC.element_to_be_clickable((By.XPATH,
                                       '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[10]/li/ul/li[27]/div/label'))) \
    .click()
time.sleep(5)

print('Ha pasado a VINTAGE')

#Deselecciona VINTAGE y selecciona WEDDING
WebDriverWait(driver, 5) \
    .until(EC.element_to_be_clickable((By.XPATH,
                                       '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[10]/li/ul/li[27]/div/label'))) \
    .click()

WebDriverWait(driver, 5) \
    .until(EC.element_to_be_clickable((By.XPATH,
                                       '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[10]/li/ul/li[28]/div/label'))) \
    .click()
time.sleep(5)

print('Ha pasado a WEDDING')