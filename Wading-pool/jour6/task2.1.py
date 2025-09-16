def recursum(n): # on defini une fonction qui prend n en parametre
    if n==0: 
        return 0
    else:
        return n + recursum(n-1)

print(recursum(42))