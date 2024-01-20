#Write a function that accepts a string and calculates the number of uppercase
#and lowercase letters in it.


def count_upper_lower(string):
    lower_count = 0
    upper_count = 0

    for char in string:
        if char.islower():
            lower_count += 1
        elif char.isupper():
            upper_count += 1
    return lower_count, upper_count



string = input("Enter a string:")
lower_count, upper_count = count_upper_lower(string)

print("The amount of uppercase letter is:", upper_count)
print("The amount of lowercase letters is:", lower_count)
    
