from PyPDF2 import PdfReader, PdfWriter, Transformation

# Get the data
reader_base = PdfReader('C:/Users/nathan.oliver/Desktop/Python/IG_Physics_Question_Bank/pdf/Test/blank.pdf')
page_base = reader_base.pages[0]

reader = PdfReader('C:/Users/nathan.oliver/Desktop/Python/IG_Physics_Question_Bank/pdf/Test/test1.pdf')
page_box = reader.pages[0]

x_page, y_page = page_box.cropbox.upper_right

x_move = 100
y_move = 100

page_box.bleedbox.upper_left = (x_move,y_move)
page_box.bleedbox.lower_right = (x_page + x_move ,y_page + y_move)

transformation = Transformation().translate(tx=x_move, ty=y_move)
page_box.add_transformation(transformation)
page_base.merge_page(page_box)

# Write the result back
writer = PdfWriter()
writer.add_page(page_base)
with open('C:/Users/nathan.oliver/Desktop/Python/IG_Physics_Question_Bank/pdf/Test/blank_question.pdf', "wb") as fp:
    writer.write(fp)
