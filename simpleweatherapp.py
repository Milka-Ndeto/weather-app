import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the API key from environment variables
api_key = os.getenv("OPENWEATHER_API_KEY")

# Function to fetch the weather data
def get_weather():
    city = input("Enter city name: ")  # Get the city name from the user
    if not city:
        print("Please enter a city name.")
        return

    # Build the API URL
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    # Fetch data from OpenWeatherMap
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        weather_description = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        
        # Display the results
        print(f"Weather in {city}: {weather_description}")
        print(f"Temperature: {temperature}°C")
    else:
        print(f"Error: {response.status_code}\n{response.json()['message']}")

# Call the function to get weather info
get_weather()
