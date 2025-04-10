import numpy as np
import pickle

# Load the model
model_path ="C:/Users/Prakshil/OneDrive/Desktop/deploy/tained_model.sav" 
with open(model_path, 'rb') as file:
    loaded_model = pickle.load(file)

# Input data
input_data = (5, 166, 72, 19, 175, 25.8, 0.587, 51)

# Preprocess the input
input_data_as_numpy_array = np.asarray(input_data)
input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

# Make prediction
prediction = loaded_model.predict(input_data_reshaped)

# Output results
if prediction[0] == 0:
    print("The person is not diabetic")
else:
    print("The person is diabetic")
