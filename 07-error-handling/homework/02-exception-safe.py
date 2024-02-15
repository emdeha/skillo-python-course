def get_integer_input():
    num = int(input("Enter an integer: "))
    return num


try:
    number = get_integer_input()
    print("You entered:", number)
except ValueError as e:
    print("invalid value:", e)
except KeyboardInterrupt:
    print("program interrupted")
except Exception as e:
    print("unknown error:", e)
