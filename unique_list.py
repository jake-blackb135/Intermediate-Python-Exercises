#I used the website https://www.w3schools.com/python/python_functions.asp to learn about the syntax for functions in python

#function to return all unique values in a list
def unique_list(my_list):
    new_list = []
    #loops through list and adds unique values to a new list
    for x in my_list:
        if x not in new_list:
            new_list.append(x)
    #returns the list pof unique values
    return new_list

#testing unique_list function
my_list = [1,2,3,2,1,4]
new_list = unique_list(my_list)
print(new_list)