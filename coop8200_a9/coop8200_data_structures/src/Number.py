"""
-------------------------------------------------------
number.py
-------------------------------------------------------
Author:  Mason Cooper
ID:    140328200
Email:   coop8200@mylaurier.ca
Version: 2014-03-15
-------------------------------------------------------
"""
class Number:
    """
    -------------------------------------------------------
    Tracks the number of times the comparison functions (__eq__, __lt__, __le__)
    are called.
    Use: print(Number.comparisons)
    Use: Number.comparisons = 0
    -------------------------------------------------------
    """
    comparisons = 0

    def __init__(self, value):
        """
        -------------------------------------------------------
        Creates a Number object.
        -------------------------------------------------------
        Preconditions:
          value - an integer (int)
        Postconditions:
          A Number object containing value is initialized.
        -------------------------------------------------------
        """
        self.value = value
        return

    def __str__(self):
        """
        -------------------------------------------------------
        Creates a formatted string of Number data.
        -------------------------------------------------------
        Postconditions:
          returns:
          the formatted contents of value (str)
        -------------------------------------------------------
        """
        return str(self.value)

    def __eq__(self, rhs):
        """
        -------------------------------------------------------
        Compares this Number against another Number for equality.
        Called by == operator.
        -------------------------------------------------------
        Preconditions:
          rhs - [right hand side] Number to compare to (Number)
        Postconditions:
          returns:
          result - True if value matches, False otherwise (boolean)
        -------------------------------------------------------
        """
        Number.comparisons += 1
        result = self.value == rhs.value
        return result

    def __lt__(self, rhs):
        """
        -------------------------------------------------------
        Determines if this Number comes before another.
        Called by < operator.
        -------------------------------------------------------
        Preconditions:
          rhs - [right hand side] Number to compare to (Number)
        Postconditions:
          returns:
          result - True if this Number precedes rhs,
          False otherwise (boolean)
        -------------------------------------------------------
        """
        Number.comparisons += 1
        result = self.value < rhs.value
        return result

    def __le__(self, rhs):
        """
        -------------------------------------------------------
        Determines if this Number precedes or is or equal to another.
        Called by <= operator.
        -------------------------------------------------------
        Preconditions:
          rhs - [right hand side] Number to compare to (movie)
        Postconditions:
          returns:
          result - True if this Number precedes or is equal to rhs,
          False otherwise (boolean)
        -------------------------------------------------------
        """
        Number.comparisons += 1
        result = self.value <= rhs.value
        return result