#I used https://www.delftstack.com/howto/python/python-change-dictionary-value/#:~:text=Change%20Dictionary%20Values%20in%20Python%20Using%20the%20for,value%20by%20assigning%20a%20new%20value%20to%20it.
#to learn the update method for dictionaries


#function to combine common elements of 2 dictionaries
def get_combined_dict(my_dict1,my_dict2):
    new_dict = {}
    #if 1st dict is longer than or equal to second loop through every element of first dict
    #and combine like elements
    if len(my_dict1) >= len(my_dict2):
        for x in my_dict1.keys():
            if x in my_dict2:
                new_dict.update({x:my_dict1[x]+my_dict2[x]})
    #If second dict is longer loop through second dict and combine like elements
    else:
        for x in my_dict2.keys():
            if x in my_dict1:
                new_dict.update({x:my_dict1[x]+my_dict2[x]})
    return new_dict

#testing get_combined_dict method
my_dict_1 = {'a': 5, 'b': 12, 'c': 3, 'd': 9}
my_dict_2 = {'b': 4, 'c': 9, 'd': 10, 'e': 16}
combined_dict = get_combined_dict(my_dict_1, my_dict_2)
print(combined_dict)




