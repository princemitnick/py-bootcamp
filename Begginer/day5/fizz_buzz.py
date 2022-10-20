print("FiZz BuZz!")

for x in range(0, 1001):
    if x % 3 == 0 and x % 5 == 0:
        print("FiZzBuZz")
    elif x % 3 == 0:
        print("FiZz")
    elif x % 5 == 0:
        print("BuZz")
    else:
        print(x)

