import pandas as pd

def to_csv(path):
    data = pd.read_csv(path)
    df = pd.DataFrame(data)
    return df

path = 'C:/Users/nathan.oliver/Desktop/Python/IG_Physics_Question_Bank/csv/question_info_coordinates_new.csv'

df = to_csv(path)

print(df['question_text'])


def replace(text):
    df['question_text'] = df['question_text'].str.replace(text,' ',regex=True)
    return df['question_text']

df['question_text'] = replace('.')
df['question_text'] = replace('\\n')
df['question_text'] = replace('Ã')

for i in range(10):
    df['question_text'] = replace(str(i))


# df['question_text'] = df['question_text'].str.rstrip('UCLES')

print(df['question_text'])


path = 'C:/Users/nathan.oliver/Desktop/Python/IG_Physics_Question_Bank/csv/question_info_coordinates_new_edit.csv'
df.to_csv(path,index = False)
