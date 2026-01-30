from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()

class OpenMeteoProvider:
    def get_weather(self, lat: float, lon: float):
        url = (
            "https://api.open-meteo.com/v1/forecast"
            f"?latitude={lat}&longitude={lon}"
            "&current=temperature_2m,relative_humidity_2m,wind_speed_10m"
        )

        response = requests.get(url)

        if response.status_code != 200:
            raise HTTPException(status_code=500, detail="Error: Wrong input!")

        data = response.json()
        current = data["current"]

        if not current:
            raise HTTPException(status_code=500, detail="No data found!")

        return {
            "temperature": current["temperature_2m"],
            "humidity": current["relative_humidity_2m"],
            "wind_speed": current["wind_speed_10m"]
        }


class OpenWeatherProvider:
    def __init__(self):
        self.api_key = "b3b4adb945eb97ff43dfbd1a14f49fd9"
        self.base_url = "https://api.openweathermap.org/data/2.5/weather"

    def get_weather(self, lat: float, lon: float):
        url = (
            f"{self.base_url}"
            f"?lat={lat}&lon={lon}"
            f"&appid={self.api_key}"
            f"&units=metric"
        )

        response = requests.get(url)
        if response.status_code != 200:
            raise HTTPException(status_code=500, detail="Error: Wrong input!")

        data = response.json()

        return {
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"]
        }


@app.get("/weather")
def get_weather(lat: float, lon: float, provider: str):

    if provider == "openmeteo":
        service = OpenMeteoProvider()
    elif provider == "openweather":
        service = OpenWeatherProvider()
    else:
        raise HTTPException(
            status_code=400,
            detail="provider is invalid."
        )

    return service.get_weather(lat, lon)