import fitz  # PyMuPDF

def catch_graphic(pdf_path):
    #pdf_path = 'C:/Users/joaquin.astorga/mis_proyectos/BAPS/app/inputs/2021/Aula 360.pdf'  # Cambia esto por la ruta a tu PDF
    doc = fitz.open(pdf_path)

    # Recorremos cada página
    for page_index in range(len(doc)):
        page = doc[page_index]
        image_list = page.get_images(full=True)
        for img_index, img in enumerate(image_list):
            xref = img[0]
            if img_index == 6:
                base_image = doc.extract_image(xref)
                image_bytes = base_image["image"]
                image_ext = base_image["ext"]
                image_filename = f"img_grap.{image_ext}"   
                  
    # Guardar imagen extraída
    with open(f'app/manipulation_data/grap/{image_filename}', "wb") as f:
        f.write(image_bytes)      
    print(f"✅ Imagen extraída y guardada como: {image_filename}")

