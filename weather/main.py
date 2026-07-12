from weather.client import getHourlyWeatherInfo
from weather.analyzer import get_hourly_forecast, summarize_forecast
from weather.config import (
    HOME_LATITUDE,
    HOME_LONGITUDE,
    WEATHER_API_URL,
)
from weather.formatter import format_weather_message


def main() -> None:
    hourly_data = getHourlyWeatherInfo(
        url=WEATHER_API_URL,
        latitude=HOME_LATITUDE,
        longitude=HOME_LONGITUDE,
    )

    hourly_forecast = get_hourly_forecast(hourly_data)

    daily_summary = summarize_forecast(hourly_forecast)

    message = format_weather_message(daily_summary)
    print(message)


if __name__ == "__main__":
    main()
