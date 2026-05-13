# Import docx NOT python-docx
import docx
import os
import pandas as pd
from docx2pdf import convert

path_csv = 'C:/Users/nathan.oliver/Desktop/Python/IG_Physics_Question_Bank/csv/final_dataset_new.csv'
path_doc = 'C:/Users/nathan.oliver/Desktop/Python/IG_Physics_Question_Bank/docx/'
path_png = 'C:/Users/nathan.oliver/Desktop/Python/IG_Physics_Question_Bank/png/Cropped_Questions_Downsized/'

print(os.listdir(path_doc))

data = pd.read_csv(path_csv)
df = pd.DataFrame(data)

categories = df['category'].unique()

for category in categories:
    question_number = 1
    df_new = df[df['category'] == category].reset_index()
    print(category)
    print(df_new['category'])
    doc = docx.Document(path_doc + str(category) + '_P2.docx')
    for n in range(len(df_new)):
        if df_new.loc[n,'duplicate'] == 0 and df_new.loc[n,'defunct'] == 0:
            # doc.add_paragraph(df_new.loc[n,'question_id'])
            # doc.add_paragraph(str(question_number) + '. ' + df_new.loc[n,'question_id'] + ' ' + df_new.loc[n,'answer'])
            doc.add_picture(path_png + df_new.loc[n,'question_id'] + '.pdf.png',width=5000000)
            question_number = question_number + 1


    doc.save(path_doc + str(category) + '_P2.docx')
    # convert(path_doc + str(category) + '_P2.docx')
