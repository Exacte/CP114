"""
-------------------------------------------------------
[filename].py
[description of main program]
-------------------------------------------------------
Author:  Mason Cooper
ID:      140328200
Email:   coop8200@mylaurier.ca
Version: 2015-03-05
-------------------------------------------------------
"""
import bst_linked
import utilities2

"""
-------------------------------------------------------
Main Program
-------------------------------------------------------
"""
values = [35, 15, 5, 0, 6, 16, 59, 40, 77, 91]
bst = bst_linked.BST()
utilities2.array_to_bst(values, bst)
#bst.remove(59)
#print(bst.traverse())
print(bst.parent_i(59))