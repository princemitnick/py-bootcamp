# def read_names():
#     with open("./Input/Names/invited_names.txt") as names:
#         lines = []
#         for name in names:
#             print(name.rstrip())
#
#
# read_names()

with open("sample1.txt", "r") as file:
    filedata = file.read()
    filedata = filedata.replace("human", "prince")

with open("sample1.txt", "w") as file:
    file.write(filedata)