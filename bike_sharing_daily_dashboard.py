
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import joblib


df = pd.read_csv(r'C:\Users\engmi\Desktop\Data Science\data_science_diploma\Machine Learning Course\interactive\Model Selection\bike_sharing_daily\bike_sharing_daily.csv')
bike_sharing_daily_model = joblib.load(r'C:\Users\engmi\Desktop\Data Science\data_science_diploma\Machine Learning Course\interactive\Model Selection\bike_sharing_daily\bike_sharing_daily_model.p')
sc = StandardScaler()

# page title
st.title("Bike Sharing Daily Price")
# Inputs 
col1, col2 = st.columns((5,5))
with col1:
    season= int(st.selectbox("season", options=df['season'].unique()))
    Year= int(st.selectbox("Year", options=df['yr'].unique()))
    Month= int(st.selectbox("Month", options=df['mnth'].unique()))
    Holiday= st.radio("IS Holiday", options=df['holiday'].unique())
    WorkingDay= int(st.radio("IS WorkingDay", options=df['workingday'].unique()))
    WeekDay= int(st.selectbox("WeekDay", options=df['weekday'].unique()))

with col2:
    WeatherSit= int(st.selectbox("WeatherSit", options=df['weathersit'].unique()))
    Temperature = sc.fit_transform([[st.number_input("Temperature")]])
    Humidity = sc.fit_transform([[st.number_input("Humidity")]])
    Wind_Speed = sc.fit_transform([[st.number_input("Wind Speed")]])
    Casual = sc.fit_transform([[st.number_input("Casual")]])
    Registered = sc.fit_transform([[st.number_input("Registered")]])

# Submit Button
if st.button("Submit"):
    price = bike_sharing_daily_model.predict([[season, Year, Month, Holiday, WeekDay, WorkingDay, WeatherSit,
                                                 Temperature[0][0], Humidity[0][0], Wind_Speed[0][0],
                                                 Casual[0][0], Registered[0][0]]])
    st.write('The price in cent:', price)  