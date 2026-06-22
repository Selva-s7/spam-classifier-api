# SPAM DETECTION API

# OVERVIEW
Built and  trained a model that detects whether a given message is spam or not

# WHAT DID I DO
I took an spam dataset and processed it with TFIDFVectorizer
used pipeline to serialize and saved it up with joblib
then wrapped the model with Flask api

## TECH USED
-PYTHON
-PANDAS
-SCIKIT LEARN
-JOBLIB
-FLASK

## SAMPLE TEST
data={
    "message":"You won a free size"
}
data2={
    "message":"hi how are you"
}

## PREDICTION
{"Prediction": "spam"}
{"Prediction": "ham"}

## HOW TO RUN
-RUN THE app.py
-RUN THE test.py with test data