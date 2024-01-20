#Write a program to count the occurrences of a specific character in a string.

def value_search_count(string, char_to_count):
    count = 0
    lower_str = string.lower()

    for s in lower_str:
        if s == char_to_count:
            count+= 1
    return count

string = input("Enter a string: ")

value_to_search = input("Enter a value to search for and count in string: ")

count_search = value_search_count(string, value_to_search)
search_count = count_search

if count_search < 2:
    print("The element",value_to_search, "in your string appears", count_search,"time.")

else:
    print("The element",value_to_search, "in your string appears", count_search,"times.")
