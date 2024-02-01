braces = "(())"
braces_incorrect = "())"
braces_incorrect_two = "(()"
braces_incorrect_three = "(()()((()))"


def check_correct_braces(string):
    stack = []
    for char in string:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if len(stack) <= 0:
                return False
            stack.pop()

    return len(stack) == 0


print(f"{braces} is correct? {check_correct_braces(braces)}")
print(f"{braces_incorrect} is correct? {check_correct_braces(braces_incorrect)}")
print(f"{braces_incorrect_two} is correct? {check_correct_braces(braces_incorrect_two)}")
print(f"{braces_incorrect_three} is correct? {check_correct_braces(braces_incorrect_three)}")
