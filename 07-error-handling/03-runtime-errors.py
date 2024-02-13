try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print("Result:", result)
except ZeroDivisionError:
    print("Division by 0")
    exit(0)
except KeyboardInterrupt:
    print("\nGoodbye!")
    exit(0)
except Exception as e:
    print("An unexpected error occurred:", e)
    exit(0)
finally:
    print("Always executed")
