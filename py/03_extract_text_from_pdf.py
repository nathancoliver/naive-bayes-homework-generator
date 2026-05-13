import PyPDF2 as pdf
import pandas as pd
import numpy as np
import os

files = os.listdir('C:/Users/nathan.oliver/Desktop/Python/IG_Physics_Question_Bank/pdf/Answers')

print(files[0])

def read_csv(path):
    data = pd.read_csv(path)
    df = pd.DataFrame(data)
    return df

path_pdf = 'C:/Users/nathan.oliver/Desktop/Python/IG_Physics_Question_Bank/pdf/Questions/0625_s16_qp_21.pdf'
path_csv = 'C:/Users/nathan.oliver/Desktop/Python/IG_Physics_Question_Bank/csv/text_coordinates_0625_s16_qp_21.csv'

df = read_csv(path_csv)

reader = pdf.PdfReader(path_pdf)
num_pages = reader.getNumPages()

page_text = []

for n in range(num_pages):
    page = reader.pages[n]
    text = page.extractText()
    page_text.append(text)

# text_nospace = text.replace(' ','')
# text_nospace = re.sub("[^a-zA-Z0-9]+", "",text_nospace)

num = np.arange(1,41,1)

def num_to_text(n):
    num_text = '  ' + str(n) + ' '
    return num_text


doc_text = ' '.join(page_text)

for i in range(1,num_pages+1):

    num_text = str(i) + " \n"
    doc_text = doc_text.replace(num_text,' ')

n = 1
l = 3

question_text = []

for n in range(1,41):

    doc_text2 = doc_text.split('  ' + str(n) + ' ')

    doc_text3 = doc_text2[1].split('  ' + str(n+1) + ' ')

    question_text.append(doc_text3[0])


page_number = []

for n in range(1,41):
    num_text = num_to_text(n)
    for page_num in range(len(page_text)):

        if num_text in page_text[page_num]:
            page_number.append(page_num+1)



df = pd.DataFrame({'question_number':np.arange(1,41,1),'question_page':page_number,'question_text':question_text})

path_csv = 'C:/Users/nathan.oliver/Desktop/Python/IG_Physics_Question_Bank/csv/what.csv'

df.to_csv(path_csv,index=False)
