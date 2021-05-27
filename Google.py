import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pandas as pd
import datetime
espacio = '   '

titles=[]
prices=[]
link=[]

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

#Hacemos click y seleccionamos Davinci templates





