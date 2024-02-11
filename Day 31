#Create a program that checks if a given string is a valid email address.

def email_valid(input_email):
    email_needs = ["@", ".com", ".org", ".edu", ".gov"]
    count = 0
    
    for i in email_needs:
        if i in input_email:
            count+= 1
        
    if count >= 2:
        return True
    else:
        return False

