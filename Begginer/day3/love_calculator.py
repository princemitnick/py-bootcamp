print("Welcome to the love Calculator")

name1 = input("What is your name ? : ")
name2 = input("What is their name? : ")

true = "true"
love = "love"

general_name =  name1.lower() + name2.lower()

'''
t = general_name.count("t")
r = general_name.count("r")
u = general_name.count("u")
e = general_name.count("e")

true = t + r + u + e

l = general_name.count("l")
o = general_name.count("o")
v = general_name.count("v")
e = general_name.count("e")
'''

count_true = 0
count_love = 0



for x in general_name:
    for y in true:
        if x == y:
            count_true += 1

for x in general_name:
    for y in love:
        if x == y:
            count_love += 1

score_str = f"{count_true}" + f"{count_love}"
score_int = int(score_str)

# print(count_true)
# print(count_love)

print(score_str)

if (score_int < 10) or (score_int > 90):
    print(f"Your score is {score_int}, you go together like coke and mentos")
elif (score_int >= 40) or (score_int <= 50):
    print(f"Your score is {score_int}, you are alright together.")
else:
    print(f"Your score is {score_int}")

'''
if score_int < 10:
    print(f"Your score is {score_int}, you go together like coke and mentos")
elif score_int > 90:
    print(f"Your score is {score_int}, you go together like coke and mentos")
elif score_int < 40:
    print(f"Your score is {score_int}, you are alright together.")
elif score_int <= 50:
    print(f"Your score is {score_int}, you are alright together.")
else:
    print(f"Your score is {score_int}")

'''