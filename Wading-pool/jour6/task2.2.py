
word = input("Enter a sentence : ").lower().replace(' ', '') # on prend une phrase en minuscule, on enleve les espaces
rev_word = ''.join(reversed(word)) # ordre inverse

if list(word) == list(rev_word): # si la phrase = la phrase en inversé
    print("palindrome")
else:
    print("pas palindrome")

