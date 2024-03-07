            
 San Francisco Bay University

Python Programming
Homework Assignment #3
Due day: 3/8/2024

Instruction: 

1. Push the source code to GitHub or answer sheet in word file.
2. Please follow the code style rule like programs on handout.
3. Overdue homework submission could not be accepted.
4. Takes academic honesty and integrity seriously (Zero Tolerance of Cheating & Plagiarism)


1.	Write a high order function to make withdrawal from the balance in bank account by nonlocal variable.

def mk_wd(balance):
    """
    Return the balance after withdrawal since inception
    >>> rem = mk_wd (100)         # deposit $100 
    >>> rem(10)
    90
    >>> rem (20)
    70
    >>> rem (100)
   'Insufficient funds'
   """


2.	Write a function that deletes all instances of an element from a list. 

def  rm_all(elem, lst): 
""" 
>>> x = [3, 1, 2, 1, 5, 1, 1, 7] 
>>> rm_all (1, x) 
>>> x 
[3, 2, 5, 7] 
"""


3. Write a function that takes in three arguments x, elem, and a list, and adds as many "elem"s to the end of the list as there are x’s. 

def add_many(x, elem, lst): 
""" 
Adds elem to the end of lst the number of times x occurs in lst. 
>>> lst = [1, 2, 4, 2, 1] 
>>> add_many (2, 5, lst) 
>>> lst 
[1, 2, 4, 2, 1, 5, 5] 
"""


4. Write a function to create a new list from given a "suits" list and a number list

def  f (suits, numbers):
"""Creates a new list (2-element list as one element in a new list) with the given suits and numbers. Each element in the returned list should be of the form [suit, number].
    >>> f (['S', 'C'], [1, 2, 3])
    [['S', 1], ['S', 2], ['S', 3], ['C', 1], ['C', 2], ['C', 3]]
    >>> f (['S', 'C'], [3, 2, 1])
    [['S', 3], ['S', 2], ['S', 1], ['C', 3], ['C', 2], ['C', 1]]
    >>> f ([], [3, 2, 1])
    []
    >>> f (['S', 'C'], [])
    []
"""


5. Write a function to merge 2 sorted lists a and b, and then return a new list with a sorted order by RECURSIVE calls.

def mrg(ls1, ls2):
    """Merges two sorted lists recursively.

    >>> mrg ([1, 3, 5], [2, 4, 6])
    [1, 2, 3, 4, 5, 6]
    >>> mrg ([], [2, 4, 6])
    [2, 4, 6]
    >>> mrg ([1, 2, 3], [])
    [1, 2, 3]
    >>> mrg ([5, 7], [2, 4, 6])
    [2, 4, 5, 6, 7]
    """


6. Write the function to flatten the deep list.

def fltn(ls):
    """Return a new version of list as follows.

    >>> fltn ([1, 2, 3])     		# normal list
    [1, 2, 3]
    >>> x = [1, [2, 3], 4]      		# deep list
    >>> fltn (x)
    [1, 2, 3, 4]
    >>> x = [[1, [1, 1]], 1, [1, 1]] 	# deep list
    >>> fltn (x)
    [1, 1, 1, 1, 1, 1]
    """


7. Define a function to check if the element exists in the list or not.

def   chk_elm(lst, n): 
"""
>>> a = [ [1,[2]], 3, [ [4], [5,[6] ] ]   ] 
>>> chk_elm (a, 6)
True
"""


8. Write a function to check whether the input argument list is symmetric or not in recursive call.

def sym(l):
    """Returns whether a list is symmetric or not
    >>> sym ([])
    True
    >>> sym ([1])
    True
    >>> sym ([1, 4, 5, 1])
    False
    >>> sym ([1, 4, 4, 1])
    True
    >>> sym (['l', 'o', 'l'])
    True
    """


9. Write a function in recursive call that takes in a list lst, a function g, and an initial value m. This function will fold lst starting at the beginning. If lst is [1, 2, 3, 4, 5] then the function g is applied as follows:

g (g (g (g (g (m, 1), 2), 3), 4), 5)

from operator import add, sub, mul

def fld (lst, g, m):
"""Return the result of applying the function g to the initial value m     and the first element in lst, and repeatedly applying g to this result and the next element in lst until it reaches the end of the list.

    >>> s = [3, 2, 1]
    >>> fld (s, sub, 0)      	# sub(sub(sub(0, 3), 2), 1)
    -6
    >>> fld (s, add, 0)      	# add(add(add(0, 3), 2), 1)
    6
    >>> fld (s, mul, 1)      	# mul(mul(mul(1, 3), 2), 1)
    6

    >>> fld ([], sub, 100)   	# return m if s is empty
    100
    """


10. Implement a function to create 2D array as follows

def   crte_2d_arr(rows, columns):
    """
    >>> crte_2d_arr(3, 5)
    [['-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-']]

    """



