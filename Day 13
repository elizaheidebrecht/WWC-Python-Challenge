#Write a program to shuffle the elements of a list randomly.

#User inputs a string
input_str = input("Enter a list with no spaces or commas:")
#Empty list is created
input_list = []
#Use slicing to copy chars from input_str to input_list
input_list[:0] = input_str
#import random to use shuffle method
import random

#shuffle elements of input_list
def shuffle(input_list):
    for i in input_list:
        i = random.shuffle(input_list)
    return input_list


#print original list and shuffled list
print("Your original list:", input_list)
print("Your shuffled list is:", shuffle(input_list))
        
        
