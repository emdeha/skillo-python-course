x = 5


def change_global_state():
    global x
    x += 5
    return x


def increment_by_five(y):
    return y + 5


def input_y():
    y = int(input())
    return y


print("change global state", change_global_state())
print("change global state", change_global_state())
print("change global state", change_global_state())

print("increment by five", increment_by_five(5))
print("increment by five", increment_by_five(5))
print("increment by five", increment_by_five(5))
