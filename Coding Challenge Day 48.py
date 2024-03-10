#Create a program that replaces specific words in a text with their synonyms

from nltk.corpus import WordNet

def syn(input_str, replace_word):
    synonyms = []
    for syn in wordnet.synsets(replace_word):
        for i in syn.lemmas():
            synonyms.append(i.name())

    for i in input_str:
        if i == replace_word:
            input_str.replace(i, synonyms[0])
    print(input_str)
        


input_str = input("Write a sentence:")

replace_word = input("Which word do you want to replace?")

syn(input_str, replace_word)
