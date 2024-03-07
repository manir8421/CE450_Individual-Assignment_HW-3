
def f(suits, numbers):                         # defines a function f with two parameters suits and numbers
    if not suits or not numbers:
        print("New generated list: []")        # check if either the suits list or the numbers list is empty
        return []                              # teturns an empty list if either input list is empty
    
    lst = []                                   # Initializes lst to store the combined elements
    for suit in suits:                         # Starts a loop for each element in suits list
        for number in numbers:                 # sested loop for each element in the numbers list for every suit
            lst.append([suit, number])         # Appends to lst with the current suit and number
    return lst

# user input
suits_inp = input("Enter suits separated by commas (Alphabets): ")
numbers_inp = input("Enter numbers separated by commas (Numbers): ")

sts_chk = suits_inp.split(',') if suits_inp else []      # Splits the input string by commas to create a list of suits
num_chk = [int(number.strip()) for number in numbers_inp.split(',')] if numbers_inp else []    # Splits the input by commas, strips whitespace from each number, converts each to an integer and creates a list of numbers.

new_gen_list = f(sts_chk, num_chk)             # Call the function f with the new suits and numbers lists

if new_gen_list:
    print("New generated list: ", new_gen_list)
