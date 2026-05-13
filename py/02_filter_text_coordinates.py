import pandas as pd
import numpy as np



path = 'C:/Users/nathan.oliver/Desktop/Python/IG_Physics_Question_Bank/csv/text_coordinates_0625_s16_qp_21.csv'

data = pd.read_csv(path)
df = pd.DataFrame(data)

# print(df.loc[39,'text'])

n = 1

def num_to_text(n):
    num_text = str(n) + '  '
    return num_text

num_text = num_to_text(n)

question_list = []
x_corr = []
y_corr = []

l = 3

for i in range(len(df)):

    txt = df.loc[i,'text']
    txt = txt.lstrip(' \n')
    if txt[0:l] == num_text:
        question_list.append(txt)
        x_corr.append(df.loc[i,'x_corr'])
        y_corr.append(df.loc[i,'y_corr'])
        n = n + 1
        num_text = num_to_text(n)

        if n == 10:
            l = 4


df_new = pd.DataFrame({'text':question_list,'x_corr':x_corr,'y_corr':y_corr})

df_new.to_csv('C:/Users/nathan.oliver/Desktop/Python/IG_Physics_Question_Bank/csv/question_coordinates_0625_s16_qp_21.csv',index=False)
