#Write a Python program to merge two dictionaries
dict1 = {'blue': 'color','beach' : 'place','Edward' : 'name', '300' : 'number'}

dict2 = {'summer':'season'}

merge_dicts = {**dict1, **dict2}

print(merge_dicts)
