def factorial(x):
    number = 1

    for i in range (1, x+1):
        number = number * i 
    return number 

print (factorial(10))
