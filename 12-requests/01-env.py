from dotenv import load_dotenv
import os

load_dotenv()

print(os.getenv("OPEN_WEATHER_API_KEY"))
