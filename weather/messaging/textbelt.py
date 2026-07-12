import requests

TEXTBELT_URL = "https://textbelt.com/text"



def send_weather_text(
    phone_number: str,
    message: str,
) -> None:
    response = requests.post(
        TEXTBELT_URL,
        data={
            "phone": phone_number,
            "message": message,
            "key": "textbelt",
        },
        timeout=10,
    )

    response.raise_for_status()

    result = response.json()

    if not result.get("success"):
        error = result.get("error", "Unknown Textbelt error")
        raise RuntimeError(f"Text message failed: {error}")

    print(
        "Text sent successfully. "
        f"Remaining quota: {result.get('quotaRemaining')}"
    )