import requests
data={
    "message":"You won a free size"
}
data2={
    "message":"hi how are you"
}
res=requests.post('http://127.0.0.1:5000/predict',json=data)
res2=requests.post('http://127.0.0.1:5000/predict',json=data2)
print(res.json())
print(res2.json())
