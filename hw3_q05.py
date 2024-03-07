
def mrg(ls1, ls2):     # defines function mrg takes two lists ls1 and ls2 as parameters
    if not ls1:        # checks if ls1 is empty returns ls2 as the result
        return ls2
    if not ls2:        # checks if ls2 is empty returns ls2 as the result
        return ls1
    
    if ls1[0] <= ls2[0]:      # compares first elements ls1 and ls2, first element of ls1 is less than or equal to first element of ls2, make a new list with the first element of ls1
        return [ls1[0]] + mrg(ls1[1:], ls2)
    else:                     # first element of ls2 is less than the first element of ls1,starts a new list with the first element of ls2
        return [ls2[0]] + mrg(ls1, ls2[1:])

def parse_input(input_str):   # defines function parse_input takes input comma-separated values input_str and converts to list of integers
    return [int(x.strip()) for x in input_str.split(',') if x.strip().isdigit()]    # splits input by commas, strips whitespace from each, and converts each to an integer

# ask user for input
input_list_1 = input("Enter the first list\t: ")
input_list_2 = input("Enter the second list\t: ")

# parsing the input strings into lists of integers and sorting them
sorted_lst_1 = sorted(parse_input(input_list_1))
sorted_lst_2 = sorted(parse_input(input_list_2))

# merging the sorted lists
merged_list = mrg(sorted_lst_1, sorted_lst_2)

print("\n============ Output  ====================")
print("First input list sorted\t: ", sorted_lst_1)
print("Second input list sorted: ", sorted_lst_2)
print("\nMerged sorted list\t:", merged_list)
