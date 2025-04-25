import fitz
from functions import cut_img, extract_data_from_img

# Esta funcion permite extraer 1 foto de una pagina en concreto
def get_table(url, num_page):
    file = fitz.open(url)
    page = file[num_page]
    pix = page.get_pixmap(dpi= 300)
    pix.save("app/manipulation_data/tables/table1.png")
    cut_img('app/manipulation_data/tables/table1.png', 1724, 2402, 1959, 2882)
    
get_table("app/inputs/2021/Aula 360.pdf", 0)
print(extract_data_from_img())
