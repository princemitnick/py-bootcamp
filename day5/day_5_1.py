
fruits = ["Apple", "Peach", "Pear"]

for fruit in fruits:
    print(fruit, end=", ")
    for x in range(1000):
        print(f"{fruit} : {x}")