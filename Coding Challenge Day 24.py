#Write a program to remove vowels from a given string.

def vowel_remove(input_list):
    input_list.lower()
    for i in input_str:
        if i not in vowel_list:
            no_vowel_lst.append(i)
            output_str = ''.join(no_vowel_lst)
    return output_str
    

vowel_list = ['a','e','i','o','u']
no_vowel_lst = []
input_str = input("Enter a string:")
input_list = input_str[:]
output_str = ''

print("Your string with no vowels:", vowel_remove(input_str))
