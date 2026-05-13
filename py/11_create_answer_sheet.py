# Import docx NOT python-docx
import pandas as pd
import docx
import math

pd.set_option('display.max_rows', None)

path_csv = 'C:/Users/nathan.oliver/Desktop/Python/IG_Physics_Question_Bank/csv/final_dataset_new.csv'
path_doc = 'C:/Users/nathan.oliver/Desktop/Python/IG_Physics_Question_Bank/docx/Answers/'

data = pd.read_csv(path_csv)
df = pd.DataFrame(data)

print(df.columns)

categories = df['category'].unique()

print(categories)

category = 220

df_new = df[df['category'] == category]
df_new2 = df_new[df_new['duplicate'] == 0]
df_new3 = df_new2[df_new2['defunct'] == 0]

df_new3 = df_new3.reset_index()

length = len(df_new3)

print(length)

rows = math.ceil(length/10)

print(rows)
print(path_doc + str(category) + '_P2_Answers.docx')

doc = docx.Document(path_doc + str(category) + '_P2_Answers.docx')

table = doc.add_table(rows=rows*2, cols=10)

n = 1
for i in range(rows):
    for j in range(10):
        cell1 = table.cell(i*2,j)
        cell2 = table.cell(i*2+1,j)

        cell1.text = str(n)
        cell2.text = df_new3.loc[n-1,'answer']

        n = n + 1

# for n in range(length):
#     question_number = 1

#     doc = docx.Document(path_doc + str(category) + '_P2.docx')
#     for n in range(len(df_new)):


#         doc.add_paragraph(str(question_number) + '. ' + df.loc[n,'question_id'])
#         doc.add_picture(path_png + df_new.loc[n,'question_id'] + '.pdf.png',width=5000000)
#         question_number = question_number + 1

print(df_new3)

# doc.save(path_doc + str(category) + '_P2_Answers.docx')
    # convert(path_doc + str(category) + '_P2.docx')
