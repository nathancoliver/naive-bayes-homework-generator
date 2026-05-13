import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

def to_csv(path):
    data = pd.read_csv(path)
    df = pd.DataFrame(data)
    return df

path1 = 'C:/Users/nathan.oliver/Desktop/Python/IG_Physics_Question_Bank_Naive_Bayes/csv/text.csv'
path2 = 'C:/Users/nathan.oliver/Desktop/Python/IG_Physics_Question_Bank/csv/question_info_coordinates_new_edit.csv'

df = to_csv(path1)
df2 = to_csv(path2)

vectorizer = CountVectorizer(stop_words='english')
all_features = vectorizer.fit_transform(df['question_text'])
# all_features2 = vectorizer.fit_transform(df2['question_text'])
all_features2 = vectorizer.transform(df2['question_text'])
print(all_features.shape)
print(vectorizer.vocabulary_)

# X_train, X_test, Y_train, Y_test = train_test_split(all_features, df['section'],test_size=0.01,random_state = 20)

# print(X_train.shape)
# print(X_test.shape)

classifier = MultinomialNB()

classifier.fit(all_features,df['section'])

prediction = classifier.predict(all_features2)

print(prediction.shape)

# correct = (Y_test == classifier.predict(X_test)).sum()

# incorrect = Y_test.size - correct

# fraction_right = correct / (correct + incorrect)

# print(fraction_right)

df2['category'] = prediction

path = 'C:/Users/nathan.oliver/Desktop/Python/IG_Physics_Question_Bank/csv/question_categorized.csv'

df2.to_csv(path,index=False)
