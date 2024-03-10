#Create a function that returns the key with the maximum value in a dictionary

def max_val(dict_1):
    return max(dict_1.values())
    

dict_1 = {"pizza":71, "soda":33, "napkins":98}
print(max_val(dict_1))
