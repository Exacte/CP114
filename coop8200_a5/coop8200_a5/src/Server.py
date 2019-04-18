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
class Server:
    def __init__( self , number, patron):
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
        self.patron = patron
        
    def is_serving(self):
        """
        -------------------------------------------------------
        Initializes an empty queue. Data is stored in a list.
        Use: q = Queue()
        -------------------------------------------------------
        Postconditions:
          Initializes an empty queue.
        -------------------------------------------------------
        """
        result = True
        if self.patron == None:
            result = False
        return result
        
        return
    def serving(self, current_time, patron):
        """
        -------------------------------------------------------
        Initializes an empty queue. Data is stored in a list.
        Use: q = Queue()
        -------------------------------------------------------
        Postconditions:
          Initializes an empty queue.
        -------------------------------------------------------
        """
        result = 0
        if self.patron != None:
            service_time = self.patron.popped_time + self.patron.service_length
            if current_time == service_time:
                print("Server {} finished serving Patron {}".format(self.number, patron.number))
                if patron.rejection(patron.reject) == True:
                    result = 1
                self.patron = None
        else:
            self.patron = patron
            self.patron.popped_time = current_time
        return result