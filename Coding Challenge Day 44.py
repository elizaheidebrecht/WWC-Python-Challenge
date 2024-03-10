#Write a program that reads an integer from the user and handles invalid inputs

try:
    user = int(input("Enter a number:"))
    print(user + 10)
except TypeError and ValueError:
    print("That is not an integer")
except:
    print("um")
