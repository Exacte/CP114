"""
-------------------------------------------------------
[filename].py
[description of main program]
-------------------------------------------------------
Author:  Mason Cooper
ID:      140328200
Email:   coop8200@mylaurier.ca
Version: 2015-02-27
-------------------------------------------------------
"""
from deque import Deque
def is_palindrome(the_string):
    """
    -------------------------------------------------------
    [function description]
    -------------------------------------------------------
    Preconditions:
       [parameter name - parameter description (parameter type and constraints)]
    Postconditions:
       [returns: or prints:]
       [return value name - return value description (return value type)] 
    -------------------------------------------------------
    """
    x = 0
    d = Deque()
    for i in range(len(the_string)):
        if the_string[i].isalpha():
            d.insert_front(the_string[i])
    while x < len(the_string)//2:
        first = d.remove_front()
        last = d.remove_rear()
        if first == last:
            value = True
        else:
            value = False
            x = len(the_string)//2
        x += 1
    return value
