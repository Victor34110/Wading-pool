for n in range(99, 0, -1):
    if n == 1: #quand il reste qu'une bouteille
        print("1 bottle of beer on the wall.")
        print("1 bottle of beer.")
        print("Take one down, pass it around,")
        print("No more bottles of beer on the wall\n")
    else:
        print(f"{n} bottles of beer on the wall.") #print f pour inserer une variable dans le texte
        print(f"{n} bottles of beer.")
        print("Take one down, pass it around,")
        print(f"{n-1} bottle of beer on the wall\n")