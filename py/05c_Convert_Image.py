from pdf2image import convert_from_path


pages = convert_from_path('C:/Users/nathan.oliver/Desktop/Python/IG_Physics_Question_Bank/pdf/Test/test1.pdf', 500)

for page in pages:
    page.save('C:/Users/nathan.oliver/Desktop/Python/IG_Physics_Question_Bank/pdf/Test/test1.jpg', 'JPEG')
