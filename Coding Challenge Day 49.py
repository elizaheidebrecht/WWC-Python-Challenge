#Create a program that implements the bubble sort algorithm

#Function sorts number from input_list from smallest to largest
def bub_sort(input_list):
    input_list = input_list.split(",")
    l = len(input_list)
    for i in range(l):
        for j in range(0, l - i - 1):
            if input_list[j] > input_list[j + 1]:
                input_list[j], input_list[j + 1] = input_list[j + 1],input_list[j]
    return input_list
    
#Usr inputs list of nums separated by commas
input_list = input("Enter a list of numbers separated by commas:".split(","))
print(bub_sort(input_list))

