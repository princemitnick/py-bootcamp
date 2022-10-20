
print("Byenvini nan jwet sa-a. Fout pran san w. lanmed")

def add(a,b):
    return a+b

def subs(a,b):
    return a - b

def mult(a,b):
    return a * b

def div(a,b):
    if b == 0:
        print("Impossible")
    else:
        return a / b

condition = True


while condition:
    cond = input("Veux-tu faire une operation?  (Y/N) : ").lower()
    if cond == "y":
        a = float(input("Entre le premier nombre : "))
        b = float(input("Entrer le second nombre : "))
        choice = input("Add, Sub, Mul, Div ? ").lower()
        if choice == 'add':
            print(add(a, b))
        elif choice == 'sub':
            print(subs(a, b))
        elif choice == 'mul':
            print(mult(a, b))
        elif choice == 'div':
            print(div(a, b))
    else:
        condition = False

    con = input("Voudrais tu continuer ? (Y/N)").lower()
    if con == 'y':
        condition = True
    else:
        condition = False

