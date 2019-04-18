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

x = [0,1,2,3,4,5]
y = [10,20,30]
s1 = Stack()
s2 = Stack()
for i in range(len(x)):
    s1.push(x[i])
for z in range(len(y)):
    s2.push(y[z])
s1.combine(s2)
print(s1.print_i())