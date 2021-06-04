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

global numero_pagina
global p
p = 1

# Opciones de navegación
options =  webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

driver_path = 'D:\\Forks\\GoogleScrap\\chromedriver_win32\\chromedriver.exe'

url = "https://motionarray.com/account/login"

driver = webdriver.Chrome(driver_path, chrome_options=options)

driver.get(url)
r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")
'''results = soup.find_all("div", {"class": "s-item__info clearfix"})'''
#Numero de scrolls que se desplaza hacia abajo
rango_scroll = range(1, 30)
moves = [Keys.DOWN,Keys.UP]


                                            #Declaración de variables

def scrapea9objetos(a, b):

    i = range(a, b)
    for j in i:
        print('He entrado en:')
        print(j)
        WebDriverWait(driver, 3) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '//*[@id="right-column"]/div[1]/div['+str(j)+']/div[2]/h2/a'))) \
            .click()
        print(j)
        driver.back()

def creartxt():
    file = open(r"D:\\Forks\\GoogleScrap\\Txts\\Datos.txt", "w")
    file.write("1")
    file.close()
    print('He creado el TXT')

def creartxtpagina():
    file = open(r"D:\\Forks\\GoogleScrap\\Txts\\Datospagina.txt", "w")
    file.write("1")
    file.close()
    print('He creado el TXT de la pagina')

def creartxtapartados():
    file = open(r"D:\\Forks\\GoogleScrap\\Txts\\Apartados.txt", "w")
    file.write("1")
    file.close()
    print('He creado el TXT Apartados')

def leertxtapartados():
    global w
    global lectura_apartados
    lectura_apartados = open("Apartados.txt", 'r')
    w = int(lectura_datos.read())

def leertxt():
    global seccion_pagina
    global lectura_datos
    lectura_datos = open("Datos.txt", 'r')
    seccion_pagina = int(lectura_datos.read())

def leer_pagina():
    global lectura_pagina
    global numero_pagina
    lectura_pagina = open("Datospagina.txt", 'r')
    numero_pagina = int(lectura_pagina.read())

def scrollhaciaabajo():

    for y in rango_scroll:
        driver.find_element_by_css_selector('body').send_keys(Keys.DOWN)

def funcionalidad():
    leertxt()
    print('Comenzamos con el numero: ')
    print(seccion_pagina)
    if (seccion_pagina == 1) :
        scrapea9objetos(1, 10)
        scrollhaciaabajo()
        scrapea9objetos(10, 19)
        scrollhaciaabajo()
        file = open(r"D:\\Forks\\GoogleScrap\\Txts\\Datos.txt", "w")
        file.write("2")
        file.close()
        print('He modificado(2) el txt')
    if (seccion_pagina == 2):
        print('Seguimos con el numero:')
        print(seccion_pagina)
        scrollhaciaabajo()
        scrollhaciaabajo()
        scrapea9objetos(19, 28)
        scrollhaciaabajo()
        scrapea9objetos(28, 37)
        scrollhaciaabajo()
        file = open(r"D:\\Forks\\GoogleScrap\\Txts\\Datos.txt", "w")
        file.write("3")
        file.close()
        print('He modificado(3) el txt')
    if seccion_pagina == 3:
        global numero_pagina
        print('Seguimos con el numero:')
        print(seccion_pagina)
        scrollhaciaabajo()
        scrollhaciaabajo()
        scrollhaciaabajo()
        scrollhaciaabajo()
        scrapea9objetos(37, 46)
        scrollhaciaabajo()
        scrapea9objetos(46, 55)
        scrollhaciaabajo()
        scrapea9objetos(55, 61)
        leer_pagina()
        numero_pagina = numero_pagina+1
        file = open(r"D:\\Forks\\GoogleScrap\\Txts\\Datospagina.txt", "w")
        file.write(str(numero_pagina))
        file.close()
        print('He escrito el numero de pagina')
        file = open(r"D:\\Forks\\GoogleScrap\\Txts\\Datos.txt", "w")
        file.write("1")
        file.close()
        print('He modificado(1) el txt')
        pasarpagina()
        print('Se ha ejecutado pasar página')


