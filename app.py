import streamlit as st
import pandas as pd
import joblib as jl
model = jl.load("model.pkl")
scaler = jl.load("scaler.pkl")
columns = jl.load("columns.pkl")
st.title("Heart Failure Predictor")
st.markdown("Provide the following details to check your heart failure risk:")
age = st.slider("Age", 18, 100, 50)
anaemia = st.selectbox("Anaemia", [0, 1])
creatinine_phosphokinase = st.number_input("Creatinine Phosphokinase (mcg/L)", 0, 10000, 100)
diabetes = st.selectbox("Diabetes", [0, 1])
ejection_fraction = st.slider("Ejection Fraction (%)", 10, 80, 50)
high_blood_pressure = st.selectbox("High Blood Pressure", [0, 1])
platelets = st.number_input("Platelets (kiloplatelets/mL)", 100000, 1000000, 250000)
serum_creatinine = st.number_input("Serum Creatinine (mg/dL)", 0.1, 10.0, 1.0, step=0.1)
serum_sodium = st.number_input("Serum Sodium (mEq/L)", 100, 160, 140)
sex = st.radio("Sex", [0, 1])
smoking = st.selectbox("Smoking", [0, 1])
time = st.slider("Follow-up Period (days)", 0, 500, 100)
input_df = pd.DataFrame([{
    'age': age,
    'creatinine_phosphokinase': creatinine_phosphokinase,
    'ejection_fraction': ejection_fraction,
    'platelets': platelets,
    'serum_creatinine': serum_creatinine,
    'serum_sodium': serum_sodium,
    'time': time,
    'anaemia': anaemia,
    'diabetes': diabetes,
    'high_blood_pressure': high_blood_pressure,
    'sex': sex,
    'smoking': smoking
}])
numerical_columns = ['age','creatinine_phosphokinase','ejection_fraction','platelets','serum_creatinine','serum_sodium','time']
categorical_columns = ['anaemia','diabetes','high_blood_pressure','sex','smoking']
input_df[numerical_columns] = scaler.transform(input_df[numerical_columns])
for col in categorical_columns:
    input_df[col] = input_df[col].values
input_df = input_df[columns]
if st.button("Predict"):
    prediction = model.predict(input_df)[0]
    if prediction == 1:
        st.error("⚠️ High Risk of Heart Disease")
    else:
        st.success("✅ Low Risk of Heart Disease")
