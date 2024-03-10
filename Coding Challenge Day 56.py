#Create a function to extract all URLs from a given text using regular
#expressions

import re

def url_extract():
    with open("Pytest2.txt") as file:
        for line in file:
            urls = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', line)
            print(urls)

url_extract()
