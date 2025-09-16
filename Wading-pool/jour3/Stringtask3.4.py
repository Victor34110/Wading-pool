sentence = input("Enter your sentence: ") # on demande une phrase
word = sentence.split() # decoupe la phrase en liste de mots .split()

first_letters = [word[0] for word in word]

result = "".join(first_letters)

print(result)