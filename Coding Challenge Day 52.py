#Create a program that checks if a string is a palindrome

def is_palindrome(string_test,reverse):
    for i in string_test:
        reverse = i + reverse
        
    if string_test == reverse:
        return True
    elif string_test != reverse:
        return False
    else:
        return None
        
        
string_test = "potato"
reverse = ""
print(is_palindrome(string_test,reverse))
print(reverse)
