try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["not_exists_key"])
except FileNotFoundError as error1_message:
    file = open("a_file.txt", "w")
    file.write("Something")
except KeyError as error_message:
    print(f"Key does not exist : {error_message}")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("Bye!")