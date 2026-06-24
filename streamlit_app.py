import requests
import streamlit as st
st.title("SPAM CLASSIFIER")

data=st.text_area("Enter message")
if st.button("CHECK MESSAGE"):
    if data=="":
        st.warning(" PLEASE ENTER A MESSAGE FIRST")
    else:
        res=requests.post("http://127.0.0.1:5000/predict",json={"message":data})
        response=res.json()
        if response['Prediction']=="spam":
            st.error("This message is a spam")
            st.write("MODEL PREDICTED AS:",1)
        else:
            st.success("THIS MESSAGE IS NOT A SPAM")
            st.write("MODEL PREDICTED AS:",0)



