import fitz
import os

path_load = 'C:/Users/nathan.oliver/Desktop/Python/IG_Physics_Question_Bank/pdf/Cropped_Questions/'
path_save = 'C:/Users/nathan.oliver/Desktop/Python/IG_Physics_Question_Bank/png/Cropped_Questions/'

files = os.listdir(path_load)

for file in files:
    doc = fitz.open(path_load + file)
    page = doc.load_page(0)
    pix = page.get_pixmap(dpi=1000)
    pix.save(path_save+file+'.png')


