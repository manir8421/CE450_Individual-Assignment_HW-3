
def rm_all(elem, lst):                                # define function "rm_all" with argument  "elem" and list "lst"
    answer = [m for m in lst if m not in elem]        # list includes items from lst that are not in elem, effectively removing the specified elements
    not_found = [n for n in elem if n not in lst]     # list contains elements from elem that supposed to be removed but were not found in lst
    return answer, not_found                          # return the values

user_inp = input("Enter a initial list of numbers / strings (separated by commas) : ")
x = [init_inp.strip() for init_inp in user_inp.split(',')]   # initial input check and seperate

del_inp = input("Enter the elements to remove (separated by commas)\t\t: ")
element = [remv_inp.strip() for remv_inp in del_inp.split(',')]  # remove input check and seperate

result, not_found = rm_all(element, x)

print("======================= Output  =============================")
print("\nType the initail input list:", x)
print("Type the Element to remove:", element)
print("The final list after removal:", result)
if not_found:
    print("\nThe following entered elements were not in the initial list:", not_found)
