#Write a function to check if a given list is sorted

def is_sorted(list1):
    return list1 == sorted(list1) or list1 == sorted(list1, reverse = True)


list1 = [4,65,7,3,54,2,7,1]
print(is_sorted(list1))
