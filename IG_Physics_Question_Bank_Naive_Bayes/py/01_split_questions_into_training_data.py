import pandas as pd
import numpy as np
import os

def read_csv(path):
    data = pd.read_csv(path,encoding='cp1252')
    df = pd.DataFrame(data)
    return df

files = os.listdir('C:/Users/nathan.oliver/Desktop/Python/IG_Physics_Question_Bank_Naive_Bayes/csv/')

df = read_csv('C:/Users/nathan.oliver/Desktop/Python/IG_Physics_Question_Bank_Naive_Bayes/csv/question_data.csv')

# df = df['text'].str.encode('ascii', 'ignore').str.decode('ascii')

df_new = df.replace('PhysicsAndMathsTutor.com',' ',regex=True)

questions = []
section_code = []

print(len(df_new))

for i in range(len(df_new)):
    text = df_new.loc[i,'text']

    num_questions = df_new.loc[i,'number_questions']
    section = df_new.loc[i,'section_code']
    print(section)
    chars = [*text]



    A,B,C,D = 0,0,0,0
    k = 2
    t = 0
    break_loop = 0


    for n in range(1,len(chars)-2):

        char = chars[n]

        str_k = str(k)


        if k < 10:
            if char == 'A' and chars[n-1] == ' ' and chars[n+1] == ' ':
                A = 1
            if char == 'B' and chars[n-1] == ' ' and chars[n+1] == ' ':
                B = 1
            if char == 'C' and chars[n-1] == ' ' and chars[n+1] == ' ':
                C = 1
            if char == 'D' and chars[n-1] == ' ' and chars[n+1] == ' ':
                D = 1
            if str(k) == char and chars[n-1] == ' ' and chars[n+1] == ' ' and D == 1 and C == 1 and B == 1 and A == 1:
                # print('entered the matrix')
                question = text[t:n-1]
                questions.append(question)
                section_code.append(section)
                # print(questions)
                t = n
                k = k + 1
                A,B,C,D = 0,0,0,0
        elif k == num_questions+1 and break_loop == 0:
            # print('entered last question')
            question = text[t:]
            questions.append(question)
            section_code.append(section)
            # print(questions)
            break_loop = 1
        else:
            # print('string k[0]: ',str_k[0])
            # print('string k[1]: ',str_k[1])
            if char == 'A' and chars[n-1] == ' ' and chars[n+1] == ' ':
                A = 1
            if char == 'B' and chars[n-1] == ' ' and chars[n+1] == ' ':
                B = 1
            if char == 'C' and chars[n-1] == ' ' and chars[n+1] == ' ':
                C = 1
            if char == 'D' and chars[n-1] == ' ' and chars[n+1] == ' ':
                D = 1
            if str_k[0] == chars[n] and str_k[1] == chars[n+1] and chars[n-1] == ' ' and chars[n+2] == ' ' and D == 1 and C == 1 and B == 1 and A == 1:
                # print('entered the matrix')
                question = text[t:n-1]
                questions.append(question)
                section_code.append(section)
                # print(questions)
                t = n
                k = k + 1
                A,B,C,D = 0,0,0,0


        # break

print(questions)



print(np.size(np.full((num_questions,),num_questions)))

# df_final = pd.DataFrame({'section':np.full((num_questions,),section),'question_text':questions})
df_final = pd.DataFrame({'section':section_code,'question_text':questions})

df_final.to_csv('C:/Users/nathan.oliver/Desktop/Python/IG_Physics_Question_Bank_Naive_Bayes/csv/text.csv',index=True)
