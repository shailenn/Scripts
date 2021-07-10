from PIL import Image
import pytesseract

image_name = 'index.jpg'

s = pytesseract.image_to_string(Image.open('index.jpg'))

f = open('output.txt', 'w')
f.write(s)
f.close()