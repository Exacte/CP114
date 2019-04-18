"""
-------------------------------------------------------
priority_queue_array.py
-------------------------------------------------------
Author:  David Brown
ID:
Email:   dbrown@wlu.ca
Version: 2015-01-20
-------------------------------------------------------
Array version of the Priority Queue ADT.
-------------------------------------------------------
"""
import copy

class PriorityQueue:

    def __init__( self ):
        """
        -------------------------------------------------------
        Initializes an empty priority queue.
        Use: pq = PriorityQueue()
        -------------------------------------------------------
        Postconditions:
          Initializes an empty priority queue.
        -------------------------------------------------------
        """
        self._values = list()

        return

    def __len__( self ):
        """
        -------------------------------------------------------
        Returns the size of priority_queue.
        Use: n = len( pq )
        -------------------------------------------------------
        Postconditions:
          Returns the size of the priority queue.
        -------------------------------------------------------
        """
        return len( self._values )

    def is_empty( self ):
        """
        -------------------------------------------------------
        Determines if priority_queue is empty.
        Use: b = pq.is_empty()
        -------------------------------------------------------
        Postconditions:
          Returns True if priority queue is empty, False otherwise.
        -------------------------------------------------------
        """
        return len( self._values ) == 0

    def insert( self, value ):
        """
        -------------------------------------------------------
        Inserts a copy of value into priority_queue.
        Use: pq.insert( value )
        -------------------------------------------------------
        Preconditions:
          value - a data value (?)
        Postconditions:
          value is added to the priority queue.
        -------------------------------------------------------
        """

        self._values.append(copy.deepcopy(value))
        
        return

    def remove( self ):
        """
        -------------------------------------------------------
        Removes and returns value from priority_queue.
        Use: v = pq.remove()
        -------------------------------------------------------
        Postconditions:
          Returns the highest priority value in the priority queue - 
          the value is removed from the priority queue. Returns None 
          if priority queue is empty.
        -------------------------------------------------------
        """
        value = 0
        top = self._values[0]
        for i in range(len(self._values)):
            if top > self._values[i]:
                top = self._values[i]
                value = i
        value = self._values.pop(value)
        return value

    def peek( self ):
        """
        -------------------------------------------------------
        Peeks at the highest priority value of priority_queue.
        Use: v = pq.peek() 
        -------------------------------------------------------
        Postconditions:
          Returns a copy of the highest priority value in the priority queue - 
          the value is not removed from the priority queue. Returns None 
          if priority queue is empty.
        -------------------------------------------------------
        """

        value = 0
        top = self._values[0]
        for i in range(len(self._values)):
            if top > self._values[i]:
                top = self._values[i]
                value = i
        value = copy.deepcopy(self._values[value])
        return value

    def print_i( self ):
        """
        -------------------------------------------------------
        Prints the contents of the priority queue.
        Use: pq.print_i()
        -------------------------------------------------------
        Postconditions:
          Prints each value in priority_queue in the order stored.
        -------------------------------------------------------
        """
        for i in range( len( self._values ) ):
            print( self._values[i] )
        return