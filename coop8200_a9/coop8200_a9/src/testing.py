"""
-------------------------------------------------------
[filename].py
[description of main program]
-------------------------------------------------------
Author:  Mason Cooper
ID:      140328200
Email:   coop8200@mylaurier.ca
Version: 2015-03-20
-------------------------------------------------------
"""
from utilities2 import array_to_bst, array_to_avl
from bst_linked import BST
from avl_linked import AVL

bst = BST()
avl = AVL()
a = ['a', 'b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',]
array_to_bst(a, bst)

bst.levelorder()

array_to_avl(a, avl)
print(avl.is_valid())