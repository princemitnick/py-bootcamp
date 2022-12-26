fruits = ["Apple", "Pear", "Orange"]

def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError as index_err_msg:
        print(f"Fruit Pie {index_err_msg}")
    else:
        print(fruit + " pie")

make_pie(3)