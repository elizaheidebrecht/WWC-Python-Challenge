#Create a program that uses a lambda function to square each element of a list.

list_nums = [1,2,3,4,5,6]

list_nums = map(lambda x:x **2,list_nums)

for num in list_nums:
    print(num, end=' ')

