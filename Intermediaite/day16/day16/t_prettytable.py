from prettytable import PrettyTable

x = PrettyTable()

x.field_names=["Nom", "Prenom", "Age"]

x.add_row(["Jean Baptiste", "Prince", 30])
x.add_row(["Jean Baptiste", "Prince", 30])
x.add_row(["Jean Baptiste", "Prince", 30])
x.add_row(["Jean Baptiste", "Prince", 30])
x.add_row(["Jean Baptiste", "Prince", 30])


print(x)

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.align = 'r'

table.add_column("Type", ["Electric", "Water", "Fire"])

print(table)