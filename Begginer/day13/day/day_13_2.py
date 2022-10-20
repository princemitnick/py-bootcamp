'''
def my_function():
    for i in range(1, 20):
        if i == 20:
            print("You got it")
my_function()


from random import randint

dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
#dice_num = randint(0, len(dice_imgs))
dice_num = randint(0, 5)
print(dice_imgs[dice_num])

year = int(input("Year : "))
if year > 1980 and year < 1994:
    print("You are millenial.")
elif year >= 1994:
    print("You are a Gen Z.")


'''

def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
    b_list.append(new_item)
    print(b_list)


mutate([1,2,3,4,8,13])