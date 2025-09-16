import re
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                


def funA(s,n): 
    return len(s) >= n
        

def funB(s,n): 
    return len(re.findall(r"[!@#$%^&*()_+{}\[\]:;<>,.?\\/-]", s)) >= n 
        

def funC(s,n): 
    return len(re.findall(r"[0123456789]", s)) >= n
        
def passcheck(func, n, s):
    return func(s, n)

print(passcheck(funA , 16 , " mysecretpasswordd "))
print(passcheck(funB , 3 , " mysecretpassword?,,, "))
print(passcheck(funC , 1 , " mysecretpassword1 "))

def reel_passcheck(s):
     return funA(s, 16) and funB(s, 3) and funC(s, 1)

print(reel_passcheck("mysecretpassword?,,88,"))
