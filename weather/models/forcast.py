from dataclasses import dataclass
from datetime import datetime


@dataclass
class DailyWeatherSummary:
    date: str
    low: float
    high: float
    max_feels_like: float
    max_rain_chance: int
    rain_start: datetime | None
    rain_end: datetime | None
    worst_condition: str
    recommendation: str


@dataclass
class HourlyForecast:
    time: datetime
    temperature: float
    feels_like: float
    rain_chance: int
    weather_code: int
    condition: str
    category: str
    severity: int
    temperature_is_reasonable: bool
    rain_is_likely: bool
    notable_weather: bool
