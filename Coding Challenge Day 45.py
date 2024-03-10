#Write a function to check if a number is a prime number

def prime(user_input):
    for num in range(2, user_input - 1):
        if user_input % num == 0:
            return f'{user_input} is not a prime number.'
        else:
            continue
    else:
        return f'{user_input} is a prime number.'

user_input = int(input("Enter a number you want to check."))
print(prime(user_input))            
