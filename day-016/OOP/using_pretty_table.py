# Example of using OOP

from prettytable import PrettyTable

# construct table object using PrettyTable class
table = PrettyTable()

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

table.align ="l" #Align to left

print(table)

