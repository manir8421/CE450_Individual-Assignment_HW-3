
def crte_2d_arr(rows, columns):    # define function "crte_2d_arr" with parameters rows and columns
    return [['-' for _ in range(columns)] for _ in range(rows)]    # return for  nested list creates 2D list, make list with columns number, outer list repeat the inner list rows times

row_value = input("Type the number/value for 2D array (row)\t: ")
column_value = input("Type the number/value for 2D array (column)\t: ")


try:                       # start try block for error check, of input data, if there no error print output, else, print error
    rows = int(row_value)   
    columns = int(column_value)
    array_2d = crte_2d_arr(rows, columns)   # Call crte_2d_arr function with rows and columns value to get result and store in variable array_2d.
    print("\nOutput is:\n",array_2d)

except ValueError:
    print("Invalid input! Type integer values for rows and columns.")
