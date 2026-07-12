from datetime import datetime

from weather.models.forcast import DailyWeatherSummary


def format_hour(value: datetime) -> str:
    return value.strftime("%I %p").lstrip("0")


def format_weather_message(
    summary: DailyWeatherSummary,
) -> str:
    message = (
        f"Today's forecast: {summary.low:.0f}–{summary.high:.0f}°F. "
        f"It may feel as hot as {summary.max_feels_like:.0f}°F. "
        f"Maximum rain chance: {summary.max_rain_chance}%. "
    )

    if summary.rain_start and summary.rain_end:
        message += (
            f"Rain is most likely between "
            f"{format_hour(summary.rain_start)} and "
            f"{format_hour(summary.rain_end)}. "
        )

    if summary.worst_condition != "No notable weather":
        message += f"Possible condition: {summary.worst_condition}. "

    message += summary.recommendation

    return message
