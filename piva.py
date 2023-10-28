from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import bs4 as bs
import json
import argparse

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import bs4 as bs
import json
import argparse

def trova_dati_PIVA(piva):
    try:
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get('https://www.ufficiocamerale.it/trova-azienda')
        driver.find_element_by_xpath('/html/body/main/div/div/div[2]/form/div[1]/div/input').send_keys(piva)
        time.sleep(5)

        i = []
        while len(i) == 0:
            driver.find_element_by_xpath('/html/body/main/div/div/div[2]/form/p/button').click()
            time.sleep(5)
            html = driver.page_source


            html2 = bs.BeautifulSoup(html, 'html.parser')
            dati = html2.find_all('div', class_='row')[18]
            i = dati.find_all('li', class_='list-group-item')

            estrazione = dict()
            for item in i:
                try:
                    tag = item.text.split(':')[0].strip()
                    value = item.text.split(':')[1].strip().replace('\xa0', ' ').replace('-\nCodice Fiscale', '')
                    estrazione[tag] = value
                except:
                    pass
        
        
        driver.close()
        return json.dumps(estrazione)
    except Exception as e:  
        #driver.close()
        return e
    
argparser = argparse.ArgumentParser()
argparser.add_argument('--piva', help='Partita IVA')
args = argparser.parse_args()
print(trova_dati_PIVA(str(args.piva)))
