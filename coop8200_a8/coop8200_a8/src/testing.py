"""
-------------------------------------------------------
[filename].py
[description of main program]
-------------------------------------------------------
Author:  Mason Cooper
ID:      140328200
Email:   coop8200@mylaurier.ca
Version: 2015-03-10
-------------------------------------------------------
"""
import bst_linked

DATA1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DATA2 = "MFTCJPWADHKNRUYBEIGLOQSVXZ"
DATA3 = "ETAOINSHRDLUCMPFYWGBVKJXZQ"

bst1 = bst_linked.BST()
bst2 = bst_linked.BST()
bst3 = bst_linked.BST()

for i in range(len(DATA1)):
    bst1.insert(DATA1[i])
    bst2.insert(DATA2[i])
    bst3.insert(DATA3[i])

f = open("otoos610.txt", "r", encoding="utf-8")
line = f.readline()
while line != "":
    for i in range(len(line)):
        bst1.retrieve(line[i])
        bst2.retrieve(line[i])
        bst3.retrieve(line[i])
    line = f.readline()
f.close()

print("Comparisons:")
print("data 1: {}".format(bst1.comparisons))
print("data 2: {}".format(bst2.comparisons))
print("data 3: {}".format(bst3.comparisons))

print()
print("********************")
print()

print("Balanced:")
print(bst1.is_balanced())
print(bst2.is_balanced())

print()
print("********************")
print()

print("Node count:")
print("data 2: {}".format(bst2.node_counts()))
print("data 3: {}".format(bst3.node_counts()))