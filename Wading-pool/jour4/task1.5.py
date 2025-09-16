num = int(input("Nombre : "))
# on attend que quelqu'un tape un mdp

if num <= 42:
    # si la phrase est comparable à mdp       
    print("a")


elif num <= 21:  # si c'est inférieur ou égal à 21
    print("b")

elif num % 2 == 0:  # si c'est pair
    print("c")

elif num / 2 < 21:  # si le nombre divisé par 2 est inférieur à 21 (exclu)
    print("d")

elif num % 2 == 1 and num >= 45:  # si impair et supérieur ou égal à 45
    print("e")

else:  # toutes les autres situations
    print("il y a rien pour toi")
    #43"