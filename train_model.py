import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline 
import joblib
data=pd.read_csv('spam.csv',encoding='latin-1')
data['v1']=data['v1'].map({'spam':1,'ham':0})
X=data['v2']
Y=data['v1']
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=42)
pipeline=Pipeline(steps=[
    ('process',TfidfVectorizer(stop_words='english')),
    ('model',LogisticRegression())
])
pipeline.fit(X_train,Y_train)
print('Accuracy',pipeline.score(X_test,Y_test))
joblib.dump(pipeline,'spam-pipeline.joblib')

