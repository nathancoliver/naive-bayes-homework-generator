import PyPDF2 as pdf
import pandas as pd
import numpy as np
import os

files = os.listdir('C:/Users/nathan.oliver/Desktop/Python/IG_Physics_Question_Bank/pdf/Questions')

page_text = []
question_text = []
page_number = []
question_number = []
question_id = []
question_file = []

def read_csv(path):
    data = pd.read_csv(path)
    df = pd.DataFrame(data)
    return df


for file in files:

    page_text = []
    doc_text = []

    path_pdf = 'C:/Users/nathan.oliver/Desktop/Python/IG_Physics_Question_Bank/pdf/Questions/' + file

    reader = pdf.PdfReader(path_pdf)
    num_pages = reader.getNumPages()



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

    # print(doc_text)
    print(file)
    for n in range(1,41):
        print(n)

        try:
            doc_text2 = doc_text.split('  ' + str(n) + ' ')
        except:
            doc_text2 = doc_text.split(' \\n' + str(n) + ' ')
            print(doc_text2)

        if n == 6:
            print(doc_text2)
        try:
            doc_text3 = doc_text2[1].split('  ' + str(n+1) + ' ')
        except:
            doc_text2 = doc_text.split(' \\n' + str(n) + ' ')
            doc_text3 = doc_text2[1].split(' \\n' + str(n+1) + ' ')

        question_text.append(doc_text3[0])

        question_number.append(n)

        question_file.append(file[0:14])

        if n < 10:
            question_id.append(file[0:14]+'_0'+str(n))
        else:
            question_id.append(file[0:14]+'_'+str(n))



    for n in range(1,41):
        num_text = num_to_text(n)
        for page_num in range(len(page_text)):

            if num_text in page_text[page_num]:
                page_number.append(page_num+1)

print(len(question_id))
print(len(question_number))
print(len(page_number))
print(len(question_text))
print(len(question_file))

print(page_number)

df = pd.DataFrame({
        'question_id':question_id,
        'question_number':question_number,
        'question_page':page_number,
        'question_text':question_text,
        'question_file':question_file
    })

path_csv = 'C:/Users/nathan.oliver/Desktop/Python/IG_Physics_Question_Bank/csv/question_info.csv'

df.to_csv(path_csv,index=False)
