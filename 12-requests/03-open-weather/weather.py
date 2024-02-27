import requests
from jsonschema import validate
from jsonschema.exceptions import ValidationError


class WeatherResponse:
    def __init__(self, description, temperature, feels_like):
        self.description = description
        self.temperature = temperature
        self.feels_like = feels_like

    def __str__(self):
        return f"The current weather is {self.description}. The temperature is {self.temperature} C but it feels like {self.feels_like} C."


class Weather:
    def __init__(self, api_key):
        self.api_key = api_key
        self.__weather_url = "https://api.openweathermap.org/data/2.5/weather"
        self.__weather_schema = {
            "type": "object",
            "properties": {
                "weather": {"type": "array"},
                "main": {
                    "type": "object",
                    "properties": {
                        "temp": {"type": "number"},
                        "feels_like": {"type": "number"}
                    }
                }
            }
        }

    def get_weather(self, lat, lon):
        response = requests.get(f"{self.__weather_url}?lat={lat}&lon={lon}&appid={self.api_key}&units=metric")

        if response.status_code == 200:
            weather = response.json()
            self.validate_response(weather)
            return WeatherResponse(
                description=weather['weather'][0]['description'],
                temperature=weather['main']['temp'],
                feels_like=weather['main']['feels_like']
            )
        else:
            raise UnsuccessfulWeatherRequestError(response.status_code)

    def validate_response(self, weather_response):
        try:
            validate(instance=weather_response, schema=self.__weather_schema)
        except ValidationError as e:
            raise InvalidWeatherResponseError(e.message)


class UnsuccessfulWeatherRequestError(Exception):
    def __init__(self, message):
        super().__init__(message)


class InvalidWeatherResponseError(Exception):
    def __init__(self, message):
        super().__init__(message)
