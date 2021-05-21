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

driver_path = 'C:\\Users\\Teo\\Scrapping1\\chromedriver_win32\\chromedriver.exe'

searchterm = input("Enter the item you want: ")
searchterm = searchterm.replace(" ", "+")
url = f'https://www.ebay.es/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw={searchterm}&_sacat=0'

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

try:
    WebDriverWait(driver, 5) \
    .until(EC.element_to_be_clickable((By.XPATH,
                                         '//*[@id="gdpr-banner-accept"]'))) \
    .click()

except:
    estado == 2

#Analiza la primera pagina
estado = 2
for items in results:
    title = items.find('h3', {'class': "s-item__title"}).text
    price = items.find("span", {"class": "s-item__price"})
    url = items.find('a',href=True)['href']

    estado = 1
    if price is None:
        continue
    titles.append(title)
    prices.append(price.text)
    link.append(url)

for j in i :
    WebDriverWait(driver, 1) \
        .until(EC.element_to_be_clickable((By.XPATH,
                                    '//*[@id="srp-river-results"]/ul/li['+str(j)+']/div/div[2]/a/h3'))) \
        .click()
    titulo = driver.find_element_by_xpath ("/html/body/div[3]/div[3]/div/div/div[2]/div[3]/div[1]/div[1]/h1")
    precio = driver.find_element_by_xpath ("/html/body/div[3]/div[3]/div/div/div[2]/div[3]/div[2]/form/div[2]/table/tbody/tr/td[2]/div[2]/div[2]/span[1]")
    descripcion = driver.find_element_by_xpath ("/html/body/div[3]/div[5]/div[1]/div[6]/div[2]/div")
    descripciones.append({"Titulo": titulo.text, "Precio": precio.text,'URL: ':link, "descripcion": descripcion.text})
    driver.back()

    if j == 50 :
        print(j)
        continue


productslist.append({ "espacio": espacio })

descripciones.append({"espacio": espacio })

# Pasa a la siguiente pagina (2)
if estado == 1:
    print('if')
    WebDriverWait(driver, 1) \
        .until(EC.element_to_be_clickable((By.XPATH,
                                             '//*[@id="srp-river-results"]/ul/div/div[2]/span/span/nav/a[2]'))) \
        .click()


#Analiza la segunda pagina
for items in results:
    title = items.find('h3', {'class': "s-item__title"}).text
    price = items.find("span", {"class": "s-item__price"})
    url = items.find('a',href=True)['href']

    estado = 1
    if price is None:
        continue
    titles.append(title)
    prices.append(price.text)
    link.append(url)

for j in i :
    WebDriverWait(driver, 1) \
        .until(EC.element_to_be_clickable((By.XPATH,
                                    '//*[@id="srp-river-results"]/ul/li['+str(j)+']/div/div[2]/a/h3'))) \
        .click()
    descripcion = driver.find_element_by_xpath ("/html/body/div[3]/div[5]/div[1]/div[6]/div[2]/div")
    descripciones.append({"descripcion": descripcion.text})
    driver.back()

    if j == 50 :
        print(j)
        continue


productslist.append({ "espacio": espacio })
descripciones.append({"espacio": espacio })

# Pasa a la siguiente pagina (3)
if estado == 1:
    print('if')
    WebDriverWait(driver, 5) \
        .until(EC.element_to_be_clickable((By.XPATH,
                                             '//*[@id="srp-river-results"]/ul/div/div[2]/span/span/nav/a[2]'))) \
        .click()

# Analiza la tercera pagina
for items in results:
    title = items.find('h3', {'class': "s-item__title"}).text
    price = items.find("span", {"class": "s-item__price"})
    url = items.find('a',href=True)['href']

    estado = 1
    if price is None:
        continue
    titles.append(title)
    prices.append(price.text)
    link.append(url)

for j in i :
    WebDriverWait(driver, 1) \
        .until(EC.element_to_be_clickable((By.XPATH,
                                    '//*[@id="srp-river-results"]/ul/li['+str(j)+']/div/div[2]/a/h3'))) \
        .click()
    descripcion = driver.find_element_by_xpath ("/html/body/div[3]/div[5]/div[1]/div[6]/div[2]/div")
    descripciones.append({"descripcion": descripcion.text})
    driver.back()

    if j == 50 :
        print(j)
        continue


productslist.append({ "espacio": espacio })
descripciones.append({"espacio": espacio })


df = pd.DataFrame({'Product Name:':titles,'Price: ':prices,'URL: ':link})
ef = pd.DataFrame(descripciones)
print(df)
print(ef)
if
df.to_csv(searchterm + ' Titulos_y_Precios.csv', index=False, encoding='utf-8')
ef.to_csv(searchterm + ' Descripciones.csv', index=False, encoding='utf-8')
print('Saved to CSV')

driver.quit()