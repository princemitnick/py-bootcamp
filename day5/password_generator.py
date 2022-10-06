import random

print("Welcome to the PyPassword Generator")

letters = "A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,Z,Y,Z,a,b,c,d,e,f,g,h,i,j,k" \
          ",l,m,n,o,p,q,r,s,t,u,v,w,x,y,z";
numbers = "1,2,3,4,5,6,7,8,9,0"

symbols = "~,!,@,#,$,%,^,&,&,*,(,),-,+"
letters_tab = letters.split(",")
numbers_tab = numbers.split(",")
symbols_tab = symbols.split(",")
password_tab = []
password = ""

letters_amount = int(input("How many letters would you like your password (0-52) : "))
symbols_amount = int(input("How many symbols would you like: "))
numbers_amount = int(input("How many numbers would you like: "))

if letters_amount < 0 or letters_amount >= len(letters_tab):
    print("Respect the range pls.")
elif symbols_amount < 0 or symbols_amount >= len(symbols_tab):
    print("Respect the range pls.")
elif numbers_amount < 0 or numbers_amount >= len(numbers_tab):
    print("Respect the range pls.")
else:
    for x in range(0,letters_amount):
        letters_random = random.randint(0, len(letters_tab)-1)
        password_tab.append(letters_tab[letters_random])

    for x in range(0, symbols_amount):
        symbols_random = random.randint(0, len(symbols_tab)-1)
        password_tab.append(symbols_tab[symbols_random])

    for x in range (0, letters_amount):
        number_random = random.randint(0, len(numbers_tab)-1)
        password_tab.append(numbers_tab[number_random])

    random.shuffle(password_tab)

    for x in range(0, len(password_tab)-1):
        password_random = random.randint(0, len(password_tab)-1)
        password += password_tab[password_random]

    print(password)
'''
random_char = random.choice(letters_tab)
print(random_char)
'''