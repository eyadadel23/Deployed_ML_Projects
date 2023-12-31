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
from sklearn.preprocessing import StandardScaler


encoder = LabelEncoder()
scaler = StandardScaler()


# loading the saved models


car_prediction = pickle.load(open('Car Price Prediction-Copy1.sav', 'rb'))

heart_prediction = pickle.load(open('Hert Diease Prediction.sav', 'rb'))

Insurance_Cost_Prediction = pickle.load(open('Medical Insurance Cost Prediction.sav', 'rb'))

diabetes_prediction = pickle.load(open('Diabetes Prediction.sav', 'rb'))

developers_salary_prediction = pickle.load(open('Developers salary prediction.sav', 'rb'))

# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Multiple Prediction Systems',
                          
                          ['Used Cars Present Price Prediction',
                           'Hert Diease Prediction',
                           'Medical Insurance Cost Prediction',
                           'Diabetes prediction',
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
#####################################################################################################
#####################################################################################################
#####################################################################################################        
    

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
####################################################################################################
####################################################################################################
####################################################################################################   
    
       
#Bigmart prediction page:
if (selected == 'Medical Insurance Cost Prediction'):
    
    # page title
    st.title('Medical Insurance Cost Prediction using ML')
    
    
    # Getting the input data from the user for each feature:
    gender = (
        "female",
        "male",)
    
    is_smoker = (
        "yes",
        "no",)
    
    
    # Below we are creating fields so we can get the data from the user and then predict based on that    
    
    age = st.text_input("Enter The Age") 									
   
    sex = st.selectbox("Select The Gender", gender)
    
    bmi = st.text_input("Enter The Body Mass Index,__(weight in kg/(height in m)^2)")
    
    children = st.text_input("Enter The Number Of Children's")
    
    smoker = st.selectbox("Is The Person A Smoker?", is_smoker)
   
    
    # creating a button for Prediction
    
    insurcostpred = ''
    ok = st.button('Predicted Health Insurance Cost')
    
    if ok: 
        x = np.array([[age, sex, bmi, children, smoker]])
        
        x[:,1] = encoder.fit_transform(x[:,1])
        x[:,4] = encoder.fit_transform(x[:,4])
        
        x = x.astype(float)

        insur_cost_pred = Insurance_Cost_Prediction.predict(x)
        #f'The predicted present car price is:{car_predict}in thousand USD ($)'
        
        insur_cost_pred = insur_cost_pred * insur_cost_pred
        
        insurcostpred = f'The Predicted Health Insurance Cost Is $: {insur_cost_pred.round()} Dollars.'
    
    
    st.success(insurcostpred)  
#####################################################################################################
#####################################################################################################
#####################################################################################################    
 
# Diabetes Prediction Page
if (selected == "Diabetes prediction"):
    
    # page title
    st.title("Diabetes prediction using ML")
    
    # Getting the input data from the user for each feature:
        
    # Below we are creating fields so we can get the data from the user and then predict based on that    
    
    Pregnancies = st.text_input("Enter The Number Of Times Pregnant")
    Glucose = st.text_input("Enter The Value Of Plasma glucose concentration a 2 hours in an oral glucose tolerance test,__Try(148)")
    BloodPressure = st.text_input("Enter The Value of Diastolic blood pressure (mm Hg),__Try(72)")
    SkinThickness = st.text_input("Enter The Value of Triceps Skin Fold Thickness (mm),__Try(35)")
    Insulin = st.text_input("Enter The Value Of 2-Hour Serum Insulin (mu U/ml),__Try(0)")
    BMI = st.text_input("Enter The Value Of Body Mass Index (weight in kg/(height in m)^2),__Try(33.6)")
    DiabetesPedigreeFunction = st.text_input("Enter The Value Of Diabetes Pedigree Function,__Try(0.627)")
    Age = st.text_input("Enter The Age")

   
    # code for Prediction
    diabetes_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Submit and Predict"):
        
      diabetes_predict = diabetes_prediction.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])                          
      
      if (diabetes_predict[0] == 0):
        diabetes_diagnosis = "This person is healthy"
      else:
        diabetes_diagnosis = "This person Is Diabetic"
      
        
    st.success(diabetes_diagnosis)
###########################################################################################
###########################################################################################
########################################################################################### 
    
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

    experince_years = st.slider("Choose the number of years of experience",0,50,0)
    
    LanguageWorkedWith_Count = st.slider("Choose the number of Programing languages you have experience in or have used before",0,30,0)
    
    # creating a button for Prediction
    
    devsalpredict = ''
    ok = st.button('Predict the salary')
    
    if ok: 
        x = np.array([[edu_level, Employment_system, experince_years, LanguageWorkedWith_Count]])
        
        x[:,0] = encoder.fit_transform(x[:,0])
        x[:,1] = encoder.fit_transform(x[:,1])
        x = x.astype(float)
                                  
        dev_sal_pred = developers_salary_prediction.predict(x)
        #f'The predicted present car price is:{car_predict}in thousand USD ($)'
        
        dev_sal_pred = dev_sal_pred * dev_sal_pred
        
        devsalpredict = f'The Predicted Salary Is $: {dev_sal_pred.round()}Thousands Dollars.'
        
        
    st.success(devsalpredict)
    
    
