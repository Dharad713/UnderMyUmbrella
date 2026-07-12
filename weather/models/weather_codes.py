from typing import TypedDict


class WeatherInfo(TypedDict):
    description: str
    category: str
    severity: int
    notable: bool


UNKNOWN_WEATHER: WeatherInfo = {
    "description": "Unknown weather condition",
    "category": "unknown",
    "severity": 0,
    "notable": False,
}


WEATHER_CODES: dict[int, WeatherInfo] = {
    0: {
        "description": "Clear sky",
        "category": "clear",
        "severity": 0,
        "notable": False,
    },
    1: {
        "description": "Mostly clear",
        "category": "clear",
        "severity": 0,
        "notable": False,
    },
    2: {
        "description": "Partly cloudy",
        "category": "cloudy",
        "severity": 0,
        "notable": False,
    },
    3: {
        "description": "Overcast",
        "category": "cloudy",
        "severity": 0,
        "notable": False,
    },
    45: {
        "description": "Fog",
        "category": "fog",
        "severity": 1,
        "notable": True,
    },
    61: {
        "description": "Light rain",
        "category": "rain",
        "severity": 1,
        "notable": True,
    },
    63: {
        "description": "Moderate rain",
        "category": "rain",
        "severity": 2,
        "notable": True,
    },
    65: {
        "description": "Heavy rain",
        "category": "rain",
        "severity": 3,
        "notable": True,
    },
    95: {
        "description": "Thunderstorm",
        "category": "thunderstorm",
        "severity": 3,
        "notable": True,
    },
}


def get_weather_info(code: int) -> WeatherInfo:
    return WEATHER_CODES.get(code, UNKNOWN_WEATHER)
