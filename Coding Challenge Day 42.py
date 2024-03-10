#Write a program that uses a try-except block to handle division by zero

value = int(input("Enter a number:"))
value2 = int(input("Enter a non zero number:"))

try:
    print(value/value2)
except ZeroDivisionError:
    print("No zeros!")
except:
    print("Invalid input!")
