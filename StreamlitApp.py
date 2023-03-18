import pickle
import streamlit as st


#Loading the model
HeartDisease_model = pickle.load(open('HeartDisease_model.sav', 'rb'))
    
# page title
st.title('Heart Disease Prediction')
    
# create a dictionary of feature descriptions
feature_descriptions = {
    'Sex': '1: male, 0: female',
    'Chest pain type': '1 = typical angina, 2 = atypical angina, 3 = non-anginal pain, 4 = asymptomatic',
    'Resting blood pressure': '(in mm Hg)',
    'Serum cholesterol level': '(in mg/dl)',
    'Fasting blood sugar level': '(> 120 mg/dl or not)',
    'Resting electrocardiographic results': 'normal: 0, ST-T wave abnormality: 1, left ventricular hypertrophy: 2',
    'Maximum heart rate achieved': '',
    'Exercise-induced angina': '(yes: 1 or no: 0)',
    'ST depression': 'ST depression induced by exercise relative to rest',
    'slope': 'The slope of the peak exercise ST segment: upsloping; 1, flat: 2, downsloping: 3',
    'ca': 'Number of major vessels (0-3) colored by flourosopy',
    'Thalassemia': 'normal: 0, fixed defect: 1, reversable defect: 2'
}

# create a sidebar with feature descriptions
st.sidebar.header("Feature Descriptions")
for feature in feature_descriptions:
    st.sidebar.subheader(feature)
    st.sidebar.write(feature_descriptions[feature])

# getting the input data from the user
col1, col2, col3= st.columns(3)
    
with col1:
    age = st.text_input('Age')
        
with col2:
    sex = st.text_input('Sex')

with col3:
    cp = st.text_input('Chest pain type')
    
with col1:
    trestbps = st.text_input('Resting blood pressure')
    
with col2:
    chol = st.text_input('Serum cholesterol level')
    
with col3:
    fbs = st.text_input('Fasting blood sugar level')
    
with col1:
    restecg = st.text_input('Resting electrocardiographic')
    
with col2:
    thalach = st.text_input('Maximum heart rate achieved')

with col3:
    exang = st.text_input('Exercise-induced angina')

with col1:
    oldpeak = st.text_input('ST depression')
    
with col2:
    slope = st.text_input('Slope')
    
with col3:
    ca = st.text_input('Number of major vessels')
    
with col1:
    thal = st.text_input('Thalassemia')    

# code for Prediction
HeartDisease_diagnosis = ''
    
# creating a button for Prediction
    
if st.button('Heart Disease Test Result'):
    HeartDisease_prediction = HeartDisease_model.predict([[age, sex, cp, trestbps, chol, fbs,	restecg, thalach, exang, oldpeak, slope, ca, thal]])
        
    if (HeartDisease_prediction == 1):
        HeartDisease_diagnosis = 'This person have a heart disease'
    else:
        HeartDisease_diagnosis = 'The person have not a heart disease'
        
st.success(HeartDisease_diagnosis)
    