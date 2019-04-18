"""
-------------------------------------------------------
processor.py
-------------------------------------------------------
Author:  Mason Cooper
ID:    140328200
Email:   coop8200@mylaurier.ca
Version: 2014-03-01
-------------------------------------------------------
"""
from deque_linked import Deque

class Processor:

    def __init__( self, number ):
        """
        -------------------------------------------------------
        Initializes a processor.
        Use: processor = Processor( number )
        -------------------------------------------------------
        Preconditions:
           number - the processor number (int)
        Postconditions:
           Initializes a Processor object.
        -------------------------------------------------------
        """
        self.number = number
        # Initialize and empty Thread deque.
        self.deque = Deque()
        # There is no current thread running.
        self.thread = None
        # Processor has been doing no work yet.
        self.working = 0
        return

    def __str__( self ):
        """
        -------------------------------------------------------
        Returns a string version of a processor (for debugging)
Use: s = str( processor ) 
        -------------------------------------------------------
        Postconditions:
           returns string, the contents of the processor.
        -------------------------------------------------------
        """
        string = "{}: {} - {}".format( 
            self.number, self.working, self.thread )
        return string

class Thread:

    def __init__( self, number, total_time ):
        """
        -------------------------------------------------------
        Initializes a Thread object.
        Use: thread = Thread( number, total_time )
        -------------------------------------------------------
        Preconditions:
           number - the thread number (int)
           total_time - the total time necessary for the thread to finish
        Postconditions:
           Initializes a Thread object.
        -------------------------------------------------------
        """
        self.number = number
        self.total_time = total_time
        # Time left for thread to finish.
        self.current_time = total_time
        return

    def __str__( self ):
        """
        -------------------------------------------------------
        Returns a string version of a thread (for debugging)
        Use: s = str( thread )
        -------------------------------------------------------
        Postconditions:
           returns string, the contents of the thread.
        -------------------------------------------------------
        """
        string = "{}: {}/{}".format( 
            self.number, self.total_time, self.current_time )
        return string