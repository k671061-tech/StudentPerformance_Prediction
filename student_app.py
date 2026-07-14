import streamlit as st
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# Load dataset
df = pd.read_csv(r"C:\Users\Kavita Gupta\python\.venv\student_data (2).csv")

# Features and Target
X = df.drop(["student_id", "final_grade"], axis=1)
y = df["final_grade"]

# Train model
model = DecisionTreeClassifier()
model.fit(X, y)

# Streamlit UI
st.title("Student Performance Predictor")

st.write("Enter student details to predict the final grade.")

age = st.number_input("Age", min_value=10, max_value=25)
attendance = st.number_input("Attendance Percentage", min_value=0.0, max_value=100.0)
math_score = st.number_input("Math Score", min_value=0.0, max_value=100.0)
science_score = st.number_input("Science Score", min_value=0.0, max_value=100.0)
english_score = st.number_input("English Score", min_value=0.0, max_value=100.0)
overall_score = st.number_input("Overall Score", min_value=0.0, max_value=100.0)

if st.button("Predict Grade"):
    prediction = model.predict(
        [[
            age,
            attendance,
            math_score,
            science_score,
            english_score,
            overall_score
        ]]
    )

    st.success(f"Predicted Final Grade:{prediction[0]}")           