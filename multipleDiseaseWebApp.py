# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 22:53:50 2025

@author: Aakriti
"""

import pickle 
import streamlit as st
from streamlit_option_menu import option_menu
#loading the saved models
diabetes_model=pickle.load(open("C:/Users/Aakriti/OneDrive/Desktop/Projects/MultipleDiseasePred/diabetes.sav",'rb'))
heart_model=pickle.load(open("C:/Users/Aakriti/OneDrive/Desktop/Projects/MultipleDiseasePred/hd.sav",'rb'))
parkinsons_model=pickle.load(open("C:/Users/Aakriti/OneDrive/Desktop/Projects/MultipleDiseasePred/parkinson.sav",'rb'))

#Sidebar for navigation
#for this we use streamlit_option_menu
#sidebar for navigate
with st.sidebar:
    selected=option_menu('Multiple Disease Prediction System',
                         
                         ['Diabetes Prediction',
                          'Heart Disease Prediction',
                          'Parkinsons Prediction'],
                         
                         icons=['bandaid-fill','clipboard2-pulse','person-arms-up'],
                         
                         default_index=0)
# for page icons use bootstrap cause stremalit option menu supports that
#take icon names from bootstrap
   
#default index=0 means that by default it points to first element of the list 

#Diabetes Prediction Page
if(selected=='Diabetes Prediction'):
    
    #page title
    st.title('Diabetes Prediction using ML')
    
    #getting the input data from the user
    #we create columns for input fields
    #to get fields side by side 
    col1,col2,col3=st.columns(3)
    
    with col1:
        Pregnancies=st.text_input("Number of pregnancies")
    with col2:
        Glucose=st.text_input("Glucos Level")
    with col3:
        BloodPressure=st.text_input("BP value")
    with col1:
        SkinThickness=st.text_input("Skin thickness value")
    with col2:
        Insulin=st.text_input("Insulin value")
    with col3:
        BMI=st.text_input("BMI value")
    with col1:
        DiabetesPedigreeFunction=st.text_input("Diabetes Pedigree Function value")
    with col2:
        Age=st.text_input("Age of the person")
    
    
    
    #code for prediction
    
    diab_diagnosis=''
    
    #creating a button for prediction
    if st.button('Diabetes Test Result'):
        diab_pred=diabetes_model.predict([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])

        if(diab_pred[0]==1):
            diab_diagnosis='The person is diabetic'
        else:
            diab_diagnosis='The person is not diabetic'

    st.success(diab_diagnosis)       
     
        
#Heart Disease Prediction Page
if(selected=='Heart Disease Prediction'):
    
    #page title
    st.title('Heart Disease Prediction using ML')
    
    col1,col2,col3=st.columns(3)
    
    with col1:
        age=st.text_input("Age of the person")
    with col2:
        sex=st.text_input("Sex of the person")
    with col3:
        cp=st.text_input("Chest pain value")
    with col1:
        trestbps=st.text_input("resting blood pressure value")
    with col2:
        chol=st.text_input("serum cholestoral in mg/dl")
    with col3:
        fbs=st.text_input("fasting blood sugar > 120 mg/dl")
    with col1:
        restecg=st.text_input("resting electrocardiographic results (values 0,1,2)")
    with col2:
        thalach=st.text_input("maximum heart rate achieved")
    with col3:
        exang=st.text_input("exercise induced angina")
    with col1:
        oldpeak=st.text_input("oldpeak = ST depression induced by exercise relative to rest")
    with col2:
        slope=st.text_input("the slope of the peak exercise ST segment")
    with col3:
        ca=st.text_input("number of major vessels (0-3) colored by flourosopy")
    with col1:
        thal=st.text_input("thal: 0 = normal; 1 = fixed defect; 2 = reversable defect")

    
    
    #code for prediction
    
    hd_diagnosis=''
    
    #creating a button for prediction
    if st.button('Heart Disease Test Result'):
        hd_pred=heart_model.predict([age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal])

        if(hd_pred[0]==1):
            hd_diagnosis='The person has a heart disease'
        else:
            hd_diagnosis='The person does not have heart disease'

    st.success(hd_diagnosis)     

#Parkinsons Disease Prediction Page

if selected == "Parkinsons Prediction":

    # page title
    st.title("Parkinson's Disease Prediction using ML")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')

    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')

    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')

    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')

    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')

    with col1:
        RAP = st.text_input('MDVP:RAP')

    with col2:
        PPQ = st.text_input('MDVP:PPQ')

    with col3:
        DDP = st.text_input('Jitter:DDP')

    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')

    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')

    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')

    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')

    with col3:
        APQ = st.text_input('MDVP:APQ')

    with col4:
        DDA = st.text_input('Shimmer:DDA')

    with col5:
        NHR = st.text_input('NHR')

    with col1:
        HNR = st.text_input('HNR')

    with col2:
        RPDE = st.text_input('RPDE')

    with col3:
        DFA = st.text_input('DFA')

    with col4:
        spread1 = st.text_input('spread1')

    with col5:
        spread2 = st.text_input('spread2')

    with col1:
        D2 = st.text_input('D2')

    with col2:
        PPE = st.text_input('PPE')

    # code for Prediction
    parkinsons_diagnosis = ''

    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):

        user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs,
                      RAP, PPQ, DDP,Shimmer, Shimmer_dB, APQ3, APQ5,
                      APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]

        user_input = [float(x) for x in user_input]

        parkinsons_prediction = parkinsons_model.predict([user_input])

        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"

    st.success(parkinsons_diagnosis)