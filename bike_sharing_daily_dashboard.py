
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import joblib


df = pd.read_csv('bike_sharing_daily.csv')
bike_sharing_daily_model = joblib.load('bike_sharing_daily_model.p')
sc = StandardScaler()

# Setting page configuration
st.set_page_config(page_title="Bike Sharing Daily Count", page_icon="💹", layout='wide')

# page title
st.title("Bike Sharing Daily Count")
# Inputs 
col1, col2 = st.columns((5,5))

with col1:

    season= st.selectbox("season", options=['winter', 'spring', 'summer', 'fall'])
    season = {'winter': 1, 'spring': 2, 'summer': 3, 'fall': 4}.get(season, season)
    
    Month= int(st.selectbox("Month", options=df['mnth'].unique()))
    WeekDay= int(st.selectbox("WeekDay", options=df['weekday'].unique()))
    
    WeatherSit= st.selectbox("WeatherSit", options=['Clear, Few clouds', 'Mist + Cloudy', 'Light Snow, Light Rain', 'Heavy Rain, Snow + Fog'] )
    WeatherSit = {'Clear, Few clouds': 1, 'Mist + Cloudy': 2, 'Light Snow, Light Rain': 3, 'Heavy Rain, Snow + Fog': 4}.get(WeatherSit, WeatherSit)

    WorkingDay= st.radio("IS WorkingDay?", options=['Weekend or Holiday', 'Workday'])
    WorkingDay = {'Weekend or Holiday': 0, 'Workday': 1}.get(WorkingDay, WorkingDay)






with col2:

    Holiday= st.radio("IS Holiday?", options=['Holiday', 'Not Holiday'])
    Holiday = {'Holiday': 1, 'Not Holiday': 0}.get(Holiday, Holiday)
    
    Temperature = (st.number_input("Temperature", step=1.0) + 8) / (39 + 8)
    Humidity = st.number_input("Humidity", step=1.0)/100

    Wind_Speed = st.number_input("Wind Speed", step=1.0)/67
    
    Casual = st.number_input("Casual", step=1.0)
    Registered = st.number_input("Registered", step=1.0)


with st.sidebar:
    # Add the image to the sidebar
    st.image('Bicycle-sharing_systems.png', use_column_width=True)
    st.sidebar.subheader('The daily count of rental bike transactions in Capital bikeshare system with the corresponding weather and seasonal information prediction.')
    st.sidebar.write("")

    # Submit Button
    if st.button("Submit"):
        count = bike_sharing_daily_model.predict([[season, Month, Holiday, WeekDay, WorkingDay, WeatherSit,
                                                 Temperature, Humidity, Wind_Speed, Casual, Registered]])
        st.write('count of total rental bikes:', count)  
        