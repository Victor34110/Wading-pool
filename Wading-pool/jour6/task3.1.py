import re
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
s = input("phrase: ")
n = int(input("entier: "))



def funA(s,n): # prend une chaine et un entier
    if len(s) >= n :
        return True
    return False

def funB(s,n): #vérifie le nombre de caractères spéciaux
    if len(re.findall(r"[!@#$%^&*()_+{}\[\]:;<>,.?\\/-]", s)) >= n: # ien cherche à compter
        return True
    return False

def funC(s,n): #vérifie le nombre de chiffres
    if len(re.findall(r"[0123456789]", s)) >= n: #  
        return True
    return False

print(funA(s,n))
print(funB(s,n))
print(funC(s,n))
