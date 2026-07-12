import os

from dotenv import load_dotenv

load_dotenv()

WEATHER_API_URL = "https://api.open-meteo.com/v1/forecast"

HOME_LATITUDE: float = float(os.getenv("HOME_LAT"))
HOME_LONGITUDE: float = float(os.getenv("HOME_LONG"))

MIN_REASONABLE_TEMP: int = 45
MAX_REASONABLE_TEMP: int = 85
RAIN_CHANCE_THRESHOLD: int = 30
PHONE_NUMBER: str = str(os.getenv("PHONE_NUMBER"))
API_KEY: str = str(os.getenv("TEXTBELT_API_KEY"))
