

from operator import add, sub, mul     # functions from Python built-in operator module

def fld(lst, g, m):           # defines function fld that takes a list lst, a function g and initial value m,function recursively fold lst using g
    if not lst:               # recursion: If lst is empty, return current accumulate value m
        return m
    return fld(lst[1:], g, g(m, lst[0]))  # Calls fld with lst,function g applies g to current accumulate value m and the first element of lst, fold lst recursively apply g

def calc(key_inp):               # define function calc that input to corresponding operation function
    operation = {"add": add, "sub": sub, "mul": mul}
    return operation.get(key_inp, None)   # return function corresponding to key_inp, If key_inp is not found, returns None

inp_list = input("Type a list of numbers separate by (,)comma/(lst)\t: ")
user_inp = [int(item.strip()) for item in inp_list.split(',') if item.strip().isdigit()]  # split inp_list by commas, strips whitespace and converts element to integer if digit

operation_input = input("Enter the name of operation (add, sub, mul)/(g)\t\t: ")
operation = calc(operation_input)   # use calc to get corresponding operation function

initial_value = int(input("Enter the initial value/(m)\t\t\t\t: "))

if operation:
    result = fld(user_inp, operation, initial_value)  # call fld with the user list, operation and the initial value and store the result
    print("\n=============== Output ===============")
    print(f"Input list is(lst)\t: {user_inp}")
    print(f"Initial value is (m)\t: {initial_value}")
    print(f"Result is\t\t: {result}")
else:
    print("Invalid operation! Please choose between add, sub, and mul")
