#Create a function that takes a string and returns the reverse of each word

def reverse_words(words):
    reverse = ""
    for word in words:
        word = word[::-1]
        reverse += word
        reverse += " "
    return reverse

input_str = input("Enter a sentence with no punctuation:")
words = input_str.split(" ")
print(reverse_words(words))

