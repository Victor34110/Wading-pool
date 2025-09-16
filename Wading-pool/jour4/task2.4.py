for num in range(-30, 30):
   if num % 3 ==0:
      print("fizz")

   elif num % 5 ==0:    #si la condioon precedente est fausse, teste celle-ci
      print("buzz")

   elif num % 3 == 0 and num % 5 == 0:
      print("fizzbuzz")

   else:
    print(num)



