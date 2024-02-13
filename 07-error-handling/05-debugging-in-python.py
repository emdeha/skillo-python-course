import pdb


def divide(a, b):
    result = a / b
    return result


num1 = 10
num2 = 0

pdb.set_trace()

result = divide(num1, num2)

num1 = num1 * num2
num2 = num2 - 2
num2 = num2 + num1
num1 = num2

print("Result:", result)
