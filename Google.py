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

WebDriverWait(driver, 3) \
    .until(EC.element_to_be_clickable((By.XPATH,
                                       '/html/body/div[1]/div[2]/div[2]/div[1]/section/div/div[1]/div[2]/div/ul[8]/li/ul/li[1]/div/label/span[2]'))) \
    .click()

def scrapea9objetos(a, b):

    i = range(a, b)
    for j in i:
        print('He entrado en:')
        print(j)
        WebDriverWait(driver, 4) \
            .until(EC.element_to_be_clickable((By.XPATH,
                                               '//*[@id="right-column"]/div[1]/div['+str(j)+']/div[2]/h2/a'))) \
            .click()
        time.sleep(5)
        print(j)
        driver.back()

def scrollhaciaabajo():

    for y in u:
        driver.find_element_by_css_selector('body').send_keys(Keys.DOWN)

while True:
    try:
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
    except:
        print('Se ha roto')