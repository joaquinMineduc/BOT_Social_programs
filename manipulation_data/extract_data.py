import os
import json
from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer


list_texts = []
dict_texts = dict()
for page_layout in extract_pages('C:/Users/joaquin.astorga/mis_proyectos/BAPS/app/inputs/2021/Aula 360.pdf'):
    for element in page_layout:
        if isinstance(element, LTTextContainer):
            list_texts.append(element.get_text())
            #print(element.get_text())
 
data_df = []    
for index, text in enumerate(list_texts):
    if index in [0,1,11,19,22,28,49,50,51,52,85]:
        if index == 0:
            data_df.append(text[-5:-1])
        data_df.append(text)
    
print(data_df)
    


        
"""directories = os.listdir("app/inputs")
for directory in directories:
    for file in os.listdir(f'app/inputs/{directory}'):
        document = pymupdf.open(f'app/inputs/{directory}/{file}')
        for doc in document:
            print(doc.get_textpage().extractText())"""
     

