import fitz
import os

files = os.listdir('C:/Users/nathan.oliver/Desktop/Python/IG_Physics_Question_Bank/pdf/Cropped_Questions/')

# pdffile = 'C:/Users/nathan.oliver/Desktop/Python/IG_Physics_Question_Bank/pdf/Test/test1.pdf'
    doc = fitz.open(pdffile)
    page = doc.load_page(0)  # number of page
    pix = page.get_pixmap(dpi=1000)
    output = 'C:/Users/nathan.oliver/Desktop/Python/IG_Physics_Question_Bank/png/test/test1.png'
    pix.save(output)

# import module


# print(files)
# Store Pdf with convert_from_path function

for file in files:
      print('C:/Users/nathan.oliver/Desktop/Python/IG_Physics_Question_Bank/pdf/Cropped_Questions/'+file)
      image = convert_from_path('C:/Users/nathan.oliver/Desktop/Python/IG_Physics_Question_Bank/pdf/Cropped_Questions/'+file,1)
      image.save('C:/Users/nathan.oliver/Desktop/Python/IG_Physics_Question_Bank/png/Cropped_Questions/'+file[0:17]+'.jpg', 'JPEG')
