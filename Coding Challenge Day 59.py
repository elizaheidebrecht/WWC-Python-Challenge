#Create a function that checks if a number is a perfect square

import math

def perfect_square(input_num):
    if math.sqrt(input_num) == math.isqrt(input_num):
        return True
    else:
        return False

input_num = int(input("Enter a number:"))
print(perfect_square(input_num))
