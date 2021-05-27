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

url = "https://motionarray.com/davinci-resolve-templates/photo-gallery-family-memories-737938/"

driver = webdriver.Chrome(driver_path, chrome_options=options)

driver.get( url )
r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")
'''results = soup.find_all("div", {"class": "s-item__info clearfix"})'''

WebDriverWait(driver, 5) \
.until(EC.element_to_be_clickable((By.XPATH,
                                     '//*[@id="download-btn-container"]/a'))) \
.click()

WebDriverWait(driver, 5) \
.until(EC.element_to_be_clickable((By.XPATH,
                                     '//*[@id="adroll_reject"]'))) \
.click()