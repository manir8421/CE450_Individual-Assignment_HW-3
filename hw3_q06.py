
def fltn(ls):             # define function fltn with an argument ls,for list contain nested lists
    fltn_empty_list = []  # empty list fltn_empty_list will used to store the flatten of ls.
    for item in ls:
        if isinstance(item, list):              # check the current item is a list itself
            fltn_empty_list.extend(fltn(item))  # if a list,recursive call the fltn function on item to flatten it, appended to fltn_empty_list using the extend method
        else:
            fltn_empty_list.append(item)        # if item is not a list,directly appended to fltn_empty_list
    return fltn_empty_list            # returns fltn_empty_list, which is flatten of the original list ls

def par_inp(input_str):     # define function par_inp take a single argument input_str representation of a list
    try:
        import ast          # to evaluate input_str as Python expression using the ast.literal_eval function,parse a string or source code into Python object
        return ast.literal_eval(input_str)
    except:
        print("Invalid input list format!")
        return []
    
key_inp = input("Type like:[1, [2, 3], 4] for list/nested list : ")
nested_lst = par_inp(key_inp)
flatten_lst = fltn(nested_lst)

print("\nInput list\t: ", key_inp)
print("=============== Output ===============")
print("Flattened list\t: ", flatten_lst)
