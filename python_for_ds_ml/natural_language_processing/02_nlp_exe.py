#%%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report, confusion_matrix
import nltk

%matplotlib inline
sns.set_style('whitegrid')


#%%
yelp = pd.read_csv('yelp.csv')

#%%
yelp.head()

#%%
yelp.info()

#%%
yelp.describe()

#%%
yelp['text length'] = yelp['text'].apply(len)

#%%
yelp.head()

#%%
g = sns.FacetGrid(yelp,col='stars')
g.map(plt.hist,'text length')

#%%
sns.boxplot(x='stars', y='text length', data=yelp)

#%%
sns.countplot(x='stars',data=yelp,palette='rainbow')

#%%
stars = yelp.groupby('stars').mean()

#%%
stars.corr()

#%%
sns.heatmap(stars.corr(), cmap='coolwarm', annot=True)

#%%
yelp_class = yelp[(yelp.stars==1) | (yelp.stars==5)]
X = yelp_class['text']
y = yelp_class['stars']

#%%
X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.3,random_state=101)

#%%
pipeline = Pipeline([
  ('bow', CountVectorizer()),
  ('tfidf', TfidfTransformer()),
  ('classifier', MultinomialNB)])

#%%
pipeline.fit(X_train,y_train)

#%%
predictions = pipeline.predict(X_test)

#%%
print(confusion_matrix(y_test,predictions))
print(classification_report(y_test,predictions))
