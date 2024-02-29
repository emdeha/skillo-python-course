import requests
from jsonschema import validate
from jsonschema.exceptions import ValidationError


class XkcdResponse:
    def __init__(self, image):
        self.image = image


class Xkcd:
    def __init__(self):
        self.__schema = {
            "type": "object",
            "properties": {
                "img": {"type": "string"}
            }
        }

    def get_latest(self):
        response = requests.get("https://xkcd.com/info.0.json")
        if response.status_code == 200:
            xkcd_comic = response.json()
            self.validate_response(xkcd_comic)
            return XkcdResponse(xkcd_comic["img"])
        else:
            raise XkcdComicAPIError(response.status_code)

    def validate_response(self, weather_response):
        try:
            validate(instance=weather_response, schema=self.__schema)
        except ValidationError as e:
            raise XkcdComicAPIError(e.message)

        
class XkcdComicAPIError(Exception):
    def __init__(self, message):
        super().__init__(message)


xkcd = Xkcd()
print(xkcd.get_latest().image)
