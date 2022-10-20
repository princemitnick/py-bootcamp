print("Adding evens.")

sum_even_numbers = 0
for x in range(0, 101):
    if x % 2 == 0:
        sum_even_numbers += x

print(sum_even_numbers)

total = 0
for number in range (2, 101, 2):
    total += number

print(total)