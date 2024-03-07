

def sym(l):             # define function sym that takes a list l as argument, checks the given list is symmetric
    if len(l) <= 1:     # base case for recursion, If the list l has one or no element, it symmetric
        return True
    return l[0] == l[-1] and sym(l[1:-1])  # two check point:compares first and last element of the list and recursively call itself with the list that exclude first and last element

def keyboard_input(lst_inp):   # defin function keyboard_input that input lst_inp, which list of element separate by commas
    elem = [m.strip() for m in lst_inp.split(',')]    # split the input lst_inp by commas to list and strips whitespace from each element
    for i, n in enumerate(elem):    # Iterate over the list elem, with i the index and n the value at each iteration
        try:                        # convert string n to an integer
            elem[i] = int(n)
        except ValueError:          # if fails shown a ValueError,then convert n to float and replace in elem
            try:
                elem[i] = float(n)
            except ValueError:
                pass
    return elem                    # return list elem contain integer, float and string

lst_inp = input("Enter a list of elements, separate by (,)commas): ")
user_list = keyboard_input(lst_inp)   # call keyboard_input function with user input, process string to list of mixed(integer, float, string), assign to user_list

is_symmetric = sym(user_list)      # call sym function with list user_list to check symmetric, result store in is_symmetric

# Print the result
print("\n=============== Output ===============")
print(f"Input list is: {user_list}")
print(f"Is the list {user_list} is symmetric? Result is: {is_symmetric}")
