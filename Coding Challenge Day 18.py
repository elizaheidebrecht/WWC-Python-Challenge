#Create a program to find the largest among three numbers.

#Function finds largest number
def largest_number(a,b,c):
    largest_number = a
    if a < b:
        largest_number = b
    if b < c:
        largest_number = c
    return largest_number


#User Enters three numbers
a = float(input("Enter first number:"))
b = float(input("Enter second number:"))
c = float(input("Enter third number:"))

print("The largest number is :", largest_number(a,b,c))
