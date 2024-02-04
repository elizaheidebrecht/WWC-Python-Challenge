# Write a program to print the first n numbers of a Fibonacci sequence

# User inputs amount of fib numbers, empty list is made to store #s
f_num = int(input("Enter the amount of Fibonacci numbers you would like:"))
f_num_list = []
# a and b represent the first and second integers of the sequence, 0 and 1.
# Count is set
count = 0
a = 0
b = 1


if f_num <= 0:
    print("Enter positive integer:")
elif f_num == 1:
    print("Fib Sequence up to", f_num,":")
    print(fn1)
else:
    print("Fib sequence up to", f_num, ";")
    #Counting makes sure that the loop stops once sequence is complete
    while count < f_num:
        f_num_list.append(a)
        #Equation for finding next fib integer
        c = a + b

        a = b
        b = c
        count += 1
    
    
print(f_num_list, sep=",")

