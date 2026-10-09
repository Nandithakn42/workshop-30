# pip install requests

import requests


def get_weather(lat, lon):
    url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={lat}&longitude={lon}&current_weather=true"
    )

    res = requests.get(url)

    # Error handling
    if res.status_code == 200:
        return res.json()
    else:
        print("API failed with status:", res.status_code)
        return None


# Get latitude and longitude from the user
lat = float(input("Enter latitude: "))
lon = float(input("Enter longitude: "))

# Get weather data
weather_data = get_weather(lat, lon)

# Display weather information
if weather_data:
    current_weather = weather_data["current_weather"]

    print("\nCurrent Weather")
    print("-------------------------")
    print("Temperature:", current_weather["temperature"], "°C")
    print("Wind Speed:", current_weather["windspeed"], "km/h")
    print("Wind Direction:", current_weather["winddirection"], "°")
    print("Weather Code:", current_weather["weathercode"])
    print("Time:", current_weather["time"])
    