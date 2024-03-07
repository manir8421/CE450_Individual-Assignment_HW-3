
def add_many(x, elem, lst):   # define function add_many takes three parameters: x, elem, lst
    lst.extend([elem] * x)    # list extend method to add elem to the list x times
    return lst

# user input
lst_input = input("Type the list like:1,2,3 (separate by comma)\t: ")
x_input = int(input("Type the value for number of times to add (x)\t: "))
elem_input = input("Type the value for element to add(elem))\t: ")


z = [int(i.strip()) for i in lst_input.split(',')]      # lst_input split it into individual elements at comma, stripping any whitespace,convert element to integer
y = int(elem_input) if elem_input.isdigit() else elem_input   # to add elem_input to an integer if it is compose only digit
modified_list = add_many(x_input, y, z)   # Call the add_many function input and assign result to modified_list

print("\n==== Output  ====")
print("Modified new list:", modified_list)
