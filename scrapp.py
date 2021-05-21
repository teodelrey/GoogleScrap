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
for j in i :
    WebDriverWait(driver, 1) \
        .until(EC.element_to_be_clickable((By.XPATH,
                                    '/html/body/div[7]/div/div[9]/div[1]/div/div[2]/div[2]/div/div/div['+str(j)+']/div/div/div[1]/a/h3'))) \
        .click()

    '''
    titulo = driver.find_element_by_xpath ("/html/body/div[3]/div[3]/div/div/div[2]/div[3]/div[1]/div[1]/h1")
    precio = driver.find_element_by_xpath ("/html/body/div[3]/div[3]/div/div/div[2]/div[3]/div[2]/form/div[2]/table/tbody/tr/td[2]/div[2]/div[2]/span[1]")
    descripcion = driver.find_element_by_xpath ("/html/body/div[3]/div[5]/div[1]/div[6]/div[2]/div")
    descripciones.append({"Titulo": titulo.text, "Precio": precio.text,'URL: ':link, "descripcion": descripcion.text})
    '''
    driver.back()

    if j == 50 :
        print(j)
        continue


df = pd.DataFrame({'Product Name:':titles,'Price: ':prices,'URL: ':link})
ef = pd.DataFrame(descripciones)
print(df)
print(ef)
df.to_csv(searchterm + ' Titulos_y_Precios.csv', index=False, encoding='utf-8')
ef.to_csv(searchterm + ' Descripciones.csv', index=False, encoding='utf-8')
print('Saved to CSV')

driver.quit()