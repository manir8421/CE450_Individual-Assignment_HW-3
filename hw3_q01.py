
def mk_wd(balance):                      # define a function "mk_wd" with argument "balance"
    def withdraw(amount):                # define a nested function "withdraw with" one argument "amount"
        nonlocal balance                 # permit to change the  value of "balance"
        if amount <= balance:            # check  if the amount is less or equal than the current balance
            balance -= amount
            return balance
        else:
            return 'Insufficient funds'
    return withdraw

def neg_chk(prompt):                     # define a function "neg_chk" with an argument "prompt"
    while True:                          # start a loop that will continue until it gets valid input
        try:
            value = float(input(prompt))
            if value >= 0:
                return value
            else:
                print("Invalid input! Please enter a positive amount.")
        except ValueError:
            print("Invalid input! Please enter a valid amount.")

init_bal = None                         # initialize variable "init_bal" as None
while init_bal is None:                 # star loop asking for initial deposit
    init_bal = neg_chk("Please enter the initial balance of the account\t: ")

rem = mk_wd(init_bal)                   # function "mk_wd " with the initial balance passed as argument

while True:                             # start a loop that will continue indefinitely
    amount = neg_chk("Enter the withdrawal amount (or enter 0 to exit): ")
    if amount == 0:
        exit_opt = input("You've entered 0. Do you want to exit? (y/n)\t: ").lower()
        if exit_opt == 'y':
            print("Program terminated.")
            break
        else:
            continue
    rem_bal = rem(amount)               #  call the function "rem" with the given amount and store the result in "rem_bal"
    if rem_bal == 'Insufficient funds':
        print(rem_bal)
        continue_option = input("Insufficient funds. Do you want to try with another amount? (y/n): ").lower()
        if continue_option != 'y':
            print("Program terminated.")
            break
    else:
        print(f"Remaining balance: {rem_bal}")
