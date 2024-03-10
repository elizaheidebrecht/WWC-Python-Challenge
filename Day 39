#Write a program to find the most common words in a text file
from collections import Counter
import re
def read_file():
    file_path = "Pytest.rtf"
    with open(file_path, "r", encoding='utf-8') as file:
        content = file.read()
    words = re.findall(r'\b\w+\b', content.lower())   
    #clean_words = [word.lower() for word in words if word.isalnum()]

    word_count = Counter(words)
    most_words = word_count.most_common(3)
    
    return most_words

print(read_file())


                                                                                    
