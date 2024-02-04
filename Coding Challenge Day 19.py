#Write a function to calculate the factorial of a number.

import math

def factorial_num(num):
    result = math.factorial(num)
    return result

num = int(input("Enter a number to be factored:"))

print("The factorial of",num,"is:",factorial_num(num))
