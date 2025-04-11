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

list_words = []
for split_word in split_words:
    words = split_word.split(":")
    for word in words:
        list_words.append(word)
print(list_words)
        

    


"""directories = os.listdir("app/inputs")
for directory in directories:
    for file in os.listdir(f'app/inputs/{directory}'):
        document = pymupdf.open(f'app/inputs/{directory}/{file}')
        for doc in document:
            print(doc.get_textpage().extractText())"""
     

