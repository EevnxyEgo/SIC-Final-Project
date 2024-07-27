import streamlit as st
import requests
import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image

API_URL = 'http://localhost:5000/api/predict'
DATA_URL = 'http://localhost:5000/api/data'

# title and logo
st.title("Asthma Attack Prediction Dashboard")
st.image("./additional/logo.jpeg", width=200)  # Replace 'your_logo.png' with your logo file

# Sidebar
st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", ["Prediction Form", "Sensor Data Trends", "Prediction Trends"])


def prediction_form():
    st.write("### Predict Asthma Attack Likelihood")
    
    with st.form(key='sensor_form'):
        st.subheader("Enter Sensor Data")
        temperature = st.number_input("Temperature (°C)", min_value=-50.0, max_value=50.0, step=0.1)
        humidity = st.number_input("Humidity (%)", min_value=0.0, max_value=100.0, step=0.1)
        air_quality = st.number_input("Air Quality (AQI)", min_value=0, max_value=5000, step=1)
        
        submit_button = st.form_submit_button(label='Submit')
        
        if submit_button:
            sensor_data = {
                'temperature': temperature,
                'humidity': humidity,
                'airQuality': air_quality
            }
            
            try:
                response = requests.post(API_URL, json=sensor_data)
                if response.status_code == 200:
                    result = response.json()
                    prediction = result['asthma_attack']
                    st.success(f"Prediction: {'Asthma Attack Detected' if prediction == 1 else 'No Asthma Attack Detected'}")
                else:
                    st.error(f"Failed to get prediction. Status code: {response.status_code}")
            except Exception as e:
                st.error(f"Error occurred: {e}")

def sensor_data_trends():
    st.write("### Sensor Data Trends")
    
    try:
        data_response = requests.get(DATA_URL)
        if data_response.status_code == 200:
            data = data_response.json()
            df = pd.DataFrame(data)

            if 'timestamp' in df.columns:
                df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')
                df.set_index('timestamp', inplace=True)
                
                # bagi kolom
                col1, col2 = st.columns(2)

                with col1:
                    st.subheader("Temperature Trend")
                    if not df.empty:
                        st.line_chart(df['temperature'], use_container_width=True)

                with col2:
                    st.subheader("Humidity Trend")
                    if not df.empty:
                        st.line_chart(df['humidity'], use_container_width=True)

                st.subheader("Air Quality Trend")
                if not df.empty:
                    st.line_chart(df['airQuality'], use_container_width=True)
            else:
                st.error("Timestamp column is missing in the sensor data.")
        else:
            st.error(f"Failed to get data. Status code: {data_response.status_code}")
    except Exception as e:
        st.error(f"Error occurred: {e}")

def prediction_trends():
    st.write("### Prediction Trends")
    
    try:
        data_response = requests.get(DATA_URL)
        if data_response.status_code == 200:
            data = data_response.json()
            df = pd.DataFrame(data)

            if 'timestamp' in df.columns:
                df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')
                df.set_index('timestamp', inplace=True)

                st.subheader("Prediction Trends")
                if 'asthma_attack' in df.columns:
                    st.write(df[['temperature', 'humidity', 'airQuality', 'asthma_attack']].tail())

                    st.subheader("Prediction Occurrences Over Time")
                    st.bar_chart(df['asthma_attack'].resample('D').sum(), use_container_width=True)
                else:
                    st.warning("No prediction data available in the recent records.")
            else:
                st.error("Timestamp column is missing in the sensor data.")
        else:
            st.error(f"Failed to get data. Status code: {data_response.status_code}")
    except Exception as e:
        st.error(f"Error occurred: {e}")

# sidebar
if selection == "Prediction Form":
    prediction_form()
elif selection == "Sensor Data Trends":
    sensor_data_trends()
elif selection == "Prediction Trends":
    prediction_trends()

# styling
st.markdown("""
<style>
    .css-18e3th9 {
        background-color: #f4f4f4;
    }
    .css-1y6a5tx {
        color: #333;
    }
</style>
""", unsafe_allow_html=True)
