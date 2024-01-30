for i in range(1, 6):  # [1, 2, 3, 4, 5, 6]
    if i == 3:
        print("Encountered 3, breaking the loop")
        break
    elif i == 2:
        print("Encountered 2, skipping this iteration")
        continue
    else:
        print("Iteration:", i)
        pass  # Placeholder statement, does nothing

print("Loop finished")
