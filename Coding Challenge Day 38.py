#Write a program to flatten a nested list


def flatten_list(lst):
    return [item for sublist in lst for item in sublist]
            
lst = [[5],[89,47,50],[77,79,54],[65,42],[78]]
flat = flatten_list(lst)
print(flat)

