
def operation(calc_operator, n1, n2):
    if calc_operator == '+':
        return n1 + n2
    if calc_operator == '-':
        return n1 - n2
    if calc_operator == '*':
        return n1 * n2
    if calc_operator == '/':
        if n2 == 0:
            print("Division by zero is not allowed")
            do_calculating()
        else:
            return n1 / n2


def do_calculating():
    start_over = True
    while start_over:

        result = 0
        keep_calculating = True
        first_number = float(input("What's the first number? "))
        print("+ - / *")
        calc_operator = input("Pick an operator : ")
        second_number = float(input("What's the second number? "))
        result = operation(calc_operator, first_number, second_number)
        print(f"{first_number} {calc_operator} {second_number} = {result}")

        while keep_calculating:
            again = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation : ").lower()
            if again == "y":
                calc_operator = input("Pick an operator : ")
                next_number = float(input("New number : "))
                last_result = result
                result = operation(calc_operator, last_result, next_number)
                print(f"{last_result} {calc_operator} {next_number} = {result}")
                keep_calculating = True
            else:
                print("Start over.")
                keep_calculating = False
                start_over = True


do_calculating()