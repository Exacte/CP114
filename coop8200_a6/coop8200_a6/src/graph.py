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
class Edge:

    def __init__(self, start, end, distance):
        """
        -------------------------------------------------------
        Initializes an Edge object.
        Use: e = Edge( start, end, distance )
        -------------------------------------------------------
        Preconditions:
           start - starting node name (?)
           end - ending node name (?)
           distance - distance between start and end (int > 0)
        Postconditions:
           The edge is initialized.
        -------------------------------------------------------
        """
        self.start = start
        self.end = end
        self.distance = distance
        return

    def __str__(self):
        """
        -------------------------------------------------------
        Returns a string representation of the edge.
        Use: s = str( e ) or print( e )
        -------------------------------------------------------
        Postconditions:
           Returns a string representation of the edge.
        -------------------------------------------------------
        """
        return "{} -> {}: {}".format(self.start, self.end, self.distance)

    def __eq__(self, rhs):
        """
        -------------------------------------------------------
        Compares two edges for equality of distance.
        Use: e == rhs
        -------------------------------------------------------
        Preconditions:
           rhs - another edge (Edge)
        Postconditions:
           Returns whether the distance of two edges are the same.
        -------------------------------------------------------
        """
        return self.distance == rhs.distance

    def __lt__(self, rhs):
        """
        -------------------------------------------------------
        Compares distance of two edges.
        Use: e < rhs
        -------------------------------------------------------
        Preconditions:
           rhs - another edge (Edge)
        Postconditions:
           Returns True if distance of edge < distance of rhs, False otherwise.
        -------------------------------------------------------
        """
        return self.distance < rhs.distance

    def __le__(self, rhs):
        """
        -------------------------------------------------------
        Compares distance of two edges.
        Use: e <= rhs
        -------------------------------------------------------
        Preconditions:
           rhs - another edge (Edge)
        Postconditions:
           Returns True if distance of edge <= distance of rhs,
           False otherwise.
        -------------------------------------------------------
        """
        return self == rhs or self < rhs

class Graph:

    def __init__(self, edges):
        """
        -------------------------------------------------------
        Initializes a Graph object.
        Use: g = Graph( edges )
        -------------------------------------------------------
        Preconditions:
           edges - a tuple of edges of the form (( start, end, distance ), )
        Postconditions:
           The graph is initialized.
        -------------------------------------------------------
        """
        self.nodes = []
        self.edges = {}

        for edge in edges:
            # Process each edge.
            start, end, distance = edge

            if start not in self.nodes:
                # Add node name if not already stored.
                self.nodes.append(start)
                # Initialize list of edges for this node.
                self.edges[start] = []

            if end not in self.nodes:
                # Add node name if not already stored.
                self.nodes.append(end)
                # Initialize list of edges for this node.
                self.edges[end] = []

            # Add the edge to the list of edges for the node.
            self.edges[start].append(Edge(start, end, distance))
            # Add this edge to the edges list for the node at the opposite end.
            self.edges[end].append(Edge(end, start, distance))
        return

    def get_edges(self, node):
        """
        -------------------------------------------------------
        Returns all the edges radiating out from node.
        Use: edges = g.get_edges( node )
        -------------------------------------------------------
        Preconditions:
           node - a node in the graph (?)
        Postconditions:
           Returns a list of all the edges connected with node.
        -------------------------------------------------------
        """
        return self.edges[node]