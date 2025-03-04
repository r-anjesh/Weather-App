import streamlit as st
import requests

# OpenWeatherMap API Key
API_KEY = '8478264ca5909e799f926ce0a2afa969'  # Replace with your actual API key

# Function to fetch current weather data from OpenWeatherMap API
def get_weather(city_name):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city_name}&appid={API_KEY}&units=metric"
    response = requests.get(complete_url)
    return response.json()

# Function to fetch 5-day weather forecast data
def get_forecast(city_name):
    base_url = "http://api.openweathermap.org/data/2.5/forecast?"
    complete_url = f"{base_url}q={city_name}&appid={API_KEY}&units=metric"
    response = requests.get(complete_url)
    return response.json()

# Streamlit app
def app():
    st.title("Weather Dashboard")
    
    # User input for city
    city = st.text_input("Enter city name:")
    
    if city:
        weather_data = get_weather(city)
        if weather_data.get('cod') != 200:
            st.error("City not found, please try again.")
        else:
            st.subheader(f"Weather in {city}")
            st.write(f"**Temperature**: {weather_data['main']['temp']} °C")
            st.write(f"**Description**: {weather_data['weather'][0]['description']}")
            st.write(f"**Humidity**: {weather_data['main']['humidity']}%")
            st.write(f"**Wind Speed**: {weather_data['wind']['speed']} m/s")
            
            # Fetch and display 5-day forecast
            forecast_data = get_forecast(city)
            st.subheader("5-Day Forecast")
            
            for entry in forecast_data['list']:
                st.write(f"Date: {entry['dt_txt']}")
                st.write(f"Temperature: {entry['main']['temp']} °C")
                st.write(f"Description: {entry['weather'][0]['description']}")
                st.write("-" * 30)

if __name__ == "__main__":
    app()
