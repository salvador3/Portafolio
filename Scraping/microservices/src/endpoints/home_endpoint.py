from flask import Blueprint, request
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.action_chains import ActionChains

api_home = Blueprint('home',__name__,)

@api_home.route('/home',  methods=['GET'])

def Home():
    try:
        return {"status": "OK", "message": "hello "}
    except Exception as inst:
        return {"status": "Failed to home", "Error": inst}
    


@api_home.route('/supermecado',  methods=['POST'])
def Supermecado():
    try:

        data = request.get_json(force=True)
        url=data['url'] 
        print('url',url)
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_prefs = {}
        chrome_options.experimental_options["prefs"] = chrome_prefs
        chrome_prefs["profile.default_content_settings"] = {"images": 2}
        
        driver = webdriver.Chrome(options=chrome_options)

        # Navegar a una página web
        driver.get(url)
        
        time.sleep(3)
        print("driver",driver.title)
       
        element = driver.find_element(By.XPATH, '//*[@id="gallery-layout-container"]')
        
        # print(element)

        enlaces = element.find_elements(By.TAG_NAME, 'span')
        # Imprimir los textos y URLs de los enlaces
        l_nombre=[]
        for enlace in enlaces:
            texto=enlace.text
            if len(texto)>3 and not '$' in texto and not '%' in texto:
                if not 'Precio Ahora' in texto and not 'Precio Regular' in texto and not 'Ahorra' in texto: 
                    l_nombre.append(texto)
                    
        l_producto=[]
        l_marca=[]
        for i in range(len(l_nombre)):
            if i % 2 == 0:
                l_producto.append(l_nombre[i])
            else:
                l_marca.append(l_nombre[i])
        
        enlaces_precios = element.find_elements(By.ID, 'items-price')
        # print(enlaces_precios)
        l_precios=[]
        for enlace_i in enlaces_precios:
            # enlaces_precios_aux = enlace_i.find_elements(By.CLASS_NAME, 'class="tiendasjumboqaio-jumbo-minicart-2-x-cencoListLabel"')
            class_list = enlace_i.get_attribute('class').split()
            # print("class_list",class_list)
            
            if 'c-emphasis' in class_list:
                enlaces_precios_aux = enlace_i.find_element(By.CLASS_NAME, 'tiendasjumboqaio-jumbo-minicart-2-x-price')
                # print(enlaces_precios_aux.text)
                l_precios.append(enlaces_precios_aux.text)
        
        list_prod=[]
        print(len(l_precios),len(l_producto))
        for i in range(len(l_precios)):
            producto={"name":l_producto[i],
                      "precio":l_precios[i]}
            list_prod.append(producto)

        salida_json={"url":url,
                     "products":list_prod,
                     "title":driver.title}
            
        time.sleep(2)

        driver.close()

        # Cerrar el navegador
        driver.quit()
       
        return salida_json
    except Exception as inst:
        print("inst",inst)
       

        return {"status": "Failed to supermercado" }


