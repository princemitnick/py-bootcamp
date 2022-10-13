def format_name(l_name, f_name):

    if l_name == "" or f_name == "":
        return
    else:
        f_name[:1].upper() + f_name[1:].lower()
        l_name[:1].upper() + l_name[1:].lower()
        # or
        c_f_name = f_name.title()
        c_l_name = l_name.title()

    return c_f_name + " " + c_l_name

format_name = format_name(input("First name : "), input("Last name : "))

print(format_name)
