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


Install dependencies:
in bash:

pip install -r requirements.txt

Run locally or deploy to Azure Functions.

📅 Schedule
The function runs every weekday at 6:02 AM and checks the weather.

📝 Example Output
"Vigyél esernyőt! (ID list: [500, 501, 800])"
SMS sent to +3630xxxxxxx

⚠️ Disclaimer
Do not commit your .env file or secrets to the repository. Use .gitignore.

🤝 Author
László Gombos
LinkedIn: www.linkedin.com/in/laszlo-gombos-the-original
