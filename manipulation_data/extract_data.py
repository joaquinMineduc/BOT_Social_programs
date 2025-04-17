from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer
from get_graph import catch_graphic
from get_data_from_graph import extract_data_from_img
import pandas as pd

list_texts = []
for page_layout in extract_pages('C:/Users/joaquin.astorga/mis_proyectos/BAPS/app/inputs/2021/Aula 360.pdf'):
    for element in page_layout:
        if isinstance(element, LTTextContainer):
            list_texts.append(element.get_text())
            #print(element.get_text().replace("\n",""))
 
data_df = []    
for index, text in enumerate(list_texts):
    print(f'{index}--> {text}')
"""    if index in [0,1,11,19,22,28,52,85]:
        if index == 0:
            data_df.append(text[-5:-1])
        else:
            data_df.append(text)
    else:
        if index == 30 and text == 'III. DESEMPEÑO 2021 DEL PROGRAMA\n':
            catch_graphic('C:/Users/joaquin.astorga/mis_proyectos/BAPS/app/inputs/2021/Aula 360.pdf')
            elemets = extract_data_from_img('app/manipulation_data/grap/img_grap.png')
            for element in elemets:
                data_df.append(element)
        if index == 57 and text[0:20] == 'GASTO POR SUBTÍTULOS':
           
           
           """
#print(data_df)
       
       
        
"""directories = os.listdir("app/inputs")
for directory in directories:
    for file in os.listdir(f'app/inputs/{directory}'):
        document = pymupdf.open(f'app/inputs/{directory}/{file}')
        for doc in document:
            print(doc.get_textpage().extractText())"""
     

