from collections import deque
import time
name = input()

customers = deque()

start_time = time.time()


while name != "End":
    if name == "Paid":
        while customers:
            print(customers.popleft())
    else:
        customers.append(name)
    name = input()


print(f"{len(customers)} people remaining.")

print("--- %s seconds ---" % (time.time() - start_time))
