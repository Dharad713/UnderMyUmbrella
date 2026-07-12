from datetime import datetime
from weather.config import (
    MAX_REASONABLE_TEMP,
    MIN_REASONABLE_TEMP,
    RAIN_CHANCE_THRESHOLD,
)
from weather.models.weather_codes import get_weather_info
from weather.models.forecast import DailyWeatherSummary, HourlyForecast


def get_hourly_forecast(hourly: dict) -> list[HourlyForecast]:
    hourly_forecast: list[HourlyForecast] = []

    weather_zip = zip(
        hourly["time"],
        hourly["temperature_2m"],
        hourly["apparent_temperature"],
        hourly["precipitation_probability"],
        hourly["weather_code"],
    )

    for (
        time,
        temperature,
        feels_like,
        rain_chance,
        weather_code,
    ) in weather_zip:
        forecast_time = datetime.fromisoformat(time)

        # Only include hours from 6:00 AM through 11:00 PM.
        if not 6 <= forecast_time.hour <= 23:
            continue

        temperature_is_reasonable = (
            MIN_REASONABLE_TEMP <= feels_like <= MAX_REASONABLE_TEMP
        )

        rain_is_likely = rain_chance >= RAIN_CHANCE_THRESHOLD

        weather_info = get_weather_info(weather_code)

        forecast = HourlyForecast(
            time=forecast_time,
            temperature=temperature,
            feels_like=feels_like,
            rain_chance=rain_chance,
            weather_code=weather_code,
            condition=weather_info["description"],
            category=weather_info["category"],
            severity=weather_info["severity"],
            temperature_is_reasonable=temperature_is_reasonable,
            rain_is_likely=rain_is_likely,
            notable_weather=weather_info["notable"],
        )

        hourly_forecast.append(forecast)

    return hourly_forecast


def summarize_forecast(
    hourly_forecast: list[HourlyForecast],
) -> DailyWeatherSummary:
    if not hourly_forecast:
        raise ValueError("Cannot summarize an empty forecast.")

    low = min(hour.temperature for hour in hourly_forecast)
    high = max(hour.temperature for hour in hourly_forecast)

    max_feels_like = max(hour.feels_like for hour in hourly_forecast)

    max_rain_chance = max(hour.rain_chance for hour in hourly_forecast)

    rainy_hours = [hour for hour in hourly_forecast if hour.rain_is_likely]

    notable_hours = [hour for hour in hourly_forecast if hour.notable_weather]

    rain_start = rainy_hours[0].time if rainy_hours else None
    rain_end = rainy_hours[-1].time if rainy_hours else None

    if notable_hours:
        worst_hour = max(
            notable_hours,
            key=lambda hour: hour.severity,
        )
        worst_condition = worst_hour.condition
    else:
        worst_condition = "No notable weather"

    if max_rain_chance >= 50:
        recommendation = "Bring an umbrella."
    elif max_feels_like > 90:
        recommendation = "Expect uncomfortable heat."
    elif max_rain_chance >= 30:
        recommendation = "There is a chance of rain."
    else:
        recommendation = "Conditions should be generally comfortable."

    return DailyWeatherSummary(
        date=hourly_forecast[0].time.strftime("%Y-%m-%d"),
        low=low,
        high=high,
        max_feels_like=max_feels_like,
        max_rain_chance=max_rain_chance,
        rain_start=rain_start,
        rain_end=rain_end,
        worst_condition=worst_condition,
        recommendation=recommendation,
    )
