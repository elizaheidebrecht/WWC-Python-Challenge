#Write a function to find the largest common divisor of two numbers
#using a function

#User enters 2 numbers
num1 = int(input("Enter a number:"))
num2 = int(input("Enter another number:"))
factors1 = []
factors2 = []

#Finds the factors for both number and adds them to two lists          
for i in range(1, num1 + 1):
    if num1 % i == 0:
        factors1.append(i)
                     
for i in range(1, num2 + 1):
    if num2 % i == 0:
        factors2.append(i)

shared_factors = []

#Adds all common factors to one list and prints out the largest number
for i in factors1:
    if i in factors2:
        shared_factors.append(i)
           
print(max(shared_factors))  
           
