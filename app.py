# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 23:56:20 2021

@author: Aravind S
"""

import numpy as np
import pickle
import pandas as pd
import streamlit as st

pickle_in = open("classifier.pkl","rb")
classifier = pickle.load(pickle_in)

def predictStroke(age,gender,hypertension,heart_disease,ever_married
                               ,work,residence,glucose,bmi,smoking):
    
    
    #gender
    gender_male=gender_other=0
    
    if gender=="male":
        gender_male=1
        gender_other=0
    elif gender =="female":
        gender_male=0
        gender_other=0
    elif gender=="other":
        gender_male=0
        gender_other=1
    
    #hypertension    
    if hypertension=="yes":
        hypertension=1
    else:
        hypertension=0
        
    #heart_disease
    if heart_disease == "yes":
        heart_disease=1
    else:
        heart_disease=0
    
    #ever_married
    
    if ever_married=="yes":
       ever_married=1
    else:
        ever_married=0
        
    #work_type
    
    work_n=work_pvt=work_self=work_c =0    #if work=="govt job"
    
    if work=="Private":
        work_pvt=1
    elif work=="Self-employed":
        work_self=1
    elif work=="children":
        work_c=1
    elif work=="Never worked":
        work_n=1
    
    #residence type
    residence_u=0
    if residence=="urban":
        residence_u=1
    else:
        residence_u=0
    
    #smoking
    smoke_f= smoke_n=smoke_s=0    #smoking==unknown
    
    if smoking=="never smoked":
        smoke_n=1
    elif smoking=="formerly smoked":
        smoke_f=1
    elif smoking=="smokes":
        smoke_s=1
        
    
    
    pred = classifier.predict([[age,hypertension,heart_disease,glucose,bmi,gender_male,gender_other,ever_married,work_n,work_pvt,work_self,work_c,residence_u,smoke_f,smoke_n,smoke_s]])
    
    if pred==1:
        pred = "Positive. (Seems to be having chances for a stroke)"
    else:
        pred = "Negative.(No chances for a stroke)"
    return pred
    
    
    
       
    


def main():
    st.title("Stroke Predictor")
    
    
    st.markdown("""
                <style> 
                body {
            
                    background-color: #cbeff5;
                    }
                h1 {
                    display: block;
                    font-size: 2em;
                    margin-top: 0.67em;
                    margin-bottom: 0.67em;
                    margin-left: 0;
                    margin-right: 0;
                    font-weight: bold;
                    }
                </style>
                
                """, unsafe_allow_html=True)
    




        
    st.sidebar.title("Stroke")
    st.sidebar.write("A stroke occurs when the blood supply to part of your brain is interrupted or reduced, preventing brain tissue from getting oxygen and nutrients. Brain cells begin to die in minutes. A stroke is a medical emergency, and prompt treatment is crucial.")
    st.sidebar.write("This WebApp predicts the chances of stroke with 93% precision.")
    
    age = st.number_input("Age")
    gender = st.selectbox("Gender", ["male","female","other"])
    hypertension=st.selectbox("Hypertension",["yes","no"])
    heart_disease = st.selectbox("Heart Disease",["yes","no"])
    ever_married = st.selectbox("Ever married",["yes","no"])
    work = st.selectbox("Work type",["Private","Self-employed","children","Govt job","Never worked"])
    residence = st.selectbox("Residence type",["urban","rural"])
    glucose = st.number_input("Average glucose level")
    bmi = st.number_input("BMI")
    smoking = st.selectbox("Smoking status",["never smoked","formerly smoked","smokes","Unknown"])
    
    result = ''
    
    if st.button("Predict"):
        result = predictStroke(age,gender,hypertension,heart_disease,ever_married
                               ,work,residence,glucose,bmi,smoking)
    
    st.success('RESULT : {}'.format(result))
    
    if st.button("About"):
        st.write("Developed by : Aravind S")
        





if __name__=='__main__':
    main()