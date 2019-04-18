"""
-------------------------------------------------------
[filename].py
[description of main program]
-------------------------------------------------------
Author:  Mason Cooper
ID:      140328200
Email:   coop8200@mylaurier.ca
Version: 2015-02-10
-------------------------------------------------------
"""
import random
class Patron:
    def __init__( self , number, arrival_time, service_length, reject):
        """
        -------------------------------------------------------
        Initializes an empty queue. Data is stored in a list.
        Use: q = Queue()
        -------------------------------------------------------
        Postconditions:
          Initializes an empty queue.
        -------------------------------------------------------
        """
        self.number = number
        self.arrival_time = arrival_time
        self.service_length = service_length
        self.reject = reject
        self.popped_time = None
        
    def rejection(self, chance):
        """
        -------------------------------------------------------
        Initializes an empty queue. Data is stored in a list.
        Use: q = Queue()
        -------------------------------------------------------
        Postconditions:
          Initializes an empty queue.
        -------------------------------------------------------
        """
        result = False
        rnum = random.random()
        if rnum < chance:
            result = True
        return result