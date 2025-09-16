import random

liste = [random.randint(1, 10000000) for _ in range(1000000)]

liste.sort()

print( liste)
