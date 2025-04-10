# Diabetes Prediction Web App

A machine learning-based web application that predicts whether a person has diabetes based on various health parameters.


## Overview

This application uses a trained machine learning model to predict diabetes status based on health metrics such as glucose levels, blood pressure, BMI, and other relevant factors. The model has been developed using the Pima Indians Diabetes Dataset and implemented as a user-friendly web application using Streamlit.

## Features

- Clean, user-friendly interface with interactive input controls
- Real-time prediction based on user inputs
- Input validation and appropriate value ranges
- Visual feedback on prediction results
- Responsive design that works on various screen sizes

## Project Structure

```
diabetes-prediction/
├── Diabetes_prediction_web_app.py  # Main Streamlit application
├── predictiveysystem.py            # Prediction system logic
├── diabetes_model.sav             # Saved machine learning model
├── requirements.txt               # Required dependencies
├── diabetesprediction.ipynb       # Jupyter notebook with model development
└── README.md                      # Project documentation
```

## Installation

1. Clone this repository or download the project files

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Navigate to the project directory in your terminal

2. Run the Streamlit application:
   ```
   streamlit run Diabetes_prediction_web_app.py
   ```

3. Enter the following health parameters:
   - Number of Pregnancies
   - Glucose Level
   - Blood Pressure
   - Skin Thickness
   - Insulin Level
   - BMI (Body Mass Index)
   - Diabetes Pedigree Function
   - Age

4. Click the "Diabetes Test Result" button to see the prediction

## Model Information

The application uses a Support Vector Machine (SVM) classifier trained on the Pima Indians Diabetes Dataset. The model analyzes various health metrics to predict the likelihood of diabetes.

## Requirements

- Python 3.8+
- NumPy 1.23.5
- Pandas 2.1.2
- scikit-learn 1.3.2
- Streamlit 1.31.1

## License

This project is available for personal and educational use. 
