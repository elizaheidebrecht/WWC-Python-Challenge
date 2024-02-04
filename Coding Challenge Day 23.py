#Write a program that checks if a key exists in a dictionary.


dict_1 = {"name" : "John", "major" : "CompSci", "height" : "5'7"}

input_key = input("Enter the name of the key you're looking for:")

def is_key(dict_1):
    if input_key in dict_1:
        return True
    else:
        return False
    
print(is_key(dict_1))
