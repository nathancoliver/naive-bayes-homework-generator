import pandas as pd



def read_csv(path):
    data = pd.read_csv(path,index_col='question_id')
    df = pd.DataFrame(data)
    return df


path1 = 'C:/Users/nathan.oliver/Desktop/Python/IG_Physics_Question_Bank/csv/question_coordinates_filtered.csv'
path2 = 'C:/Users/nathan.oliver/Desktop/Python/IG_Physics_Question_Bank/csv/question_info.csv'

df1 = read_csv(path1)
df2 = read_csv(path2)

print(len(df1))
print(len(df2))

df_new = pd.merge(df1,df2,left_index=True,right_index=True)

print(len(df_new))

path = 'C:/Users/nathan.oliver/Desktop/Python/IG_Physics_Question_Bank/csv/question_info_coordinates.csv'

df_new.to_csv(path)
