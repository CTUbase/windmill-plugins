from io import BytesIO
import requests
from pyvi import ViTokenizer, ViPosTagger
import string
import joblib
import numpy as np
import pandas as pd
from analyze_data import create_input


with open('input.txt', 'r', encoding='utf-8') as file:
    article = file.read()

data = create_input(article)

model = joblib.load('models/best_decision_tree_model.joblib')
# Convert the data dictionary to a DataFrame with appropriate feature names
data_df = pd.DataFrame([{
    'death': data['deaths'],
    'injuries': data['injuries'],
    'property_large': data['property'][0],
    'property_medium': data['property'][1],
    'property_small': data['property'][2],
    'keyword': data['keyword']
}])

# Make the prediction
prediction = model.predict(data_df)
print(f"Muc do du doan: {prediction[0]}")