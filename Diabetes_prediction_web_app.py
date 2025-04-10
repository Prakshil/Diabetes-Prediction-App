import numpy as np
import pickle
import streamlit as st
import os

# loading the saved model
model_path = os.path.join(os.path.dirname(__file__), 'diabetes_model.sav')
loaded_model = pickle.load(open(model_path, 'rb'))

def diabetes_prediction(input_data):
    try:
        # changing the input_data to numpy array
        input_data_as_numpy_array = np.asarray(input_data, dtype=float)

        # reshape the array as we are predicting for one instance
        input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

        prediction = loaded_model.predict(input_data_reshaped)
        
        if (prediction[0] == 0):
            return 'The person is not diabetic'
        else:
            return 'The person is diabetic'
    except Exception as e:
        return f'Error in prediction: {str(e)}'
  
def main():
    st.title('Diabetes Prediction Web App')
    st.write('Please enter the following details:')
    
    # getting the input data from the user with number inputs
    col1, col2 = st.columns(2)
    
    with col1:
        Pregnancies = st.number_input('Number of Pregnancies', min_value=0, max_value=20, value=0)
        Glucose = st.number_input('Glucose Level', min_value=0, max_value=200, value=100)
        BloodPressure = st.number_input('Blood Pressure value', min_value=0, max_value=200, value=70)
        SkinThickness = st.number_input('Skin Thickness value', min_value=0, max_value=100, value=20)
    
    with col2:
        Insulin = st.number_input('Insulin Level', min_value=0, max_value=1000, value=80)
        BMI = st.number_input('BMI value', min_value=0.0, max_value=100.0, value=25.0, step=0.1)
        DiabetesPedigreeFunction = st.number_input('Diabetes Pedigree Function value', min_value=0.0, max_value=2.5, value=0.5, step=0.01)
        Age = st.number_input('Age of the Person', min_value=0, max_value=120, value=30)
    
    # code for Prediction
    diagnosis = ''
    
    # creating a button for Prediction
    if st.button('Diabetes Test Result'):
        diagnosis = diabetes_prediction([Pregnancies, Glucose, BloodPressure, SkinThickness, 
                                       Insulin, BMI, DiabetesPedigreeFunction, Age])
        
    if diagnosis:
        if 'not diabetic' in diagnosis:
            st.success(diagnosis)
        else:
            st.error(diagnosis)
    
if __name__ == '__main__':
    main()
    
