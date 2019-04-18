"""
-------------------------------------------------------
utilities.py
-------------------------------------------------------
Author:  Mason Cooper
ID:      140328200
Email:   coop8200@mylaurier.ca
Version: 2015-01-20
-------------------------------------------------------
"""
def array_to_stack(s, tlist):
    """
    -------------------------------------------------------
    converts a array to a stack
    -------------------------------------------------------
    Preconditions:
       s - a empty stack
       tlist -  a filled list
    Postconditions:
       returns:
       s - a filled stack
    -------------------------------------------------------
    """
    while len(tlist) != 0:
        value = tlist.pop()
        s.push(value)
    return 

def stack_to_array(s, flist):
    """
    -------------------------------------------------------
    converts a stack to an array
    -------------------------------------------------------
    Preconditions:
       s - a filled stack
       flist -  a empty list
    Postconditions:
       returns:
       flist - a filled list
    -------------------------------------------------------
    """
    while s.is_empty() == False:
        value = s.pop()
        flist.append(value)
    return 
def array_to_bst(a, bst):
    """
    -------------------------------------------------------
    puts array into a BST
    -------------------------------------------------------
    Preconditions:
       a - an array
       bst - a binary search tree
    Postconditions:
       returns:
       bst - a binary search tree
    -------------------------------------------------------
    """
    for i in range(len(a)):
        bst.insert(a[i])
    return

def array_to_avl(a, avl):
    """
    -------------------------------------------------------
    puts array into a BST
    -------------------------------------------------------
    Preconditions:
       a - an array
       bst - a binary search tree
    Postconditions:
       returns:
       bst - a binary search tree
    -------------------------------------------------------
    """
    for i in range(len(a)):
        avl.insert(a[i])
    return