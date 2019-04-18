"""
-------------------------------------------------------
stack_array.py
-------------------------------------------------------
Author:  MAson Cooper
ID: 140328200
Email:   coop8200@wlu.ca
Version: 2015-01-15
-------------------------------------------------------
Array version of the Stack ADT.
-------------------------------------------------------
"""

import copy

class Stack:
    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty stack. Data is stored in a list.
        Use: s = Stack()
        -------------------------------------------------------
        Postconditions:
          Initializes an empty stack.
        -------------------------------------------------------
        """
        self._values = []
        return

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the size of the stack.
        Use: n = len(s)
        -------------------------------------------------------
        Postconditions:
          Returns the number of values in the stack.
        -------------------------------------------------------
        """
        return len(self._values)

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the stack is empty.
        Use: b = s.is_empty()
        -------------------------------------------------------
        Postconditions:
          Returns True if the stack is empty, False otherwise.
        -------------------------------------------------------
        """
        result = False
        if len(self._values) == 0:
            result = True 

        return result

    def push(self, value):
        """
        -------------------------------------------------------
        Pushes a copy of value onto stack.
        Use: s.push( value )
        -------------------------------------------------------
        Preconditions:
          value - a data element (?)
        Postconditions:
          value is added to the top of the stack.
        -------------------------------------------------------
        """
        self._values.append(copy.deepcopy(value))
        return

    def pop(self):
        """
        -------------------------------------------------------
        Pops and returns the top of stack.
        Use: value = s.pop()
        -------------------------------------------------------
        Postconditions:
          Returns the value at the top of the stack - the value is
          removed from the stack. Returns None if the stack is empty.
        -------------------------------------------------------
        """
        value = None
        if len(self._values) != 0:
            value = self._values.pop()

        return value

    def peek(self):
        """
        -------------------------------------------------------
        Peeks at the top of the stack.
        Use: value = s.peek()
        -------------------------------------------------------
        Postconditions:
          Returns a copy of the value at the top of the stack -
          the value is not removed from stack. Returns None
          if the stack is empty.
        -------------------------------------------------------
        """
        value = None
        if len(self._values) != 0:
            value = copy.deepcopy(self._values[len(self._values)-1])
        return value

    def print_i(self):
        """
        -------------------------------------------------------
        Prints the contents of the stack from bottom to top.
        Use: s.print_i()
        -------------------------------------------------------
        Postconditions:
          Prints each value in the stack from bottom to top.
          Each value starts on a new line.
        -------------------------------------------------------
        """
        for i in range(len(self._values)):
            print(self._values[i])
        return
    
    def combine(self, s2):
        """
        -------------------------------------------------------
        combineds two stacks
        -------------------------------------------------------
        Preconditions:
           s2 - stacks to be beautifully intertwined
        Postconditions:
           returns:
           cs - a combining of stackie goodness
        -------------------------------------------------------
        """
        cs = self._values
        self._values = []
        while len(cs) != 0 or len(s2) != 0:
            if len(cs) != 0:
                self._values.append(copy.deepcopy(cs.pop()))
            if len(s2) != 0:
                self._values.append(copy.deepcopy(s2.pop()))
        return