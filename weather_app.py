import requests
from dotenv import load_dotenv
import os
import tkinter as tk
from tkinter import messagebox

# Load environment variables from .env file
load_dotenv()

# Retrieve the API key from the environment variable
api_key = os.getenv("OPENWEATHER_API_KEY")

# Function to get the weather for a given city
def get_weather():
    city = city_entry.get()  # Get the city name from the entry box
    if not city:
        messagebox.showerror("Input Error", "Please enter a city name.")
        return

    # Build the API request URL
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        weather_description = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        
        # Display the results in the result_label
        result_label.config(text=f"Weather in {city}: {weather_description}\nTemperature: {temperature}°C")
    else:
        messagebox.showerror("Error", f"Error: {response.status_code}\n{response.json()['message']}")

# Set up the main application window
root = tk.Tk()
root.title("Weather App")
root.geometry("400x300")

# Set up UI components
city_label = tk.Label(root, text="Enter city name:")
city_label.pack(pady=10)

city_entry = tk.Entry(root, width=30)
city_entry.pack(pady=5)

get_weather_button = tk.Button(root, text="Get Weather", command=get_weather)
get_weather_button.pack(pady=20)

result_label = tk.Label(root, text="Weather information will be displayed here.", justify="left")
result_label.pack(pady=10)

# Start the application
root.mainloop()
