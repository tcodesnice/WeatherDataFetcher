import requests
import urllib.parse
import datetime  # Import the datetime module to work with dates

# Set your API keys
openweather_api_key = 'ENTER API KEY'
geocoding_api_key = 'ENTER API KEY'

# Function to get latitude and longitude coordinates for a given location (city or zip code)
def get_coordinates(location):
    geocoding_url = f"https://maps.googleapis.com/maps/api/geocode/json?address={location}&key={geocoding_api_key}"
    response = requests.get(geocoding_url)
    
    if response.status_code == 200:
        data = response.json()
        if data['status'] == 'OK':
            result = data['results'][0]
            lat = result['geometry']['location']['lat']
            lon = result['geometry']['location']['lng']
            return lat, lon
        else:
            raise Exception(f"Geocoding API failed with status: {data['status']}")
    else:
        raise Exception(f"Geocoding API request failed with status code {response.status_code}")

# Ask the user to enter a city name or zip code
location = input("Enter a city name or zip code: ")

# Ask the user to enter a specific date in 'YYYY-MM-DD' format
date = input("Enter a specific date (YYYY-MM-DD): ")

try:
    # Get coordinates for the entered location
    lat, lon = get_coordinates(location)

    # Encode values
    encoded_lat = urllib.parse.quote(str(lat))
    encoded_lon = urllib.parse.quote(str(lon))
    encoded_date = urllib.parse.quote(date)
    encoded_api_key = urllib.parse.quote(openweather_api_key)

    # Modify units to 'imperial' for Fahrenheit
    units = 'imperial'
    
    # Construct the OpenWeatherMap API request URL with encoded parameters
    weather_url = f"https://api.openweathermap.org/data/3.0/onecall/day_summary?lat={encoded_lat}&lon={encoded_lon}&date={encoded_date}&appid={encoded_api_key}&units={units}"

    # Make the OpenWeatherMap API request and handle the response
    response = requests.get(weather_url)

    if response.status_code == 200:
        data = response.json()
        print(data)
    else:
        print(f"OpenWeatherMap API request failed with status code {response.status_code}")

except Exception as e:
    print(f"An error occurred: {e}")

