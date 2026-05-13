# Import docx NOT python-docx
import docx
import os
import pandas as pd

path_csv = 'C:/Users/nathan.oliver/Desktop/Python/IG_Physics_Question_Bank/csv/question_categorized.csv'

data = pd.read_csv(path_csv)
df = pd.DataFrame(data)

print(df)

duplicate_list = []

df['text_new'] = df['text'].str.replace('\d+', '')
df['text_new'] = df['text_new'].str.replace(' ', '')

df['duplicate'] = 0

print(df['text_new'])
n=0

for i in range(len(df)):
    text = df.loc[i,'text_new']

    for j in range(i+1,len(df)):
        # print(j)
        compare = df.loc[j,'text_new']

        if text == compare:
            # print(text, compare)
            n=n+1
            # print(j)
            df.loc[j,'duplicate'] = 1

print(n)
path_csv = 'C:/Users/nathan.oliver/Desktop/Python/IG_Physics_Question_Bank/csv/question_categorized_duplicates.csv'

df.to_csv(path_csv,index=False)
