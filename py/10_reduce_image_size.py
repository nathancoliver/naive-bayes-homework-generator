from PIL import Image
import os

path = 'C:/Users/nathan.oliver/Desktop/Python/IG_Physics_Question_Bank/png/Cropped_Questions/'

files = os.listdir(path)

for file in files:
    foo = Image.open(path+file)
    x, y = foo.size

    # print(x,y)
     # My image is a 200x374 jpeg that is 102kb large
     # foo.size  # (200, 374)

     # downsize the image with an ANTIALIAS filter (gives the highest quality)
    # foo = foo.resize(int((round(x-x*.2,0)),int(round(y-y*.2,0))),Image.ANTIALIAS)
    # foo = foo.resize((x-1000,y-500),Image.ANTIALIAS)

    foo.save('C:/Users/nathan.oliver/Desktop/Python/IG_Physics_Question_Bank/png/Cropped_Questions_Downsized/' + file, optimize=True,quality=20)

