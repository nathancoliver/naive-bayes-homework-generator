# import module
from pdf2image import convert_from_path
import os

files = os.listdir('C:/Users/nathan.oliver/Desktop/Python/IG_Physics_Question_Bank/pdf/Cropped_Questions/')

# print(files)
# Store Pdf with convert_from_path function

for file in files:
      print('C:/Users/nathan.oliver/Desktop/Python/IG_Physics_Question_Bank/pdf/Cropped_Questions/'+file)
      image = convert_from_path('C:/Users/nathan.oliver/Desktop/Python/IG_Physics_Question_Bank/pdf/Cropped_Questions/'+file)
      image.save('C:/Users/nathan.oliver/Desktop/Python/IG_Physics_Question_Bank/png/Cropped_Questions/'+file[0:17]+'.jpg', 'JPEG')


# print(len(images))
 
# for i in range(len(images)):
   
#       # Save pages as images in the pdf
#     images[i].save('C:/Users/nathan.oliver/Desktop/Python/IG_Physics_Question_Bank/pdf/Test/test1.jpg', 'JPEG')
