def get_combined_dict(my_dict1,my_dict2):
    new_dict = {}
    if len(my_dict1) >= len(my_dict2):
        for x in my_dict1.keys():
            if x in my_dict2:
                new_dict.update({x:my_dict1[x]+my_dict2[x]})
    else:
        for x in my_dict2.keys():
            if x in my_dict1:
                new_dict.update({x:my_dict1[x]+my_dict2[x]})
    return new_dict

my_dict_1 = {'a': 5, 'b': 12, 'c': 3, 'd': 9}
my_dict_2 = {'b': 4, 'c': 9, 'd': 10, 'e': 16}
combined_dict = get_combined_dict(my_dict_1, my_dict_2)
print(combined_dict)



