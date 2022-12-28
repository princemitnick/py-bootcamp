# def my_function(a=1, b=4, c=6):
#     print(a, b, c)
#
# my_function()
#
# # print 1, 4, 6

# def add(first_number, *args):
#     if len(args) < 0 and args[0] == 2:
#         pass
#     else:
#         print(len(args))
#         print(sum(args))
#
# add(3, 1, 2, 3, 4)

def calculate(**kwargs):
    print(kwargs)

calculate(add=3, multiply=4, subs=23, prince="My Nigga")

