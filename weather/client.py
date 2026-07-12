import requests


def get_hourly_weather_info(url: str, latitude: float, longitude: float) -> dict:
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "hourly": (
            "temperature_2m,"
            "apparent_temperature,"
            "precipitation_probability,"
            "weather_code"
        ),
        "temperature_unit": "fahrenheit",
        "timezone": "America/New_York",
        "forecast_days": 1,
    }

    headers: dict[str:str] = {
        "Accept": "application/json",
        "User-Agent": "UnderMyUmbrella/1.0",
    }

    response = requests.get(url, params=params, headers=headers, timeout=10)
    response.raise_for_status()
    return response.json()["hourly"]
