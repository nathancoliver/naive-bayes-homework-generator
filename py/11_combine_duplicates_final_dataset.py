import pandas as pd

def to_csv(path):
    data = pd.read_csv(path)
    df = pd.DataFrame(data)
    return df


path1 = 'C:/Users/nathan.oliver/Desktop/Python/IG_Physics_Question_Bank/csv/question_categorized_duplicates.csv'
path2 = 'C:/Users/nathan.oliver/Desktop/Python/IG_Physics_Question_Bank/csv/final_dataset.csv'

df1 = to_csv(path1)
df2 = to_csv(path2)

print(df1,df2)

df1.set_index('question_id')
df2.set_index('question_id')

df_new = pd.merge(df1,df2,left_index=True,right_index=True)

path3 = 'C:/Users/nathan.oliver/Desktop/Python/IG_Physics_Question_Bank/csv/final_dataset_new.csv'

df_new.to_csv(path3)
