"""
-------------------------------------------------------
[filename].py
[description of main program]
-------------------------------------------------------
Author:  Mason Cooper
ID:      140328200
Email:   coop8200@mylaurier.ca
Version: 2015-02-26
-------------------------------------------------------
"""
from priority_queue_array import PriorityQueue
def prims(g, node):
    """
    -------------------------------------------------------
    an exmplar of prims algorithum
    -------------------------------------------------------
    Preconditions:
       g -  a graph to be navigated
       node - a node to start on, in the graph
    Postconditions:
       prints:
       final - a list of how to navigate the graph at the lowest distance
    -------------------------------------------------------
    """
    final = []
    activated =[]
    pq = PriorityQueue()
    done = False
    first_node = g.get_edges(node)
    for i in range(len(first_node)):
        pq.insert(first_node[i])
    while not done:
        lowest = pq.remove()
        if lowest.end not in activated or lowest.start not in activated:
            activated.append(lowest.start)
            activated.append(lowest.end)
            final.append(lowest)
            node = lowest.end
            next_node = g.get_edges(node)
            for i in range(len(next_node)):
                pq.insert(next_node[i])
        if pq.is_empty() == True:
            done = True
    for i in range(len(final)):
        print(final[i])