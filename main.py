# Import the FastApi and HTTPException
from fastapi import FastAPI, HTTPException

# Import pycountry, will be used to retireve country from country code

import pycountry


# Import httpx for making external API calls

import httpx

# import load_dotenv to load the API KEY so that it can be hidden.
from dotenv import load_dotenv
import os

load_dotenv()


# Create the app
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Welcome to the Weather API! Visit /docs for documentation"}

# Storing the API Key and the OpenWeather base URL
API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# Decorator & Function


@app.get("/weather/")
async def get_weather(country: str, city: str, units: str = "metric"):

 # Validate units first

    if units not in ["metric", "imperial"]:
        raise HTTPException(
            status_code=400,
            detail="Invalid units. Use 'metric' for Celsius or 'imperial' for Fahrenheit"
        )

 # Build the request URL and call the API
    async with httpx.AsyncClient() as client:
        response = await client.get(BASE_URL, params={
            "q": f"{city}, {country}",
            "appid": API_KEY,
            "units": units
        })
 # Return the response
    data = response.json()
 # This converts the country code from API to country
    api_country_code = data["sys"]["country"]

    api_country_name = pycountry.countries.get(
        alpha_2=api_country_code
    ).name
 # This checks if the city exist
    if api_country_name.lower() != country.lower():
        raise HTTPException(
            status_code=404,
            detail=f"{city} not found in {country}"
        )

 # checks if city exist
    if data.get("cod") == "404":
        raise HTTPException(
            status_code=404,
            detail=f"{city} not found"
        )

    # check the temperature and the appropriate unit then approximate to two decimal places
    if units == "metric":
        temperature = str(round(data["main"]["temp"], 2))+"°C"
    else:
        temperature = str(round(data["main"]["temp"], 2))+"°F"

    # check the feels_likee temperature and the appropriate unit then approximate to two decimal places
    if units == "metric":
        feels_like_temp = str(round(data["main"]["feels_like"], 2))+"°C"
    else:
        feels_like_temp = str(round(data["main"]["feels_like"], 2))+"°F"

     # calculate wind_speed and approximate to two decimal places
    calc_wind_speed = round(data["wind"]["speed"] * 3.6, 2)

    return {
        "country": country,
        "city": city,
        "temperature": temperature,
        "feels_like_temperature": feels_like_temp,
        "pressure": data["main"]["pressure"],
        "humidity": data["main"]["humidity"],
        "description": data["weather"][0]["description"],
        "wind_speed": calc_wind_speed
    }
