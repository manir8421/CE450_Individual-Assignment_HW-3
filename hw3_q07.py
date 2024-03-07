

def chk_elm(lst, n):     # define function chk_elm has two parameters lst, n; wgere lst is input list and n is the search element
    return n in lst      # return True if n is found within lst, otherwise False

# user input from keyboard
lst_input = input("Type like:[1, [2, 3], 4] for input list/nested list\t: ")
n = input("Enter the element you want to search for\t\t: ")

if not lst_input.strip() or not n.strip(): # both input check
    print("\n=============== Output ===============")
    print("Invalid input.")
else:
    found = chk_elm(lst_input, n)

    # print output
    print("\n=============== Output ===============")
    print(f"Input list\t: {lst_input}")
    print(f"Search element\t: {n}")
    print(f"Is the element {n} exist in the list? Result is: {found}")
