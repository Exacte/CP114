"""
-------------------------------------------------------
list_array.py
-------------------------------------------------------
Author:  Mason cooper
ID:
Email:   coop8200@mylaurier.ca
Version: 2013-01-13
-------------------------------------------------------
Array version of the list ADT.
-------------------------------------------------------
"""
import copy

class List:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty list. Data is stored in a Python list.
        Use: l = List()
        -------------------------------------------------------
        Postconditions:
          Initializes an empty list.
        -------------------------------------------------------
        """
        self._values = []
        return

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the size of the list.
        Use: n = len( l )
        -------------------------------------------------------
        Postconditions:
          Returns the number of values in the list.
        -------------------------------------------------------
        """
        return len(self._values)

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the list is empty.
        Use: b = l.is_empty()
        -------------------------------------------------------
        Postconditions:
          Returns True if the list is empty, False otherwise.
        -------------------------------------------------------
        """
        return len(self._values) == 0

    def append(self, value):
        """
        -------------------------------------------------------
        Appends a copy of value to the end of the list.
        Use: l.append( value )
        -------------------------------------------------------
        Preconditions:
          value - a data element (?)
        Postconditions:
          value is added to the end of the list.
        -------------------------------------------------------
        """

        self._values.append(copy.deepcopy(value))

        return

    def insert_front(self, value):
        """
        -------------------------------------------------------
        Add a copy of value to the front of list.
        Use: l.insert_front( value )
        -------------------------------------------------------
        Preconditions:
          value - a data element (?)
        Postconditions:
          value is added to the list.
        -------------------------------------------------------
        """

        self._values.insert(0, copy.deepcopy(value))

        return

    def _linear_search(self, key):
        """
        -------------------------------------------------------
        Searches for a copy of key in the list.
        Private helper operations - used only by other ADT operations.
        -------------------------------------------------------
        Preconditions:
          key - a data element (?)
        Postconditions:
          Returns i, the index of key in the list, -1
          if key is not found.
        -------------------------------------------------------
        """
        x = True
        i = -1
        if len(self._values) != 0:
            i = 0
            while x == True:
                if self._values[i] == key:
                    x = False
                i += 1
            if i == len(self._values):
                i = -1
                x = False
        
        return i

    def remove(self, key):
        """
        -------------------------------------------------------
        Finds, removes, and returns the value in list that matches key.
        Use: value = l.remove( key )
        -------------------------------------------------------
        Preconditions:
          key - a data element (?)
        Postconditions:
          Returns and removes the full value matching key, otherwise
          returns None.
        -------------------------------------------------------
        """
        
        value = self._linear_search(key)
        if value != -1:
            value = self._values.pop(value)
        else:
            value = None
        
        
        return value
    
    def remove_front(self):
        """
        -------------------------------------------------------
        Removes first node in list.
        Use: value = l.remove_front()
        -------------------------------------------------------
        Postconditions:
            returns:
            value - the first value in the list, None if the list is empty.
        -------------------------------------------------------
        """

        value = None
        if len(self._values) != 0:
            value = self._values.pop(0)

        return value

    def print_i(self):
        """
        -------------------------------------------------------
        Prints the contents of list.
        -------------------------------------------------------
        Postconditions:
          Prints each value in list.
        -------------------------------------------------------
        """
        for i in range(len(self._values)):
            print(self._values[i])
        return

    def index(self, key):
        """
        -------------------------------------------------------
        Finds location of a value by key in list.
        Use: n = l.index( key )
        -------------------------------------------------------
        Preconditions:
          key - a data element (?)
        Postconditions:
          Returns the index of the location of key in the list, -1 if
          key is not in the list.
        -------------------------------------------------------
        """
        
        i = self._linear_search(key)
        
        return i

    def is_identical(self, rhs):
        """
        ---------------------------------------------------------
        Determines whether two lists are identical.
        Use: b = l.is_identical( rhs )
        -------------------------------------------------------
        Preconditions:
          rhs - another list (List)
        Postconditions:
          Returns True if this list contains the same values as rhs
          in the same order, otherwise returns False.
        -------------------------------------------------------
        """
        
        identical = False
        if self._values == rhs:
            identical = True
        
        return identical

    def __getitem__(self, n):
        """
        ---------------------------------------------------------
        Returns a copy of the nth element of the list.
        Use: value = l[n]
        -------------------------------------------------------
        Preconditions:
          n - index of the element to access (int)
        Postconditions:
          Returns the nth element of list if it exists, None if n
          is outside the array boundaries of the list.
        -------------------------------------------------------
        """
        value = None
        if 0<=n < len(self._values):
            value = copy.deepcopy(self._values[n])
        
        return value
    
    def replace(self, n, value):
        """
        ---------------------------------------------------------
        Places a copy of value into the list at position n.
        Use: l.replace( n, value )
        -------------------------------------------------------
        Preconditions:
            n - index of the element to access (int)
            value - a data value (?)
        Postconditions:
            The nth element of list contains value if it exists, and
            returns True. The value being replaced is thrown away. Returns
            false if n is outside the array boundaries of the list.
        -------------------------------------------------------
        """
        
        result = False
        if len(self._values) != 0 and len(self._values) >= n:
            self._values[n] = value
            result = True
        
        return result

    def __contains__(self, key):
        """
        ---------------------------------------------------------
        Determines if the list contains key.
        Use: b = key in l
        -------------------------------------------------------
        Preconditions:
          key - a comparable data element (?)
        Postconditions:
          Returns True if the list contains key, False otherwise.
        -------------------------------------------------------
        """
        
        contains = False
        if self._linear_search(key) != -1:
            contains = True
        
        return contains

    def max(self):
        """
        -------------------------------------------------------
        Finds the maximum value in list.
        Use: value = l.max()
        -------------------------------------------------------
        Postconditions:
          Returns a copy of the first maximum value in the list,
          None if the list is empty.
        -------------------------------------------------------
        """
        
        max_value = None
        if len(self._values) != 0:
            max_value = self._values[0]
            for i in range(len(self._values)):
                if self._values[i] > max_value:
                    max_value = self._values[i]
        
        return max_value

    def min(self):
        """
        -------------------------------------------------------
        Finds the minimum value in list.
        -------------------------------------------------------
        Postconditions:
          Returns a copy of the first minimum value in the list,
          None if the list is empty.
        -------------------------------------------------------
        """
        
        min_value = None
        if len(self._values) != 0:
            min_value = self._values[0]
            for i in range(len(self._values)):
                if self._values[i] < min_value:
                    min_value = self._values[i]
        
        return min_value

    def count(self, key):
        """
        -------------------------------------------------------
        Finds the number of times key appears in list.
        -------------------------------------------------------
        Postconditions:
          Returns the number of times key appears in list..
        -------------------------------------------------------
        """
        number = 0

        for value in self._values:
            if key == value:
                number += 1
        return number

    def reverse(self):
        """
        -------------------------------------------------------
        Reverses the order of the elements in list.
        -------------------------------------------------------
        Postconditions:
          The contents of list are reversed in order with respect
          to their order before the operation was called.
        -------------------------------------------------------
        """
        
        # your code here
        
        return

    def _swap(self, i, j):
        """
        -------------------------------------------------------
        Swaps the position of two elements in the data list.
        Private helper operations called only from within class.
        -------------------------------------------------------
        Preconditions:
          i - index of one element to switch (int, 0 <= i < len(self._values))
          j - index of other element to switch
              (int, 0 <= i < len(self._values))
        Postconditions:
          The element originally at position i is now at position j,
          and visa versa.
        -------------------------------------------------------
        """
        temp = self._values[i]
        self._values[i] = self._values[j]
        self._values[j] = temp
        return