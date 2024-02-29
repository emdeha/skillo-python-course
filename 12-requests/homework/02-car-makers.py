from typing import List

import requests
from jsonschema import validate
from jsonschema.exceptions import ValidationError


class CarMakerResult:
    def __init__(self, make_id: int, make_name: str):
        self.make_id = make_id
        self.make_name = make_name

    def __str__(self):
        return f"Make ID: {self.make_id}\nMake Name: {self.make_name}"


class CarMakersResponse:
    def __init__(self, count: int, results: List[CarMakerResult]):
        self.count = count
        self.results = results


class CarMakers:
    def __init__(self):
        self.__cached_makers = None
        self.__schema = {
            "type": "object",
            "properties": {
                "Count": {"type": "number"},
                "Results": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "Make_ID": {"type": "number"},
                            "Make_Name": {"type": "string"}
                        }
                    }
                },
            }
        }

    def get_all(self):
        if self.__cached_makers is not None:
            return self.__cached_makers

        response = requests.get("https://vpic.nhtsa.dot.gov/api/vehicles/getallmakes?format=json")
        if response.status_code == 200:
            all_makes = response.json()
            self.validate_response(all_makes)
            results = list(map(
                lambda res: CarMakerResult(res["Make_ID"], res["Make_Name"]),
                all_makes["Results"],
            ))
            self.__cached_makers = CarMakersResponse(all_makes["Count"], results)
            return self.__cached_makers
        else:
            raise CarMakersError(response.status_code)

    def find_maker(self, make_name):
        all_makers = self.get_all()
        for maker in all_makers.results:
            if maker.make_name == make_name:
                return maker
        return None

    def validate_response(self, car_makers_response):
        try:
            validate(instance=car_makers_response, schema=self.__schema)
        except ValidationError as e:
            raise CarMakersError(e.message)


class CarMakersError(Exception):
    def __init__(self, message):
        super().__init__(message)


car_makers = CarMakers()
print(car_makers.find_maker("102 IRONWORKS, INC."))
print(car_makers.find_maker("Alabala"))
# all_makers = car_makers.get_all()
# print(car_makers.get_all().count)
