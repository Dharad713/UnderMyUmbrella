import os

from dotenv import load_dotenv

load_dotenv()


def get_required_setting(name: str) -> str:
    value = os.getenv(name)

    if not value:
        raise RuntimeError(f"Required environment variable {name} is missing.")

    return value


WEATHER_API_URL = "https://api.open-meteo.com/v1/forecast"

HOME_LATITUDE = float(get_required_setting("HOME_LAT"))
HOME_LONGITUDE = float(get_required_setting("HOME_LONG"))
PHONE_NUMBER = get_required_setting("PHONE_NUMBER")
API_KEY: str = str(get_required_setting("TEXTBELT_API_KEY"))

MIN_REASONABLE_TEMP: int = 45
MAX_REASONABLE_TEMP: int = 85
RAIN_CHANCE_THRESHOLD: int = 30