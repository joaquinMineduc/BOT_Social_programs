from datetime import datetime
from PIL import Image
from paddleocr import PaddleOCR
import cv2
import os

def get_last_four_years():
    list_years = []
    year = datetime.now().year -1
    for year_less in range(4):
        temp = year - year_less
        list_years.append(temp)
    return list_years  


def cut_img(route, x1, x2, y1, y2):
    img = cv2.imread(route)
    if img is None:
        print("La imagen no ha sido cargada correctamente")
        exit()
    recorte = img[y1:y2, x1:x2] 
    # img[y1,y2, x1,x2] y1 = es el comienzo, y2 es hasta donde quiero llegar
    # x1 = es mi comienza y x2 hasta donde quiero llegar en el eje horizontal
    cv2.imwrite(route, recorte)
    
    
    
def extract_data_from_img(route):
        list_result = []
        # Inicializa el OCR en español
        ocr = PaddleOCR(use_angle_cls=True, lang='es')  # lang='en' para inglés
        # Ruta de la imagen que quieres analizar
        results = ocr.ocr(route, cls=True)
        # Imprime solo el texto detectado
        for line in results:
            for box in line:
                list_result.append(box[1][0])
        return list_result
