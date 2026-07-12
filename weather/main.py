import argparse
import requests

from weather.client import get_hourly_weather_info
from weather.analyzer import get_hourly_forecast, summarize_forecast
from weather.config import (
    HOME_LATITUDE,
    HOME_LONGITUDE,
    WEATHER_API_URL,
)
from weather.formatter import format_weather_message
from weather.messaging.textbelt import send_weather_text


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-d",
        "--dry",
        action="store_true",
        default=False,
        help="Dry run (dont send texts)",
    )

    args = parser.parse_args()

    try:
        hourly_data = get_hourly_weather_info(
            url=WEATHER_API_URL,
            latitude=HOME_LATITUDE,
            longitude=HOME_LONGITUDE,
        )

        hourly_forecast = get_hourly_forecast(hourly_data)
        summary = summarize_forecast(hourly_forecast)
        message = format_weather_message(summary)

        if args.dry:
            print(message)
        else:
            send_weather_text(message)

    except requests.RequestException as error:
        print(f"Weather API request failed: {error}")

    except Exception as error:
        print(f"Application failed: {error}")


if __name__ == "__main__":
    main()
