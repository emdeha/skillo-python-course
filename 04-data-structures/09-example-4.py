name = 'Alice'


def reverse_with_stack(string):
    reversed_name_stack = []
    for char in string:
        reversed_name_stack.append(char)
    # ['A','l','i','c','e']
    reversed_name = ''
    while len(reversed_name_stack) > 0:
        reversed_name += reversed_name_stack.pop()  # "e", "ec", "eci", "ecil", "ecilA"
    return reversed_name


print("Reversed name:", reverse_with_stack(name))
