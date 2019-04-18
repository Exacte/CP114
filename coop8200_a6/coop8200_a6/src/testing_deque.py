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
"""
-------------------------------------------------------
Main Program
-------------------------------------------------------
"""
d = Deque()
testing = [1, "a", 2, "b", 3, "c"]
for i in range (len(list)):
    d.insert_rear(list[i])
for i in range (5):   
    print("***********")
    print(d.remove_rear())
d.print_i()