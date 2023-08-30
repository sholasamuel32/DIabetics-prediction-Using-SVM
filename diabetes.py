# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 08:29:54 2023

@author: HP
"""


import pandas as pd
import streamlit as st
import pickle

filename = "diabetesmodel.sav"
model = pickle.load(open(filename, 'rb')) 


st.title ('Diabetes Prediction App')
st.subheader('This app takes in certain variable to enable prediction')

def user_imput():
    pregnancy = st.slider('If you are pregnant, how many weeks gone? NB: choose 0 if you are not preganant', 0, 50)
    glucose = st.slider('what is your glucose level?', 0, 300)
    bloodpressure = st.slider('What is your blood Pressue', 0, 200)
    skinthickness = st.slider('What is your Skin Thickness level', 0, 200)
    insulin = st.slider('What is your Insulin data', 0, 200)
    bmi = st.slider('What is your BMI level', 0.0, 200.0)
    diabetespedigree = st.slider('What is your Diabetes Pedigree Function level', 0.0, 20.0)
    age = st.slider('How old are you', 1, 100)
    

    data = {'Pregnancies':pregnancy,
         'Glucose':glucose,
         'BloodPressure':bloodpressure,
         'SkinThickness':skinthickness,
         'Insulin':insulin,
         'BMI':bmi,  
         'DiabetesPedigreeFunction':diabetespedigree,
         'Age':age
         }

    features = pd.DataFrame(data, index=[0])  #- convert the dictionary to dataframe
    
    return features

df = user_imput()


def prediction():
    predict = model.predict(df)
    result = ''
    if predict == 0:
        result = 'Non-Diabetic'
    else:
        result= 'Diabetic'
    return result


submit = st.button('Get prediction')
result = prediction()
if submit:
    st.success('Thank you for filling the form. you are {}'.format(result))

