import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load("cricket_runs_prediction_model.pkl")

st.set_page_config(page_title="Cricket Runs Prediction", page_icon="🏏")

st.title("🏏 Cricket Runs Prediction")
st.write("Enter the match details below.")

match = st.number_input("Match", value=101)

batsman = st.number_input("Batsman", value=15)

batting_team = st.number_input("Batting Team", value=2)

bowling_team = st.number_input("Bowling Team", value=3)

venue = st.number_input("Venue", value=1)

over = st.slider("Over", 1, 20, 10)

wickets = st.slider("Wickets", 0, 10, 2)

current_run_rate = st.number_input("Current Run Rate", value=8.4)

powerplay = st.selectbox("Powerplay", [0, 1])

if st.button("Predict Runs"):

    sample = pd.DataFrame({
        "Match": [match],
        "Batsman": [batsman],
        "Batting_Team": [batting_team],
        "Bowling_Team": [bowling_team],
        "Venue": [venue],
        "Over": [over],
        "Wickets": [wickets],
        "Current_Run_Rate": [current_run_rate],
        "Powerplay": [powerplay]
    })

    prediction = model.predict(sample)

    st.success(f"🏏 Predicted Runs: {prediction[0]:.2f}")