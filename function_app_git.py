import logging
import azure.functions as func
import requests
from twilio.rest import Client
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Create an instance of the Azure Function App
app = func.FunctionApp()

# Define the function to run on a schedule (Weekdays at 6:02 AM)
@app.timer_trigger(
    schedule="0 2 6 * * 1-5",  # At 6:02 AM every weekday
    arg_name="myTimer",
    run_on_startup=False,
    use_monitor=False
)
def timer_trigger(myTimer: func.TimerRequest) -> None:
    """
    Azure timer-triggered function entry point.
    Calls the weather-checking function if schedule is met.
    """
    if myTimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function executed.')
    willrain()


def willrain():
    """
    Checks the weather forecast from OpenWeatherMap API.
    If rain is detected in upcoming forecasts, sends an SMS alert via Twilio.
    """

    # Load secrets from environment variables
    AppID = os.getenv("OPENWEATHER_APP_ID")               # OpenWeatherMap API Key
    account_sid = os.getenv("TWILIO_ACCOUNT_SID")         # Twilio Account SID
    auth_token = os.getenv("TWILIO_AUTH_TOKEN")           # Twilio Auth Token
    from_number = os.getenv("TWILIO_FROM")                # Twilio phone number (sender)
    to_number = os.getenv("TWILIO_TO")                    # Recipient phone number

    # Set up weather API parameters
    parameters = {
        "lat": 47.40,             # Latitude (e.g., Budapest)
        "lon": 19.10,             # Longitude
        "lang": "hu",             # Response language (Hungarian)
        "appid": AppID,
        "units": "metric",        # Use Celsius
        "cnt": 4                  # Number of forecast intervals to check (3-hour steps)
    }

    # Send request to OpenWeatherMap
    response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
    response.raise_for_status()
    data = response.json()

    # Extract weather condition IDs from forecasts
    ID_list = [forecast["weather"][0]["id"] for forecast in data["list"]]

    # Determine if rain or snow is expected (ID < 700 means precipitation)
    Will_rain = any(weather_id < 700 for weather_id in ID_list)

    # If precipitation is expected, send SMS alert
    if Will_rain:
        logging.info("Rain or snow expected. Weather ID list: %s", ID_list)

        # Create Twilio client and send SMS
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body='Vigyél esernyőt ma!',   # "Take an umbrella today!" in Hungarian
            from_=from_number,
            to=to_number
        )

        logging.info("SMS sent. Status: %s", message.status)
    else:
        logging.info("No rain expected. Weather ID list: %s", ID_list)
