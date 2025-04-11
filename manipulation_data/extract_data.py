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

        
for index, text in enumerate(list_texts):
    if index == 11:
        split_words = text.split("\n")
#print(split_words)

for value in split_words:
    print(value)

"""for index, text in enumerate(list_texts):
    if index == 1:
        dict_texts['Nombre del programa'] = text
        dict_texts['año del programa'] = 2021
    if index == """
        

"""directories = os.listdir("app/inputs")
for directory in directories:
    for file in os.listdir(f'app/inputs/{directory}'):
        document = pymupdf.open(f'app/inputs/{directory}/{file}')
        for doc in document:
            print(doc.get_textpage().extractText())"""
"""            
doc = pymupdf.open(f"C:/Users/joaquin.astorga/mis_proyectos/BAPS/app/inputs/2021/Aula 360.pdf")

list_words = []

for index, files in enumerate(doc):
    files = files.get_textpage().extractText()
    if index == 3:
        files = str(files)
        file = files.replace("\n"," ")
        for word in file.split(" "):
            list_words.append(word)
print(list_words)


for word in list_words:
    print(word)
        #print(f'{index}-{files}')"""