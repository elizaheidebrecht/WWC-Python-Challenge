#Create a program that imports the math module and uses its functions

import math

#function returns binomial coefficients

def bi_co(x,y):
    product = math.comb(x,y)
    return product

x = int(input("Enter first integer:"))
y = int(input("Enter second integer:"))

print(bi_co(x, y))


#when x < y, evaluates to 0 else: x! / (y! * (x - y)!)
