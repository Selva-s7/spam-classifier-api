from flask import Flask,request,jsonify
import joblib
import pandas as pd
app=Flask(__name__)
pipeline=joblib.load('spam-pipeline.joblib')
@app.route('/predict',methods=['POST'])
def spamPredict():
    data=request.get_json()
    message=data['message']
    prediction=pipeline.predict([message])
    label='spam' if prediction[0]==1 else 'ham'
    return jsonify({'Prediction':label})
if __name__=="__main__":
    app.run(debug=True)
    