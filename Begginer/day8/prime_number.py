print("Prime number checker")



def prime_checker(number):
    if number == 0 or number == 1:
        print("Non-prime number")
    else:
        test = False
        for x in range(2, number):
            if number % x == 0:
                test = True

        if not test:
            print("Prime number")
        else:
            print("Non-prime number")


number = int(input("Number : "))

prime_checker(number)
