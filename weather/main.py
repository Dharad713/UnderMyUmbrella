import argparse
import logging

from weather.analyzer import (
    get_hourly_forecast,
    summarize_forecast,
)
from weather.client import get_hourly_weather_info
from weather.config import (
    HOME_LATITUDE,
    HOME_LONGITUDE,
    PHONE_NUMBER,
    WEATHER_API_URL,
)
from weather.formatter import format_weather_message
from weather.messaging.textbelt import send_weather_text 

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

logger = logging.getLogger(__name__)


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-D",
        "--dry",
        action="store_true",
        help="Print the forecast without sending a text.",
    )

    return parser.parse_args()


def main() -> None:
    args = parse_arguments()

    logger.info("Weather job started")

    try:
        hourly_data = get_hourly_weather_info(
            url=WEATHER_API_URL,
            latitude=HOME_LATITUDE,
            longitude=HOME_LONGITUDE,
        )

        logger.info("Weather data received")

        hourly_forecast = get_hourly_forecast(hourly_data)
        summary = summarize_forecast(hourly_forecast)
        message = format_weather_message(summary)

        if args.dry:
            logger.info("Dry run: text not sent")
            print(message)
        else:
            send_weather_text(PHONE_NUMBER, message)
            logger.info("Weather text sent successfully")

    except Exception:
        logger.exception("Weather job failed")
        raise


if __name__ == "__main__":
    main()
