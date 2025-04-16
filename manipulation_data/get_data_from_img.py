from PIL import Image
import pytesseract


# Asegúrate de tener Tesseract instalado y accesible

imagen = Image.open("grafico_p6_7.png")  # Cambia según el nombre generado
texto = pytesseract.image_to_string(imagen, lang='es')

print("📋 Texto extraído desde imagen:")
print(texto)