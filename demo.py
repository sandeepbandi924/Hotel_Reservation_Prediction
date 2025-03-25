import joblib
import numpy as np
import streamlit as st
from config.paths_config import MODEL_OUTPUT_PATH

# Load the model
loaded_model = joblib.load(MODEL_OUTPUT_PATH)

# Streamlit app
st.title("Hotel Reservation Prediction")

# User inputs
lead_time = st.number_input("Lead Time", min_value=0, step=1)
no_of_special_request = st.number_input("Number of Special Requests", min_value=0, step=1)
avg_price_per_room = st.number_input("Average Price per Room", min_value=0.0, step=0.01)
arrival_month = st.selectbox("Arrival Month", list(range(1, 13)), format_func=lambda x: ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"][x-1])
arrival_date = st.selectbox("Arrival Date", list(range(1, 32)))

market_segment_type = st.selectbox("Market Segment Type", [0, 1, 2, 3, 4], format_func=lambda x: ["Aviation", "Complimentary", "Corporate", "Offline", "Online"][x])
no_of_week_nights = st.number_input("Number of Week Nights", min_value=0, step=1)
no_of_weekend_nights = st.number_input("Number of Weekend Nights", min_value=0, step=1)

type_of_meal_plan = st.selectbox("Type of Meal Plan", [0, 1, 2, 3], format_func=lambda x: ["Meal Plan 1", "Meal Plan 2", "Meal Plan 3", "Not Selected"][x])
room_type_reserved = st.selectbox("Room Type Reserved", [0, 1, 2, 3, 4, 5, 6], format_func=lambda x: ["Room Type 1", "Room Type 2", "Room Type 3", "Room Type 4", "Room Type 5", "Room Type 6", "Room Type 7"][x])

# Predict button
if st.button("Predict"):
    features = np.array([[lead_time, no_of_special_request, avg_price_per_room, arrival_month, arrival_date, market_segment_type, no_of_week_nights, no_of_weekend_nights, type_of_meal_plan, room_type_reserved]])
    prediction = loaded_model.predict(features)[0]
    
    if prediction == 0:
        st.error("The Customer is going to cancel their reservation.")
    else:
        st.success("The Customer is not going to cancel their reservation.")
