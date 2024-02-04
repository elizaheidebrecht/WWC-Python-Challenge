#Write a function that takes a list of numbers and returns a new list
#containing only the even numbers.

#Find even numbers and add them to a new list
def only_even(num_list):
    even_nums = []
    for i in num_list:
        if i % 2 == 0:
            even_nums.append(i)
    return even_nums

#User inputs list of numbers which are added to a new list and converted to
#integers. 
input_list = input("Enter a list of numbers separated by a comma:")
new_list = input_list.split(",")
num_list = []

for i in new_list:
    num_list.append(int(i))
    

print("The even numbers are:", only_even(num_list))
