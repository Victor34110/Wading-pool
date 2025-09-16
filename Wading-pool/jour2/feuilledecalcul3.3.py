num = 44490320097
res = 0

while num > 0:
    res += num % 10  # extract last digit
    num //= 10       # remove last digit


print("Resultat :", res)

