#Create a function to find all words in a sentence that start with a vowel

def vowel_finder(sentence):
    vowels = "a","e","i","o","u"
    vowel_words = []
    for word in sentence.split(" "):
        if word[0] in vowels:
            vowel_words.append(word)
    return vowel_words

sentence = input("Enter a sentence:")
print(vowel_finder(sentence))
            
