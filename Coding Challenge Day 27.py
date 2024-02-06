#Create a program that sorts a list of strings alphabetically.

def alpha_list(input_lst):
    splitted = input_lst.split(",")
    return sorted(splitted)
    


input_lst = input("Enter a list of strings:")
print(alpha_list(input_lst))