def pasarpagina():
    global p
    global w
    leer_pagina()
    while p <= numero_pagina:

        WebDriverWait(driver, 10) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '//*[@id="right-column"]/div[2]/ul/li[9]'))) \
            .click()
        p = p+1
        if (p == 7):
            p = 1
            try:
                leertxtapartados()
                print('he leido el txt apartados')
            except:
                creartxtapartados()
                print('he creado el txt apartados')
            w = w+1
            file = open(r"D:\\Forks\\GoogleScrap\\Txts\\Apartados.txt", "w")
            file.write(str(w))
            file.close()
            cambio_apartado()
    print('Siguiente página')
    print('He pasado de pagina')

def cambio_apartado():
    global w
    if w == 2:
        # Deselecciona Title y selecciona logos
        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[8]/li/ul/li[1]/div/label/span[2]'))) \
            .click()

        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[8]/li/ul/li[2]/div/label'))) \
            .click()

        time.sleep(3)
        print('Ha pasado a Logos')

    if w == 3:
        # Deselecciona Logos y selecciona Photo/Video
        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[8]/li/ul/li[2]/div/label'))) \
            .click()

        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[8]/li/ul/li[3]/div/label'))) \
            .click()
        time.sleep(3)
        print('Ha pasado a Photos/Videos')

    if w == 4:
        # Deselecciona Photo/Video y selecciona Transitions
        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[8]/li/ul/li[3]/div/label'))) \
            .click()

        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[8]/li/ul/li[4]/div/label'))) \
            .click()
        time.sleep(3)
        print('Ha pasado a Transitions')

    if w == 5:
        # Deselecciona Transitions y selecciona Slideshows
        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[8]/li/ul/li[4]/div/label'))) \
            .click()

        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[8]/li/ul/li[5]/div/label'))) \
            .click()
        time.sleep(3)
        print('Ha pasado Slideshows')

    if w == 6:
        # Deselecciona Slideshows y selecciona Intros
        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[8]/li/ul/li[5]/div/label'))) \
            .click()

        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[8]/li/ul/li[6]/div/label'))) \
            .click()
        time.sleep(3)
        print('Ha pasado a Intros')

    if w == 7:
        # Deselecciona Intros y selecciona Luts
        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[8]/li/ul/li[6]/div/label'))) \
            .click()

        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[8]/li/ul/li[7]/div/label'))) \
            .click()
        time.sleep(3)
        print('Ha pasado a Luts')

    if w == 8:
        # Deselecciona Luts y selecciona Effects
        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[8]/li/ul/li[7]/div/label'))) \
            .click()

        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[8]/li/ul/li[8]/div/label'))) \
            .click()
        time.sleep(3)
        print('Ha pasado a Effects')

    if w == 9:
        # Deseleccionamos Effects
        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[8]/li/ul/li[8]/div/label'))) \
            .click()
        time.sleep(3)

        # Deseleccionamos Davinci Templates
        WebDriverWait(driver, 1) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[8]/li/div[1]/div/label'))) \
            .click()

    if w == 10:
        # Seleccionamos Davinci Macros
        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[9]/li/div[1]/div/label/span[2]'))) \
            .click()
        time.sleep(3)

        # Seleccionamos Titles
        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[9]/li/ul/li[1]/div/label'))) \
            .click()
        time.sleep(3)
        print('Ha pasado a Titles')

    if w == 11:
        # Deselecciona Title y selecciona Transitions
        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[9]/li/ul/li[1]/div/label'))) \
            .click()

        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[9]/li/ul/li[2]/div/label/span[2]'))) \
            .click()
        time.sleep(3)
        print('Ha pasado a Transitions')

    if w == 12:
        # Deselecciona Transitions y selecciona Logo
        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[9]/li/ul/li[2]/div/label/span[2]'))) \
            .click()

        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[9]/li/ul/li[3]/div/label'))) \
            .click()
        time.sleep(3)
        print('Ha pasado a Logo')

    if w == 13:
        # Deselecciona Logo y selecciona Backgrounds
        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[9]/li/ul/li[3]/div/label'))) \
            .click()

        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[9]/li/ul/li[4]/div/label'))) \
            .click()
        time.sleep(3)
        print('Ha pasado a Backgrounds')

    if w == 14:
        # Deselecciona Backgrounds y selecciona Overlays
        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[9]/li/ul/li[4]/div/label'))) \
            .click()

        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[9]/li/ul/li[5]/div/label'))) \
            .click()
        time.sleep(3)
        print('Ha pasado a Overlays')

    if w == 15:
        # Deseleccionar Overlays
        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[9]/li/ul/li[5]/div/label'))) \
            .click()
        time.sleep(3)

        # Deseleccionamos Macros
        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[9]/li/div[1]/div/label/span[2]'))) \
            .click()
        time.sleep(3)

    if w == 16:
        # Apartado photos
        # Seleccionamos STOCK PHOTOS
        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[10]/li/div[1]/div/label'))) \
            .click()
        time.sleep(3)

        # Seleccionamos ABSTRACT & TEXTURES
        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[10]/li/ul/li[1]/div/label'))) \
            .click()
        time.sleep(3)
        print('Ha pasado a ABSTRACT & TEXTURES')

    if w == 17:
        # Deselecciona ABSTRACT & TEXTURES y selecciona AGRICULTURE
        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[10]/li/ul/li[1]/div/label'))) \
            .click()

        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[10]/li/ul/li[2]/div/label'))) \
            .click()
        time.sleep(3)
        print('Ha pasado a AGRICULTURE')

    if w == 18:
        # Deselecciona AGRICULTURE y selecciona ANIMALS & WILDLIFE
        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[10]/li/ul/li[2]/div/label'))) \
            .click()

        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[10]/li/ul/li[3]/div/label'))) \
            .click()
        time.sleep(3)
        print('Ha pasado a ANIMALS & WILDLIFE')

    if w == 19:
        # Deselecciona ANIMALS & WILDLIFE y selecciona ARCHITECTURE
        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[10]/li/ul/li[3]/div/label'))) \
            .click()

        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[10]/li/ul/li[4]/div/label'))) \
            .click()
        time.sleep(3)
        print('Ha pasado a ARCHITECTURE')

    if w == 20:
        # Deselecciona ARCHITECTURE y selecciona BACKGROUNDS
        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[10]/li/ul/li[4]/div/label'))) \
            .click()

        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[10]/li/ul/li[5]/div/label'))) \
            .click()
        time.sleep(3)
        print('Ha pasado a BACKGROUNDS')

    if w == 21:
        # Deselecciona BACKGROUNDS y selecciona BUSINESS & FINANCE
        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[10]/li/ul/li[5]/div/label'))) \
            .click()

        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[10]/li/ul/li[6]/div/label'))) \
            .click()
        time.sleep(3)
        print('Ha pasado a BUSINESS & FINANCE')

    if w == 22:
        # Deselecciona BUSINESS & FINANCE y selecciona CITY & URBAN
        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[10]/li/ul/li[6]/div/label'))) \
            .click()

        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[10]/li/ul/li[7]/div/label'))) \
            .click()
        time.sleep(3)
        print('Ha pasado a CITY & URBAN')

    if w == 23:
        # Deselecciona CITY & URBAN y selecciona CREATIVITY & DESIGN
        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[10]/li/ul/li[7]/div/label'))) \
            .click()

        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[10]/li/ul/li[8]/div/label'))) \
            .click()
        time.sleep(3)
        print('Ha pasado a CREATIVITY & DESIGN')

    if w == 24:
        # Deselecciona CREATIVITY & DESIGN y selecciona CULTURE
        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[10]/li/ul/li[8]/div/label'))) \
            .click()

        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[10]/li/ul/li[9]/div/label'))) \
            .click()
        time.sleep(3)
        print('Ha pasado a CULTURE')

    if w == 25:
        # Deselecciona CULTURE y selecciona EDUCATION
        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[10]/li/ul/li[9]/div/label'))) \
            .click()

        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[10]/li/ul/li[10]/div/label'))) \
            .click()
        time.sleep(3)
        print('Ha pasado a EDUCATION')

    if w == 26:
        # Deselecciona EDUCATION y selecciona FAMILY
        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[10]/li/ul/li[10]/div/label'))) \
            .click()

        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[10]/li/ul/li[11]/div/label'))) \
            .click()
        time.sleep(3)
        print('Ha pasado a FAMILY')

    if w == 27:
        # Deselecciona FAMILY y selecciona FASHION
        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[10]/li/ul/li[11]/div/label'))) \
            .click()

        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[10]/li/ul/li[12]/div/label'))) \
            .click()
        time.sleep(3)
        print('Ha pasado a FASHION')

    if w == 28:
        # Deselecciona FASHION y selecciona FOOD & DRINK
        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[10]/li/ul/li[12]/div/label'))) \
            .click()

        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[10]/li/ul/li[13]/div/label'))) \
            .click()
        time.sleep(3)
        print('Ha pasado a FOOD & DRINK')

    if w == 29:
        # Deselecciona FOOD & DRINK y selecciona HEALTH & FITNESS
        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[10]/li/ul/li[13]/div/label'))) \
            .click()

        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[10]/li/ul/li[14]/div/label'))) \
            .click()
        time.sleep(3)
        print('Ha pasado a HEALTH & FITNESS')

    if w == 30:
        # Deselecciona HEALTH & FITNESS y selecciona HEALTHCARE
        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[10]/li/ul/li[14]/div/label'))) \
            .click()

        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[10]/li/ul/li[15]/div/label'))) \
            .click()
        time.sleep(3)
        print('Ha pasado a HEALTHCARE')

    if w == 31:
        # Deselecciona HEALTHCARE y selecciona HOLIDAYS & SEASONAL
        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[10]/li/ul/li[15]/div/label'))) \
            .click()

        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[10]/li/ul/li[16]/div/label'))) \
            .click()
        time.sleep(3)
        print('Ha pasado a HOLIDAYS & SEASONAL')

    if w == 32:
        # Deselecciona HOLIDAYS & SEASONAL y selecciona HOME
        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[10]/li/ul/li[16]/div/label'))) \
            .click()

        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[10]/li/ul/li[17]/div/label'))) \
            .click()
        time.sleep(3)
        print('Ha pasado a HOME')

    if w == 33:
        # Deselecciona HOME y selecciona INDUSTRIAL
        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[10]/li/ul/li[17]/div/label'))) \
            .click()

        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[10]/li/ul/li[18]/div/label'))) \
            .click()
        time.sleep(3)
        print('Ha pasado a INDUSTRIAL')

    if w == 34:
        # Deselecciona INDUSTRIAL y selecciona LIFESTYLE
        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[10]/li/ul/li[18]/div/label'))) \
            .click()

        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[10]/li/ul/li[19]/div/label'))) \
            .click()
        time.sleep(3)
        print('Ha pasado a LIFESTYLE')

    if w == 35:
        # Deselecciona LIFESTYLE y selecciona MUSIC
        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[10]/li/ul/li[19]/div/label'))) \
            .click()

        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[10]/li/ul/li[20]/div/label'))) \
            .click()
        time.sleep(3)
        print('Ha pasado a MUSIC')

    if w == 36:
        # Deselecciona MUSIC y selecciona NATURE & OUTDOORS
        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[10]/li/ul/li[20]/div/label'))) \
            .click()

        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[10]/li/ul/li[21]/div/label'))) \
            .click()
        time.sleep(3)
        print('Ha pasado a NATURE & OUTDOORS')

    if w == 37:
        # Deselecciona NATURE & OUTDOORS y selecciona PEOPLE
        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[10]/li/ul/li[21]/div/label'))) \
            .click()

        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[10]/li/ul/li[22]/div/label'))) \
            .click()
        time.sleep(3)
        print('Ha pasado a PEOPLE')

    if w == 38:
        # Deselecciona PEOPLE y selecciona SCIENCE & TECHNOLOGY
        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[10]/li/ul/li[22]/div/label'))) \
            .click()

        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[10]/li/ul/li[23]/div/label'))) \
            .click()
        time.sleep(3)
        print('Ha pasado a SCIENCE & TECHNOLOGY')

    if w == 39:
        # Deselecciona SCIENCE & TECHNOLOGY y selecciona SPORTS & RECREATION
        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[10]/li/ul/li[23]/div/label'))) \
            .click()

        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[10]/li/ul/li[24]/div/label'))) \
            .click()
        time.sleep(3)
        print('Ha pasado a SPORTS & RECREATION')

    if w == 40:
        # Deselecciona SPORTS & RECREATION y selecciona TRANSPORTATION
        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[10]/li/ul/li[24]/div/label'))) \
            .click()

        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[10]/li/ul/li[25]/div/label'))) \
            .click()
        time.sleep(3)
        print('Ha pasado a TRANSPORTATION')

    if w == 41:
        # Deselecciona TRANSPORTATION y selecciona TRAVEL
        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[10]/li/ul/li[25]/div/label'))) \
            .click()

        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[10]/li/ul/li[26]/div/label'))) \
            .click()
        time.sleep(3)
        print('Ha pasado a TRAVEL')

    if w == 42:
        # Deselecciona TRAVEL y selecciona VINTAGE
        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[10]/li/ul/li[26]/div/label'))) \
            .click()

        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[10]/li/ul/li[27]/div/label'))) \
            .click()
        time.sleep(3)
        print('Ha pasado a VINTAGE')

    if w == 43:
        # Deselecciona VINTAGE y selecciona WEDDING
        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[10]/li/ul/li[27]/div/label'))) \
            .click()

        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[10]/li/ul/li[28]/div/label'))) \
            .click()
        time.sleep(3)
        print('Ha pasado a WEDDING')

    if w == 44:
        # Deselecciona WEDDING
        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[10]/li/ul/li[28]/div/label'))) \
            .click()
        print('Desseleccionamos wedding')

        # Deselecciona photos
        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[10]/li/div[1]/div/label'))) \
            .click()
        print('Deseleccionamos photos')

    if w == 45:
        # Apartado videos
        # Seleccionamos Video
        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[13]/li/div[1]/div/label'))) \
            .click()
        time.sleep(3)
        print('Seleccionamos Video')

        # Seleccionamos GREEN SCREEN
        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[13]/li/ul/li[1]/div/label'))) \
            .click()
        time.sleep(3)
        print('Seleccionamos GREEN SCREEN')

    if w == 46:
        # Deselecciona GREEN SCREEN y selecciona TRANSPORTATION
        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[13]/li/ul/li[1]/div/label'))) \
            .click()

        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[13]/li/ul/li[2]/div/label'))) \
            .click()
        time.sleep(3)
        print('Ha pasado a TRANSPORTATION')

    if w == 47:
        # Deselecciona TRANSPORTATION y selecciona BUILDINGS
        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[13]/li/ul/li[2]/div/label'))) \
            .click()

        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[13]/li/ul/li[3]/div/label'))) \
            .click()
        time.sleep(3)
        print('Ha pasado a BUILDINGS')

    if w == 48:
        # Deselecciona BUILDINGS y selecciona TECHNOLOGY
        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[13]/li/ul/li[3]/div/label'))) \
            .click()

        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[13]/li/ul/li[4]/div/label'))) \
            .click()
        time.sleep(3)
        print('Ha pasado a TECHNOLOGY')

    if w == 49:
        # Deselecciona TECHNOLOGY y selecciona PEOPLE
        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[13]/li/ul/li[4]/div/label'))) \
            .click()

        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[13]/li/ul/li[5]/div/label'))) \
            .click()
        time.sleep(3)
        print('Ha pasado a PEOPLE')

    if w == 50:
        # Deselecciona PEOPLE y selecciona HEALTH
        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[13]/li/ul/li[5]/div/label'))) \
            .click()

        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[13]/li/ul/li[6]/div/label'))) \
            .click()
        time.sleep(3)
        print('Ha pasado a HEALTH')

    if w == 51:
        # Deselecciona HEALTH y selecciona FASHION
        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[13]/li/ul/li[6]/div/label'))) \
            .click()

        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[13]/li/ul/li[7]/div/label'))) \
            .click()
        time.sleep(3)
        print('Ha pasado a FASHION')

    if w == 52:
        # Deselecciona FASHION y selecciona ANIMALS
        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[13]/li/ul/li[7]/div/label'))) \
            .click()

        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[13]/li/ul/li[8]/div/label'))) \
            .click()
        time.sleep(3)
        print('Ha pasado a ANIMALS')

    if w == 53:
        # Deselecciona ANIMALS y selecciona FOOD
        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[13]/li/ul/li[8]/div/label'))) \
            .click()

        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[13]/li/ul/li[9]/div/label'))) \
            .click()
        time.sleep(3)
        print('Ha pasado a FOOD')

    if w == 54:
        # Deselecciona FOOD y selecciona SPORTS
        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[13]/li/ul/li[9]/div/label'))) \
            .click()

        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[13]/li/ul/li[10]/div/label'))) \
            .click()
        time.sleep(3)
        print('Ha pasado a SPORTS')

    if w == 55:
        # Deselecciona SPORTS y selecciona NATURE
        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[13]/li/ul/li[10]/div/label'))) \
            .click()

        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[13]/li/ul/li[11]/div/label'))) \
            .click()
        time.sleep(3)
        print('Ha pasado a NATURE')

    if w == 56:
        # Deselecciona NATURE y selecciona AERIAL
        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[13]/li/ul/li[11]/div/label'))) \
            .click()

        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[13]/li/ul/li[12]/div/label'))) \
            .click()
        time.sleep(3)
        print('Ha pasado a AERIAL')

    if w == 57:
        # Deselecciona AERIAL y selecciona HOLIDAYS
        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[13]/li/ul/li[12]/div/label'))) \
            .click()

        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[13]/li/ul/li[13]/div/label'))) \
            .click()
        time.sleep(3)
        print('Ha pasado a HOLIDAYS')

    if w == 58:
        # Deselecciona HOLIDAYS y selecciona INDUSTRIAL
        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[13]/li/ul/li[13]/div/label'))) \
            .click()

        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[13]/li/ul/li[14]/div/label'))) \
            .click()
        time.sleep(3)
        print('Ha pasado a INDUSTRIAL')

    if w == 59:
        # Deselecciona INDUSTRIAL y selecciona HOUSEHOLD
        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[13]/li/ul/li[14]/div/label'))) \
            .click()

        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[13]/li/ul/li[15]/div/label'))) \
            .click()
        time.sleep(3)
        print('Ha pasado a HOUSEHOLD')

    if w == 60:
        # Deselecciona HOUSEHOLD y selecciona SCIENCE
        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[13]/li/ul/li[15]/div/label'))) \
            .click()

        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[13]/li/ul/li[16]/div/label'))) \
            .click()
        time.sleep(3)
        print('Ha pasado a SCIENCE')

    if w == 61:
        # Deselecciona SCIENCE y selecciona EDUCATION
        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[13]/li/ul/li[16]/div/label'))) \
            .click()

        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[13]/li/ul/li[17]/div/label'))) \
            .click()
        time.sleep(3)
        print('Ha pasado a EDUCATION')

    if w == 62:
        # Deselecciona EDUCATION y selecciona TRAVEL
        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[13]/li/ul/li[17]/div/label'))) \
            .click()

        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[13]/li/ul/li[18]/div/label'))) \
            .click()
        time.sleep(3)
        print('Ha pasado a TRAVEL')

    if w == 63:
        # Deselecciona TRAVEL y selecciona BUSINESS
        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[13]/li/ul/li[18]/div/label'))) \
            .click()

        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[13]/li/ul/li[19]/div/label'))) \
            .click()
        time.sleep(3)
        print('Ha pasado a BUSINESS')

    if w == 64:
        # Deselecciona BUSINESS y selecciona INK
        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[13]/li/ul/li[19]/div/label'))) \
            .click()

        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[13]/li/ul/li[20]/div/label'))) \
            .click()
        time.sleep(3)
        print('Ha pasado a INK')

    if w == 65:
        # Deselecciona INK y selecciona FIRE
        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[13]/li/ul/li[20]/div/label'))) \
            .click()

        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[13]/li/ul/li[21]/div/label'))) \
            .click()
        time.sleep(3)
        print('Ha pasado a FIRE')

    if w == 66:
        # Deselecciona FIRE y selecciona DUST
        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[13]/li/ul/li[21]/div/label'))) \
            .click()

        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[13]/li/ul/li[22]/div/label'))) \
            .click()
        time.sleep(3)
        print('Ha pasado a DUST')

    if w == 67:
        # Deselecciona DUST y selecciona PAINT
        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[13]/li/ul/li[22]/div/label'))) \
            .click()

        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[13]/li/ul/li[23]/div/label'))) \
            .click()
        time.sleep(3)
        print('Ha pasado a PAINT')

    if w == 68:
        # Deselecciona PAINT y selecciona SMOKE
        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[13]/li/ul/li[23]/div/label'))) \
            .click()

        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[13]/li/ul/li[24]/div/label'))) \
            .click()
        time.sleep(3)
        print('Ha pasado a SMOKE')

    if w == 69:
        # Deselecciona SMOKE y selecciona SNOW
        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[13]/li/ul/li[24]/div/label'))) \
            .click()

        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[13]/li/ul/li[25]/div/label'))) \
            .click()
        time.sleep(3)
        print('Ha pasado a SNOW')

    if w == 70:
        # Deselecciona SNOW y selecciona CLOUDS
        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[13]/li/ul/li[25]/div/label'))) \
            .click()

        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[13]/li/ul/li[26]/div/label'))) \
            .click()
        time.sleep(3)
        print('Ha pasado a CLOUDS')

    if w == 71:
        # Deselecciona CLOUDS y selecciona PAPER
        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[13]/li/ul/li[26]/div/label'))) \
            .click()

        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[13]/li/ul/li[27]/div/label'))) \
            .click()
        time.sleep(3)
        print('Ha pasado a PAPER')

    if w == 72:
        # Deselecciona PAPER y selecciona LIGHT
        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[13]/li/ul/li[27]/div/label'))) \
            .click()

        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[13]/li/ul/li[28]/div/label'))) \
            .click()
        time.sleep(3)
        print('Ha pasado a LIGHT')

    if w == 73:
        # Deselecciona LIGHT y selecciona SPARKS
        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[13]/li/ul/li[28]/div/label'))) \
            .click()

        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[13]/li/ul/li[29]/div/label'))) \
            .click()
        time.sleep(3)
        print('Ha pasado a SPARKS')

    if w == 74:
        # Deselecciona SPARKS y selecciona WATER
        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[13]/li/ul/li[29]/div/label'))) \
            .click()

        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[13]/li/ul/li[30]/div/label'))) \
            .click()
        time.sleep(3)
        print('Ha pasado a WATER')

    if w == 75:
        # Deselecciona WATER y selecciona OIL
        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[13]/li/ul/li[30]/div/label'))) \
            .click()

        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[13]/li/ul/li[31]/div/label'))) \
            .click()
        time.sleep(3)
        print('Ha pasado a OIL')

    if w == 76:
        # Deselecciona OIL y selecciona PARTICLES
        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[13]/li/ul/li[31]/div/label'))) \
            .click()

        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[13]/li/ul/li[32]/div/label'))) \
            .click()
        time.sleep(3)
        print('Ha pasado a PARTICLES')

    if w == 77:
        # Deselecciona PARTICLES y selecciona OVERLAY
        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[13]/li/ul/li[32]/div/label'))) \
            .click()

        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[13]/li/ul/li[33]/div/label'))) \
            .click()
        time.sleep(3)
        print('Ha pasado a OVERLAY')

    if w == 78:
        # Deselecciona OVERLAY y selecciona BACKGROUND
        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[13]/li/ul/li[33]/div/label'))) \
            .click()

        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[13]/li/ul/li[34]/div/label'))) \
            .click()
        time.sleep(3)
        print('Ha pasado a BACKGROUND')

def pasarpagina2():
    WebDriverWait(driver, 1) \
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
time.sleep(3)
print('Ha pasado a Titles')

#----------------------------------------------------------Ejecucion de funciones---------------------------------------------------------------------------
while True:
    global numero_pagina
    try:
        leertxt()
    except:
        creartxt()
        print('He creado el primer txt')

    try:
        leer_pagina()
    except:
        creartxtpagina()
        print('He creado el segundo txt')
    if numero_pagina == 1:
        funcionalidad()
    else:
        pasarpagina()
        funcionalidad()
        break
#----------------------------------------------------------Ejecucion de funciones---------------------------------------------------------------------------


