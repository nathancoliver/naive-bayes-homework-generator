import pandas as pd
import numpy as np
import os

files = os.listdir('C:/Users/nathan.oliver/Desktop/Python/IG_Physics_Question_Bank/pdf/Questions')


path = 'C:/Users/nathan.oliver/Desktop/Python/IG_Physics_Question_Bank/csv/question_coordinates.csv'

data = pd.read_csv(path)
df = pd.DataFrame(data)



n = 1

def num_to_text(n):
    num_text = str(n) + '  '
    return num_text

num_text = num_to_text(n)

question_list = []
x_corr = []
y_corr = []
question_id = []

l = 3



for i in range(len(df)):

    txt = df.loc[i,'text']
    txt = txt.lstrip(' \n')
    if txt[0:l] == num_text:
        question_list.append(txt)
        x_corr.append(df.loc[i,'x_corr'])
        y_corr.append(df.loc[i,'y_corr'])
        if n < 10:
            question_id.append(df.loc[i,'question_file']+'_0'+str(n))
        else:
            question_id.append(df.loc[i,'question_file']+'_'+str(n))
        n = n + 1
        num_text = num_to_text(n)

        print(n)

        if n == 10:
            l = 4
        if n == 1:
            l = 3
        if n == 41:
            print('entered reset')
            n = 1
            l = 3
            num_text = num_to_text(n)
            print(num_text)


df_new = pd.DataFrame({'question_id':question_id,'text':question_list,'x_corr':x_corr,'y_corr':y_corr})

df_new.to_csv('C:/Users/nathan.oliver/Desktop/Python/IG_Physics_Question_Bank/csv/question_coordinates_filtered.csv',index=False)
