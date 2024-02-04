#Create a program that capitalizes the first letter of each word in a sentence

def capitalize_words(input_sentence):
    cap_words = []
    for word in input_sentence.split():
        cap_words.append(word.capitalize())
    return ' '.join(cap_words)

input_sentence = input("Enter a sentence:")

print(capitalize_words(input_sentence))

