#Create a function that converts a string to an integer and handles ValueError

def multiply_num(input_num):
    try:
        print(int(input_num) * int(input_num))
    except ValueError:
        print("Please enter a real number")
    except:
        print("I don't know just try again.")

input_num = input("Enter a number:")
multiply_num(input_num)
