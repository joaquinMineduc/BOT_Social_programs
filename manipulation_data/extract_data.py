from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer
from get_graph import catch_graphic
from get_data_from_graph import extract_data_from_img
import pdfplumber
import pandas as pd


def format_data(list_data):
    content_text = ""
    for text in list_data:
        content_text = content_text + text
    return content_text
    

def get_data_by_category_unificated(list_texts, conditional_target):
    list_data = []
    last_target = ""
    for text in list_texts: # recorre nuevamente la lista
        if text == conditional_target: # si el target condicion es = al texto detectado en el ciclo
            last_target = text # Se añade el texto al ultimo target
        if text != conditional_target and str(text).isupper(): 
# Si el texto es distinto al targe conidicnal y además no contiene el formato de seccion modifica el ultimo target   
            last_target = text
        if last_target == conditional_target:
            list_data.append(text)
    list_data.pop(0)
    data = format_data(list_data)
    return data


def get_data_from_tables(file):
    with pdfplumber.open(file) as pdf:
        first_page = pdf.pages[0]
        second_page = pdf.pages[1]
        table_one = first_page.extract_table()
        table_two = second_page.extract_table()
        for row in table_one:
            print(row[-1])
            
        for row in table_two:
            print(row[-1])
      
        
        

list_texts = []
for page_layout in extract_pages('app/inputs/2021/Educación Especial Diferencial.pdf'):
    for element in page_layout:
        if isinstance(element, LTTextContainer):
            list_texts.append(element.get_text())
            #print(element.get_text().replace("\n",""))

data_df = []
data_dict = dict()
for index, text in enumerate(list_texts):
    if index == 0:
        data_dict['Año monitoreo'] = text[-5:-1]
    if index == 1:
        data_dict['nombre programa'] = text
    if text == 'HISTORIAL EVALUATIVO DEL PROGRAMA\n':
        data_dict[f'{text}'] = get_data_by_category_unificated(list_texts, text)
    if text == 'OBSERVACIONES EVALUADOR(ES)\n':
        get_data_from_tables('app/inputs/2021/Educación Especial Diferencial.pdf')
        
        
        
        
#print(data_dict)
            
    
 
 
       
"""df_data = pd.DataFrame([data_dict])
df_data.to_excel("2021.xlsx",sheet_name="2021")"""
        
"""directories = os.listdir("app/inputs")
for directory in directories:
    for file in os.listdir(f'app/inputs/{directory}'):
        document = pymupdf.open(f'app/inputs/{directory}/{file}')
        for doc in document:
            print(doc.get_textpage().extractText())"""
     

