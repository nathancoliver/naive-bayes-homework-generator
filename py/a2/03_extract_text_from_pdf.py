import PyPDF2 as pdf
import pandas as pd
import numpy as np
import os

files = os.listdir('C:/Users/nathan.oliver/Desktop/Python/IG_Physics_Question_Bank/pdf/Answers_P2')



# page_text = []
# question_text = []
# page_number = []
# question_number = []
# question_id = []
# question_file = []
# question_id_edit = []

answer = []
question_file = []
question_id = []

def read_csv(path):
    data = pd.read_csv(path)
    df = pd.DataFrame(data)
    return df



path = 'C:/Users/nathan.oliver/Desktop/Python/IG_Physics_Question_Bank/csv/question_categorized.csv'

df_compare = read_csv(path)

for file in files:

    file_name = file[0:14]
    print(file_name)
    file_id = file_name[0:9] + 'qs' + file_name[12:14]

    page_text = []
    doc_text = []



    # path_pdf = 'C:/Users/nathan.oliver/Desktop/Python/IG_Physics_Question_Bank/pdf/Questions_P4/' + file
    path_pdf = 'C:/Users/nathan.oliver/Desktop/Python/IG_Physics_Question_Bank/pdf/Answers_P2/' + file

    # year = str(20)+str(file_name[6:8])
    # print(year)
    reader = pdf.PdfReader(path_pdf)
    num_pages = reader.getNumPages()



    for n in range(1,num_pages):
        page = reader.pages[n]
        text = page.extractText()

        page_text.append(text)

    # print(page_text)

    if int(file_name[6:8]) < 17:
        page_text_new = page_text[0].split('Mark Scheme')

        # print(page_text_new[1])

        text = page_text_new[1]


        text = text.replace('\n',' ')
        text = text.replace('  ',' ')
        text = text.replace('   ',' ')
        text = text.replace('    ',' ')
        text = text.replace('     ',' ')
        text = text.replace('      ',' ')
        text = text.replace('       ',' ')
        text = text.replace('        ',' ')
        text = text.replace('         ',' ')
        text = text.replace('          ',' ')
        text = text.replace('           ',' ')
        text = text.replace('            ',' ')
        text = text.replace('             ',' ')
        text_split = text.split(' ')
        # print(text_split)

        question = np.arange(1,41,1)
        num_1 = 0
        for n in range(1,41):
            for i in range(len(text_split)):
                if text_split[i] == str(n) and text_split[i-1] != '0625':
                    # if n < 10:
                    #     question_id.append(file_name + '_0' + str(n))
                    # else:
                    #     question_id.append(file_name + '_'+ str(n))
                    if num_1 == 0 and n == 1:
                        num_1 = 1
                        answer.append(text_split[i+1])
                        question_file.append(file_name)
                        question_id.append(file_name + '_0' + str(n))
                    elif n < 10 and n > 1:
                        answer.append(text_split[i+1])
                        question_file.append(file_name)
                        question_id.append(file_name + '_0' + str(n))
                    elif n > 9:
                        answer.append(text_split[i+1])
                        question_file.append(file_name)
                        question_id.append(file_name + '_'+ str(n))

    else:
        num_1 = 0
        text = page_text[0] + page_text[1]
        # print(text)
        text = text.replace('\n',' ')
        print(text)
        text = text.replace('Page 2 of 3',' ')
        text = text.replace('Page 3 of 3',' ')
        text = text.replace('  ',' ')
        text = text.replace('   ',' ')
        text = text.replace('    ',' ')
        text = text.replace('     ',' ')
        text = text.replace('      ',' ')
        text = text.replace('        ',' ')
        text = text.replace('         ',' ')
        text = text.replace('          ',' ')
        text = text.replace('           ',' ')
        text = text.replace('            ',' ')
        text = text.replace('             ',' ')
        text_split = text.split(' ')
        print(text_split)

        question = np.arange(1,41,1)

        for n in range(1,41):
            for i in range(len(text_split)):
                if text_split[i] == str(n):
                    # answer.append(text_split[i+1])
                    # question_file.append(file_name)
                    # if n < 10:
                    #     question_id.append(file_name + '_0' + str(n))
                    # else:
                    #     question_id.append(file_name + '_'+ str(n))
                    if num_1 == 0 and n == 1:
                        num_1 = 1
                        answer.append(text_split[i+1])
                        question_file.append(file_name)
                        question_id.append(file_name + '_0' + str(n))
                    elif n < 10 and n > 1:
                        answer.append(text_split[i+1])
                        question_file.append(file_name)
                        question_id.append(file_name + '_0' + str(n))
                    elif n > 9:
                        answer.append(text_split[i+1])
                        question_file.append(file_name)
                        question_id.append(file_name + '_'+ str(n))
        # print(answer)


