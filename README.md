# 🫀 Heart Failure Prediction App

This project is a **Machine Learning-based Heart Failure Prediction System** built with **Python, Scikit-learn, and Streamlit**.  
It uses the **Heart Failure Clinical Records Dataset** to train models and predict whether a patient is at high risk of heart failure.

---

## 🚀 Project Overview
The project has two main parts:

1. **Model Training (`train_model.py`)**  
   - Performs Exploratory Data Analysis (EDA)  
   - Cleans and preprocesses the dataset  
   - Trains multiple ML models (Logistic Regression, KNN, Naive Bayes, Decision Tree, SVM)  
   - Evaluates models using Accuracy & F1 Score  
   - Saves the best model (`model.pkl`), scaler (`scaler.pkl`), and column names (`columns.pkl`)  

2. **Web App (`app.py`)**  
   - Built with **Streamlit**  
   - Takes patient details as input  
   - Preprocesses the input using the saved scaler  
   - Predicts Heart Failure Risk using the trained Logistic Regression model  
   - Shows results as:
     - ⚠️ High Risk of Heart Disease  
     - ✅ Low Risk of Heart Disease  

---

## 📊 Dataset
- **File**: `heart_failure_clinical_records_dataset.csv`  
- **Rows**: 299 patients  
- **Target Variable**: `DEATH_EVENT` (1 = death, 0 = survival)  
- **Features**:  
  - Age, Anaemia, Diabetes, High Blood Pressure, Sex, Smoking  
  - Creatinine Phosphokinase, Ejection Fraction, Platelets, Serum Creatinine, Serum Sodium, Follow-up Time  

---

## ⚙️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/heart-failure-predictor.git
   cd heart-failure-predictor
