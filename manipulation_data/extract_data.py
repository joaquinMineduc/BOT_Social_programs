import pymupdf
import os
import json

doc = pymupdf.open(f'inputs/{2021}/Centro de Lectura y Biblioteca Escolar (CRA).pdf')

for file in doc:
    value  = file.get_textpage().extractWORDS()
    for v in value:
        print(v[4])
        
        
        
"""for a in doc:
    x = a.get_textpage("text").extractJSON()
    values = json.loads(x)
    for value in values['blocks']:
        for val in value['lines']:
            for index, v in enumerate(val['spans']):
                print(f"{index}/{v['text']}")
            """
    

"""def extrac_data_from_files(dir):
    doc = pymupdf.open(f'inputs/{dir}/Centro de Lectura y Biblioteca Escolar (CRA).pdf')
    for index , page in enumerate(doc):
        text = page.get_textpage().extractText()
        print(f'{index}/{text}')
  

for directory in os.listdir("inputs"):
    print(f"============{directory}========")
    for file in os.listdir(f"inputs/{directory}"):
        extrac_data_from_files(directory)
"""





