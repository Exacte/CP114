"""
-------------------------------------------------------
[filename].py
[description of main program]
-------------------------------------------------------
Author:  Mason Cooper
ID:      140328200
Email:   coop8200@mylaurier.ca
Version: 2015-01-29
-------------------------------------------------------
"""
from stack_array import Stack
def stack_combine(s1, s2):
    """
    -------------------------------------------------------
    combineds two stacks
    -------------------------------------------------------
    Preconditions:
       s1 and s2 - stacks to be beautifully intertwined
    Postconditions:
       returns:
       cs - a combining of stackie goodness
    -------------------------------------------------------
    """
    cs = Stack()
    while s1.is_empty() == False or s2.is_empty() == False:
        if s1.is_empty() == False:
            cs.push(s1.pop())
        if s2.is_empty() == False:
            cs.push(s2.pop())
    return cs.print_i()
    
     
x = [0,1,2,3,4,5]
y = [10,20,30]
s1 = Stack()
s2 = Stack()
for i in range(len(x)):
    s1.push(x[i])
for z in range(len(y)):
    s2.push(y[z])
print(stack_combine(s2, s1))