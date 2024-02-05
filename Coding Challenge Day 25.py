#Create a program to concatenate two lists.

def concat_lists(list1, list2):
    list1.split(",")
    list2.split(",")
    new_list = list1 + list2
    return new_list

list1 = input("Enter your first list ending with a comma:")
list2 = input("Enter your second list:")

print(concat_lists(list1, list2))
