#Create a program that counts the occurrences of each word in a text file

from collections import Counter
import re

with open('Pytest2.txt') as file:
    counts = Counter(file.read().split())
    print(counts)
