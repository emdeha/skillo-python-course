class NegativeQuantityException(Exception):
    pass


items = {"Coffee": 2.2, "Tea": 1.5, "Chocolate": 2.5}


def calculate_income():
    income = 0

    for item in items.keys():
        qty = float(input(f"How many {item}s have you sold? "))
        if qty < 0:
            raise NegativeQuantityException
        income = income + qty * items[item]

    return income


try:
    print(f"\nThe income today was £{calculate_income():0.2f}")
except Exception as e:
    print("Issue while calculating income", e)
