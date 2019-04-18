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
import prims
import graph
"""
-------------------------------------------------------
Main Program
-------------------------------------------------------
"""
print("First Test")
edges = (('A', 'B', 2), ('A', 'C', 3), ('A', 'D', 7), ('B', 'C', 6),
          ('B', 'G', 4), ('C', 'E', 1), ('C', 'F', 8), ('D', 'E', 5),
          ('E', 'F', 4), ('F', 'G', 2))
g = graph.Graph(edges)
prims.prims(g, "A")
print()
print("Second Test")
edges = (('A', 'B', 3), ('A', 'C', 3), ('B', 'C', 3),
          ('B', 'H', 6), ('C', 'D', 2), ('D', 'E', 8),
          ('D', 'G', 7), ('E', 'F', 7), ('F', 'G', 5),
          ('F', 'H', 3), ('H', 'I', 4),)
g = graph.Graph(edges)
prims.prims(g, "A")