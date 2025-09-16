def doubleham():
    print("<////////// >")
    print("~~~~~~~~~~~~")
    print("O O O O O O")
    print("============")
    print("============")
    print("<////////// >")

try:
    user = int(input("How many sandwiches do you want? "))
    if user > 0:
        for _ in range(user): # _ pas de boucle definie, donc "doubleham" tourne à la demande de l'utilisateur
            doubleham()
    else:
        print("I can't do this!")
except ValueError: # quand il y a une erreur dans le code 
    print("I can't do this!")