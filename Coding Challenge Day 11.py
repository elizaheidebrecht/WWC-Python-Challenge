# Write a program to print the multiplication table of a given number

#User inputs a number
num_to_multiply = int(input("Enter a number for multiplication table:"))

#Input number is multiplied by every number in range 1 to 14
for num in range(1,15):
    product = num_to_multiply * num
#Product of operation is printed in a table
    print(num_to_multiply, "*", num, "=", product)
