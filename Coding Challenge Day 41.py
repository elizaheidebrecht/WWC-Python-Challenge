#Write a program that uses recursion to generate all permutations of a list

def perm_list(input_list):
    perms = []
    if len(input_list) <= 1:
        return input_list

    for i in perm_list(input_list[:-1]):
        for j in range(len(i)+1):
            perms.append(i[:j] + input_list[-1] + i[j:])
    return perms
            


input_list = input("Enter a list separated by commas:")
input_list = input_list.split(sep=",")

print(perm_list(input_list))
