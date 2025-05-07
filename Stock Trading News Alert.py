import requests
from twilio.rest import Client
import os
from dotenv import load_dotenv

# Load environment variables from .env file (Ensure you create and configure .env)
load_dotenv()

# Twilio & API Keys (Stored securely in environment variables)
VIRTUAL_TWILIO_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")
VERIFIED_NUMBER = os.getenv("VERIFIED_PHONE_NUMBER")

STOCK_NAME = "NVDA"  # Ticker symbol for NVIDIA
COMPANY_NAME = "Nvidia Corporation"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = os.getenv("STOCK_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")

# Fetch stock data
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
stock_data = response.json()

# Check if "Time Series (Daily)" key exists
if "Time Series (Daily)" not in stock_data:
    print("Error: 'Time Series (Daily)' not found in API response.")
    print("API Response:", stock_data)
    exit()

data = stock_data["Time Series (Daily)"]
data_list = [value for key, value in data.items()]

if len(data_list) < 2:
    print("Error: Not enough data points to compare stock prices.")
    exit()

# Get yesterday's and day-before-yesterday's closing stock prices
yesterday_closing_price = float(data_list[0]["4. close"])
day_before_yesterday_closing_price = float(data_list[1]["4. close"])

# Calculate percentage difference
difference = yesterday_closing_price - day_before_yesterday_closing_price
up_down = "🔺" if difference > 0 else "🔻"
diff_percent = round((difference / day_before_yesterday_closing_price) * 100, 2)

print(f"{STOCK_NAME}: {up_down} {diff_percent}% change")

# Fetch news if stock price changed significantly (e.g., > 5%)
if abs(diff_percent) > 5:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    news_data = news_response.json()

    if "articles" not in news_data:
        print("Error: 'articles' key not found in News API response.")
        print("API Response:", news_data)
        exit()

    articles = news_data["articles"][:3]  # Get first 3 articles

    # Format messages
    formatted_articles = [
        f"{STOCK_NAME}: {up_down} {diff_percent}%\nHeadline: {article['title']}\nBrief: {article['description']}"
        for article in articles
    ]

    # Send messages via Twilio
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_=VIRTUAL_TWILIO_NUMBER,
            to=VERIFIED_NUMBER
        )
        print(f"Sent message: {message.sid}")
