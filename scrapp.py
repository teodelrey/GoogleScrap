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

driver_path = 'D:\\Forks\\GoogleScrap\\chromedriver_win32\\chromedriver.exe'

searchterm = input("¿Que quieres buscar?: ")
searchterm = searchterm.replace(" ", "+")
url = f"https://www.google.es/search?q={searchterm}&sxsrf=ALeKk01yago1e8FHuK6OkdB78U4ZSiyPew%3A1621614800296&ei=0OCnYJvDEcW4lwT76KzYCQ&oq=venom+2&gs_lcp=Cgdnd3Mtd2l6EAMyCAguELEDEJMCMgQILhBDMgUIABCxAzICCAAyAggAMgIIADICCAAyAggAMgIIADICCAA6BwgAEEcQsAM6BwgAELADEEM6DQguELADEMgDEEMQkwI6CgguELADEMgDEEM6DQguELEDEIMBEEMQkwI6BwguELEDEEM6BAgAEEM6CggAELEDEIMBEENKBQg4EgExUIkfWKggYOsiaAFwAngAgAGtAYgBuQOSAQMwLjOYAQCgAQGqAQdnd3Mtd2l6yAEPwAEB&sclient=gws-wiz&ved=0ahUKEwib64jxmdvwAhVF3IUKHXs0C5sQ4dUDCA4&uact=5"

driver = webdriver.Chrome(driver_path, chrome_options=options)

driver.get( url )
r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")
productslist = []
descripciones = []
'''i = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]'''
i = [1,50]
print(i)
results = soup.find_all("div", {"class": "s-item__info clearfix"})
j = [1,2,3,4,5,6]

try:
    WebDriverWait(driver, 5) \
    .until(EC.element_to_be_clickable((By.XPATH,
                                         '/html/body/div[3]/div[3]/span/div/div/div[3]/button[2]/div'))) \
    .click()

except:
    estado == 2

#Analiza la primera pagina
estado = 2

WebDriverWait(driver, 1) \
    .until(EC.element_to_be_clickable((By.CLASS_NAME,
                                'yuRUbf'))) \
    .click()