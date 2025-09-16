def doubleham():
    print("<////////// >")
    print("~~~~~~~~~~~~")
    print("O O O O O O")
    print("============")
    print("============")
    print("<////////// >")

def doubleveggie():
    print("<////////// >")
    print("~~~~~~~~~~~~")
    print("O O O O O O")
    print("~~~~~~~~~~~~")
    print("<////////// >")

try:
    user = int(input("How many sandwiches do you want? "))
    if user > 0:
        choice= input("Sandwiches veggie ?")
        for _ in range(user): # _ pas de boucle definie, donc "doubleham" tourne à la demande de l'utilisateur
            if choice =="yes":
                doubleveggie()
            else:
                doubleham()
    else:
     print("I can't do this!")

except ValueError: # quand il y a une erreur dans le code 
    print("i don't understand")