df_new = pd.DataFrame({'question_id':question_id,'answer':answer,'question_file':question_file})

for n in range(len(df_new)):
    text = df_new.loc[n,'question_id']
    print(text[0:9])
    print(text[11:18])
    df_new.loc[n,'question_id'] = text[0:9]+'qp'+text[11:18]

df_new.set_index('question_id')
df_compare.set_index('question_id')

df_final = pd.merge(df_new,df_compare,left_index=True,right_index=True)

path = 'C:/Users/nathan.oliver/Desktop/Python/IG_Physics_Question_Bank/csv/final_dataset.csv'

df_final.to_csv(path,index=False)



















#     # text_nospace = text.replace(' ','')
#     # text_nospace = re.sub("[^a-zA-Z0-9]+", "",text_nospace)

#     num = np.arange(1,41,1)

#     def num_to_text(n):
#         num_text = '  ' + str(n) + ' '
#         return num_text


#     doc_text = ' '.join(page_text)

#     for i in range(1,num_pages+1):

#         num_text = str(i) + " \n"
#         doc_text = doc_text.replace(num_text,' ')

#     n = 1
#     l = 3

#     # print(doc_text)
#     # print(file)
#     for n in range(1,41):
#         # print(n)


#         doc_text2 = doc_text.split('  ' + str(n) + ' ')

#         try:
#             doc_text3 = doc_text2[1].split('  ' + str(n+1) + ' ')

#             question_text.append(doc_text3[0])

#             question_number.append(n)

#             question_file.append(file[0:14])

#             if n < 10:
#                 question_id.append(file[0:14]+'_0'+str(n))
#             else:
#                 question_id.append(file[0:14]+'_'+str(n))
#         except:
#             question_text.append('pass')
#             question_number.append('pass')
#             question_file.append('pass')
#             question_id.append('pass')

#         # question_text.append(doc_text3[0])

#         # question_number.append(n)

#         # question_file.append(file[0:14])

#         # if n < 10:
#         #     question_id.append(file[0:14]+'_0'+str(n))
#         # else:
#         #     question_id.append(file[0:14]+'_'+str(n))


#     print(file)
#     k = 1
#     for p in range(1,41):
#         # print(p)
#         num_text = num_to_text(p)
#         if p < 10:
#             id_edit = file[0:14]+'_0'+str(p)
#         else:
#             id_edit = file[0:14]+'_'+str(p)

#         for page_num in range(len(page_text)):

#             if num_text in page_text[page_num]:
#                 print(p)
#                 # print(page_num)
#                 question_id_edit.append(id_edit)
#                 page_number.append(page_num+1)



# print(len(question_id))
# print(len(question_number))

# print(len(question_text))
# print(len(question_file))
# print(len(page_number))
# print(len(question_id_edit))

# df2 = pd.DataFrame({
#         'question_id':question_id,
#         'question_number':question_number,
#         'question_text':question_text,
#         'question_file':question_file
#     })

# df = pd.DataFrame({
#         'question_page':page_number,
#         'question_id_edit':question_id_edit,
#     })

# path_csv = 'C:/Users/nathan.oliver/Desktop/Python/IG_Physics_Question_Bank/csv/question_info.csv'
# # path_csv = 'C:/Users/nathan.oliver/Desktop/Python/IG_Physics_Question_Bank/csv/question_page_num_edit.csv'


# df2.to_csv(path_csv,index=False)
