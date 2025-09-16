first_names = [" Jackie ", " Chuck ", " Arnold ", " Sylvester "]
last_names = [" Stallone ", " Schwarzenegger ", " Norris ", " Chan "]
magic = [* zip ( first_names , last_names [:: -1]) ] # zip pour rassembler 2 listes
print ( magic [0])
print ( magic [3])
print ( magic [1][0])
print ( magic [0][1])
print ( magic [2])