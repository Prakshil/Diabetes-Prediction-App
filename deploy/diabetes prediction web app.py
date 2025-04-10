# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 23:00:34 2024

@author: Prakshil
"""

import numpy as np
import pickle
import streamlit as st

loaded_model=pickle.load(open("C:\Users\Prakshil\OneDrive\Desktop\deploy\tained_model.sav"))

def diabeted_prediction(input_data):
    # Convert to numpy array
    input_data_as_numpy_array = np.asarray(input_data)
    # Reshape for a single instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
    # Predict
    prediction = loaded_model.predict(input_data_reshaped)
    if prediction[0] == 0:
        return 'The person is not diabetic'
    else:
        return 'The person is diabetic'
  
def main():
    st.title('diabetes prediction web app')
    
    Pregnancies = int(st.text_input("Number of Pregnancies", "0"))
    Glucose = float(st.text_input("Glucose Level", "0"))
    BloodPressure = float(st.text_input("Pressure Level", "0"))
    SkinThickness = float(st.text_input("Skin Thickness Value", "0"))
    Insulin = float(st.text_input("Insulin Value", "0"))
    BMI = float(st.text_input("BMI Value", "0"))
    DiabetesPedigreeFunction = float(st.text_input("Diabetes Pedigree Function Value", "0"))
    Age = int(st.text_input("Age of Person", "0"))

    
    diagnosis=''
    if st.button('Diabetes Test Result'):
        diagnosis=diabeted_prediction([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age])
    st.success(diagnosis)
if __name__=='__main__':
    main()
        
    