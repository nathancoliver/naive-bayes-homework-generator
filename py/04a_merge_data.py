import pandas as pd



def read_csv(path):
    data = pd.read_csv(path,index_col='question_id')
    df = pd.DataFrame(data)
    return df


path1 = 'C:/Users/nathan.oliver/Desktop/Python/IG_Physics_Question_Bank/csv/question_coordinates_filtered.csv'
path2 = 'C:/Users/nathan.oliver/Desktop/Python/IG_Physics_Question_Bank/csv/question_info.csv'
path3 = 'C:/Users/nathan.oliver/Desktop/Python/IG_Physics_Question_Bank/csv/question_page_num_edit.csv'

df1 = read_csv(path1)
df2 = read_csv(path2)
df3 = read_csv(path3)


print(len(df1))
print(len(df2))
print(len(df3))

print(df1.columns)
print(df2.columns)
print(df3.columns)


df_new = pd.merge(df1,df2,left_index=True,right_index=True)
df_new = pd.merge(df_new,df3,left_index=True,right_index=True)

print(len(df_new))

path = 'C:/Users/nathan.oliver/Desktop/Python/IG_Physics_Question_Bank/csv/question_info_coordinates_new.csv'

df_new.to_csv(path)
