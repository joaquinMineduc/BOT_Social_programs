from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from functions import get_last_four_years
import time
import requests
import os


route= os.getcwd()
base_directory = os.path.basename(route)

driver = webdriver.Chrome()


def extract_data(driver, year):  
    list_names_programs = []  
    driver.find_element(By.XPATH, f"//a[contains(text(), 'Ministerio de Educación')]").click()
    time.sleep(3)
    names_programs = driver.find_elements(By.XPATH, "//div[@id='instrumento_gestion"+
        "_group_14437_pvid_14438']//p")

    # Se almacenan todos los nombres de programas sociales pertenecientes a la Subsecretaría de Educación
    for name_program in names_programs:
        list_names_programs.append(name_program.text)
        
    new_directory = os.path.join("inputs",f'{year}')
    if not os.path.exists(new_directory):
        os.makedirs(new_directory)

    """Este ciclo se encarga de acceder a cada uno de los documentos PDF y al identificarlos
    comienza a extraer el link del PDF embebido para luego realizar un request y extrar el 
    archivo en formato PDF """
    for name in list_names_programs:
        link = driver.find_element(By.XPATH, "//a[@title='Ir a Documento PDF :"+
            f" {name}']").get_property("href")
        #time.sleep(0.5)
        
        file_path = os.path.join(new_directory, f'{name}.pdf')
        print(file_path)
        #El PDF está embebido dentro del html, por lo tanto se descarga directamente el documento.
        response = requests.get(link) # Gestionar el acceso a link

        with open(file_path, 'wb') as file:
            file.write(response.content)

   

# Ingreso a la página web
driver.get('https://www.dipres.gob.cl/598/w3-propertyvalue-24167.html#instrumentos')
time.sleep(3)
    
#Selección de años
#Se debe seleccionar los últimos 3 años
list_years = get_last_four_years()
    
for year in list_years:
    try:
        driver.refresh()
        driver.get('https://www.dipres.gob.cl/598/w3-propertyvalue-24167.html#instrumentos')
        time.sleep(3)
        driver.find_element(By.CLASS_NAME, "ntg-label-monitoreo").click()
        time.sleep(3)
        driver.find_element(By.XPATH, f"//a[contains(text(), '{year}')]").click()
        time.sleep(3)
    except NoSuchElementException:
        print(f"elemento no encontrado")
        continue
    except:
        print(f"No existe registros de monitoreos realizados el {year}")
        continue
    extract_data(driver, year)
    
    
    
    
