from PyPDF2 import PdfWriter, PdfReader, Transformation
import pandas as pd



c

path = 'C:/Users/nathan.oliver/Desktop/Python/IG_Physics_Question_Bank/csv/question_info_coordinates_new.csv'

df = read_csv(path)

print(df.info())

for n in range(len(df)):

    question_file = df.loc[n,'question_file']
    question_id = df.loc[n,'question_id']

    reader = PdfReader('C:/Users/nathan.oliver/Desktop/Python/IG_Physics_Question_Bank/pdf/Questions/' + question_file + '.pdf')
    writer = PdfWriter()

    # set question page number
    page_num = df.loc[n,'question_page'] - 1
    x_corr = df.loc[n,'x_corr']
    y_corr = df.loc[n,'y_corr']

    # set next question page number
    # if question page number and next question page number are not the same, then the question will
    try:
        next_page_num = df.loc[n+1,'question_page'] - 1
        y_corr_next = df.loc[n+1,'y_corr']
        next_question_text = df.loc[n+1,'text']
    except:
        next_page_num = 100
    page = reader.pages[int(page_num)]
    x_page, y_page = page.cropbox.upper_right

    # op = Transformation().scale(sx=0.3, sy=0.3)
    # page.add_transformation(op)

    top_adj = 25
    btm_adj = 25

    # for page in reader.pages:
    if next_page_num == page_num:

        page.cropbox.upper_left = (x_corr,y_page-y_corr+top_adj)
        page.cropbox.lower_right = (550,y_page-y_corr_next+btm_adj)

        # print(next_question_text)


    else:

        page.cropbox.upper_left = (x_corr,y_page-y_corr+top_adj)
        page.cropbox.lower_right = (550,y_page-780+btm_adj)

        # page.trimbox.upper_left = (49.60629,y_page-75.2325464+top_adj)
        # page.trimbox.lower_right = (550,y_page-350.052505392+btm_adj)

        # page.bleedbox.upper_left = (49.60629,y_page-75.2325464+top_adj)
        # page.bleedbox.lower_right = (550,y_page-350.052505392+btm_adj)




    # page.scaleTo(50, 10)

    writer.add_page(page)
    # writer.remove_text('Which diagram shows the current-voltage (I - V) characteristic for a filament lamp?')

    with open('C:/Users/nathan.oliver/Desktop/Python/IG_Physics_Question_Bank/pdf/Cropped_Questions/' + question_id + '.pdf','wb') as fp:
        writer.write(fp)
