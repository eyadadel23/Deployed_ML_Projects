# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 18:08:47 2023

@author: User
"""


import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import numpy as np
from sklearn.preprocessing import LabelEncoder

encoder = LabelEncoder()



# loading the saved models


car_prediction = pickle.load(open('Car Price Prediction-Copy1.sav', 'rb'))

heart_prediction = pickle.load(open('Hert Diease Prediction.sav', 'rb'))

#bigmart_sales_prediction = pickle.load(open('Big mart Sales Prediction.sav', 'rb'))

#diabetes_prediction = pickle.load(open('Diabetes Prediction.sav', 'rb'))

developers_salary_prediction = pickle.load(open('Developers salary prediction.sav', 'rb'))

# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Multiple Prediction Systems',
                          
                          ['Used Cars Present Price Prediction',
                           'Hert Diease Prediction',
                           #'Bigmart sales prediction',
                           #'Diabetes prediction',
                           'Developers salary prediction'],
                          #icons=['Car','heart'],
                          default_index=0)
    

# Used Cars Present Price Prediction Page
if (selected == 'Used Cars Present Price Prediction'):
    
    # page title
    st.title('Used Cars Present Price Prediction using ML')
    
    
    # Getting the input data from the user for each feature:
        
    # Below we are creating fields so we can get the data from the user and then predict based on that    
    
    Year = st.text_input(" Enter the selling year, try(2014)")
    Selling_Price = st.text_input(" Enter the The selling price, try (3.35)")
    Kms_Driven = st.text_input(" Enter the killometers driven, try (27000)")
    Owner = st.text_input(" Enter the number of previous owners, try (0)")
    Seller_Type = st.text_input(" Enter the seller type; Dealer = 1 // Individual = 0 ")
    
        
     
     
    # code for Prediction
    carpredict = ''
    
    # creating a button for Prediction
    
    if st.button('Predict the present car price'):
        car_predict = car_prediction.predict([[Year,Selling_Price,Kms_Driven,Owner,Seller_Type]])                          
        
        #f'The predicted present car price is:{car_predict}in thousand USD ($)'
        
        carpredict = f'The Predicted Present Car Price Is: {car_predict.round()}Thousands Dollars.'
        
        
    st.success(carpredict)
        
    
    

# Hert Diease Prediction Page
if (selected == "Hert Diease Prediction"):
    
    # page title
    st.title("Hert Diease Prediction using ML")
    
    # Getting the input data from the user for each feature:
    
    # Below we are creating fields so we can get the data from the user and then predict based on that    
    
    age = st.text_input(" Enter the age, try (63)")
    sex = st.text_input(" Enter the The sex, (1 = 'Male'; 0 = 'Female') ")
    cp = st.text_input(" Enter the chest pain type, try (3)")
    trestbps = st.text_input(" Enter the resting blood pressure value, try (145)")
    chol = st.text_input(" Enter the serum cholestoral in mg/dl, try (233)")
    fbs = st.text_input(" Enter the fasting blood sugar value, try (1)")
    restecg = st.text_input(" Enter the resting electrocardiographic results, try (0)")
    thalach = st.text_input(" Enter the maximum heart rate achieved, try (150)")
    exang = st.text_input(" Enter the exercise induced angina (1 = yes; 0 = no)")
    oldpeak = st.text_input(" Enter the ST depression induced by exercise relative to rest value, try (2.3)")
    slope = st.text_input(" Enter the the slope of the peak exercise ST segment value, try (0)")
    ca = st.text_input(" Enter the number of major vessels, try (0)")
    thal = st.text_input(" Enter the thal value; (1 = normal; 2 = fixed defect; 3 = reversable defect)")

    
    
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Submit and Predict"):
        heart_predict = heart_prediction.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])                          
        
        if (heart_predict[0] == 0):
          heart_diagnosis = "This person is healthy"
        else:
          heart_diagnosis = "This person has a heart disesse"
        
    st.success(heart_diagnosis)
    
    
    
# Developers salary prediction Page
if (selected == 'Developers salary prediction'):
    
    # page title
    st.title('Developers salary prediction using ML')
    
    # Getting the input data from the user for each feature:
    
    # Below we are creating fields so we can get the data from the user and then predict based on that
    
    EdLevel = (
        "Bachelor’s degree (B.A., B.S., B.Eng., etc.)",
        "Master’s degree (M.A., M.S., M.Eng., MBA, etc.)",
        "Some college/university study without earning a degree",
        "Secondary school (e.g. American high school, German Realschule or Gymnasium, etc.)",
        "Associate degree (A.A., A.S., etc.)",
        "Other doctoral degree (Ph.D., Ed.D., etc.)",
        "Primary/elementary school",
        "Professional degree (JD, MD, etc.)",
        "I never completed any formal education",)
    
    Employment = (
        "Employed full-time",
        "Student",
        "Independent contractor, freelancer, or self-employed",
        "Not employed, but looking for work",
        "Employed part-time",)
    
    # bulding select box:
        
    edu_level = st.selectbox("Select The Education Level", EdLevel)
    
    Employment_system = st.selectbox("Select The Employment System", Employment)

    experince_years = st.slider("Choose the number of years of experience",0,50,3)
    
    LanguageWorkedWith_Count = st.slider("Choose the number of languages you have experience in or have used before",0,15,1)
    
    # creating a button for Prediction
    
    
    ok = st.button('Predict the salary')
    
    if ok: 
        x = np.array([[edu_level, Employment_system, experince_years, LanguageWorkedWith_Count]])
        
        x[:,0] = encoder.transform(x[:,0])
        x[:,1] = encoder.transform(x[:,1])
        x = x.astype(float)
                                  
        dev_sal_pred = developers_salary_prediction.predict(x)
        #f'The predicted present car price is:{car_predict}in thousand USD ($)'
        
        devsalpredict = f'The Predicted Salary Is $: {dev_sal_pred.round()}Thousands Dollars.'
        
        
    st.success(devsalpredict)
    
    
