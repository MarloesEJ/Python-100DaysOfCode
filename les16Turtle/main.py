from prettytable import *

table = PrettyTable()
table.add_column("Pokemon Name", ["pikachu", "Squirtle", "Charmander"])
table.add_column("type",["Electric", "Water", "Fire"])
table.align = "l"
#table.add_row("pikachu", "Electric")
# table.add_row("Squirtle", "Water")
# table.add_row("Charmander", "Fire")

print(table)
