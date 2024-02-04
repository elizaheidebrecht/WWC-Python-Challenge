#Write a function that counts the frequency of each word in a sentence.

from collections import Counter
import string


def word_frequency(sent):
    words = sent.split()
    cleaned_words = [word.strip(string.punctuation).lower() for word in words]

    frequency_dict = Counter(cleaned_words)

    return frequency_dict

sent = input("Enter a sentence:")
result = word_frequency(sent)
print(result)

