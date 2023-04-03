import os

with os.scandir("./test-dir/") as entries:
    for entry in entries:
        print(entry.name)