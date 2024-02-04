#Create a program to find the second-largest element in a list.

def second_largest(num_list):
    largest_number = max(num_list)
    num_list.remove(largest_number)
    second_largest = max(num_list)
    return second_largest

num_list = [17,23,4,6,75,3500,65,78,92]

print("The second largest number is:", second_largest(num_list))
