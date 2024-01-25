weather = "rainy"
temperature = 0

if weather == "sunny":
    pass
elif weather == "rainy":
    if temperature <= 0:
        print("Caution! Road may be icy")
    elif temperature < 20:
        print("Caution! Slippery road")
    else:
        print("Drive carefully!")