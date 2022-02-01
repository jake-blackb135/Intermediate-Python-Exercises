#method to count the number of times a letter appears in a string
#and returns the result as a dict
def letter_counter(text):
    my_dict = {}
    
    #loops through each letter in text 
    for x in text:
        #if the current letter is a space it skips to the next letter
        if x == ' ':
            continue
        #if the current letter has already appeared it updates the counter
        elif x in my_dict:
            my_dict.update({ x : my_dict[x] + 1})
        #if the letter is new it adds it to the dict
        else:
            my_dict.update({x: 1})
    #returns result
    return my_dict

#tests letter_counter method
text = input("Enter a string: \n")
print(letter_counter(text))


