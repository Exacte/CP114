"""
-------------------------------------------------------
[filename].py
[description of main program]
-------------------------------------------------------
Author:  Mason Cooper
ID:      140328200
Email:   coop8200@mylaurier.ca
Version: 2015-03-26
-------------------------------------------------------
"""
from utilities2 import array_to_pt
from pt_linked import PT

a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
pt = PT()

array_to_pt(a, pt)

f = open("otoos610.txt", "r", encoding="utf-8")
line = f.readline().strip()
while line != "":
    for i in range(len(line)):
        pt.retrieve(line[i])
    line = f.readline()
f.close()

pt.levelorder()