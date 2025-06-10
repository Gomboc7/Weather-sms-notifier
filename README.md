# ☁️ Azure Weather Notifier with SMS Alert

This Python project runs as an Azure Function and checks the morning weather forecast using OpenWeatherMap. If rain is predicted, it sends an SMS alert via Twilio.

## 💡 Features

- Daily weather forecast from OpenWeatherMap
- Checks for rain in the next 4 time intervals
- Sends an SMS alert with Twilio if rain is expected
- Runs as an Azure Timer Trigger Function (Mon–Fri, 6:02 AM)

## 🚀 Technologies

- Python
- Azure Functions
- Twilio SMS API
- OpenWeatherMap API
- `.env` config management with `python-dotenv`

## 📦 Setup

1. Clone the repo
2. Create a `.env` file in the root folder with:

```env
OPENWEATHER_APP_ID=your_openweather_key
TWILIO_ACCOUNT_SID=your_twilio_sid
TWILIO_AUTH_TOKEN=your_twilio_token
TWILIO_FROM=+123456789
TWILIO_TO=+36301234567
```

Help for get your APIs:
- [OpenWeatherMap API](https://openweathermap.org/api)
- [Twilio SMS API](https://www.twilio.com/docs/sms)


3. Edit your location in function_app_git.py (row 48-49):
```python
    parameters = {
        "lat": 47.40,             # Latitude (e.g., Budapest)
        "lon": 19.10,             # Longitude
```
-> you can get it from https://www.latlong.net/.

4. Install dependencies:

```bash
pip install -r requirements.txt
```

5. This project is designed to run as an Azure Functions Timer Trigger, not as a standalone script.
To run locally for testing purpose, you can call: 
```bash
python test.py
```
And then check willrain.log for output

Hint for deploying to Azure functions:
https://dev.to/edgaras/deploying-azure-functions-with-python-a-step-by-step-guide-5db6


📅 Schedule
The function runs every weekday at 6:02 AM and checks the weather.
You can set time in row 16:
```python
@app.timer_trigger(
    schedule="0 2 6 * * 1-5",  # At 6:02 AM every weekday ("Sec Min Hour Day Month Daysofweek")
```

📝 Example Output
"Vigyél esernyőt! (ID list: [500, 501, 800])"
SMS sent to +3630xxxxxxx

⚠️ Disclaimer
Do not commit your .env file or secrets to the repository. Use .gitignore.


🤝 Author
László Gombos
LinkedIn: www.linkedin.com/in/laszlo-gombos-the-original
