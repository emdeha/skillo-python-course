queue = []


def enqueue(element):
    queue.append(element)


def dequeue():
    return queue.pop(0)


enqueue(1)
enqueue(2)
enqueue(3)

print(dequeue())  # 1
print(dequeue())  # 2
print(dequeue())  # 3
