#Write a program to find the maximum and minimum values in a list.

#User inputs list of numbers 
num_list = [int(x) for x in input("Please Enter a list of numbers separated by a space: ").split()]

#Find smallest and largest numbers using min() and max()
min_list = min(num_list)

max_list = max(num_list)

#Print largest and smallest numbers
print("Original list:\n", num_list)
print("The largest number is:", max_list)
print("The smallest number is:", min_list)
