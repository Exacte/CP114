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
import copy

class _DequeNode:

    def __init__(self, value, next_node):
        """
        -------------------------------------------------------
        Initializes a list node.
        Use: node = _ListNode(value, next_node)
        -------------------------------------------------------
        Preconditions:
          _value - data value for node (?)
          _next - another list node (_ListNode)
        Postconditions:
          Initializes a list node that contains a copy of value
          and a link to the next node in the list.
        -------------------------------------------------------
        """
        self._value = copy.deepcopy(value)
        self._next = next_node
        return
    
class Deque:
    
    def __init__( self ):
        """
        -------------------------------------------------------
        [function description]
        -------------------------------------------------------
        Preconditions:
           [parameter name - parameter description (parameter type and constraints)]
        Postconditions:
           [returns: or prints:]
           [return value name - return value description (return value type)] 
        -------------------------------------------------------
        """
        self._front = None
        self._size = 0
        self._rear = None
        self._previous = None
        
        return
    
    
    def __len__( self ):
        """
        -------------------------------------------------------
        [function description]
        -------------------------------------------------------
        Preconditions:
           [parameter name - parameter description (parameter type and constraints)]
        Postconditions:
           [returns: or prints:]
           [return value name - return value description (return value type)] 
        -------------------------------------------------------
        """
        return self._size
        
    def is_empty( self ):
        """
        -------------------------------------------------------
        [function description]
        -------------------------------------------------------
        Preconditions:
           [parameter name - parameter description (parameter type and constraints)]
        Postconditions:
           [returns: or prints:]
           [return value name - return value description (return value type)] 
        -------------------------------------------------------
        """
        return self._size == 0
        
    def insert_front( self, value ):
        """
        -------------------------------------------------------
        [function description]
        -------------------------------------------------------
        Preconditions:
           [parameter name - parameter description (parameter type and constraints)]
        Postconditions:
           [returns: or prints:]
           [return value name - return value description (return value type)] 
        -------------------------------------------------------
        """
        node = _DequeNode(value, self._front)
        self._front = node
        self._size += 1
        if self._size == 0:
            self._rear = node
        self._size += 1
        return
    
        
    def insert_rear(self, value):
        """
        -------------------------------------------------------
        [function description]
        -------------------------------------------------------
        Preconditions:
           [parameter name - parameter description (parameter type and constraints)]
        Postconditions:
           [returns: or prints:]
           [return value name - return value description (return value type)] 
        -------------------------------------------------------
        """
        if self._size == 0:
            self._rear = _DequeNode(value, self._rear)
            self._size += 1
            
        
        else:
            current = self._rear
            self._size += 1
            while current is not None:
                current = current._next
            node = _DequeNode(value, current)
            print(node._value)
            current = node
            
        return
    
        
    def remove_front( self ):
        """
        -------------------------------------------------------
        [function description]
        -------------------------------------------------------
        Preconditions:
           [parameter name - parameter description (parameter type and constraints)]
        Postconditions:
           [returns: or prints:]
           [return value name - return value description (return value type)] 
        -------------------------------------------------------
        """
        current = self._front
        value = None
            
        if self._size != 0:
                
            value = current._value
            self._front = self._front._next
            self._size = self._size - 1
    
        return value
                
            
    def remove_rear( self ):
        """
        -------------------------------------------------------
        [function description]
        -------------------------------------------------------
        Preconditions:
           [parameter name - parameter description (parameter type and constraints)]
        Postconditions:
           [returns: or prints:]
           [return value name - return value description (return value type)] 
        -------------------------------------------------------
        """
        if self._size != 0:
            value = self._rear._value
            current = self._front
            while current is not None:
                self._previous = current
                current = current._next
            self._rear = self._previous
            self._size = self._size - 1
        
        return value
        
    def peek_front( self ):
        """
        -------------------------------------------------------
        [function description]
        -------------------------------------------------------
        Preconditions:
           [parameter name - parameter description (parameter type and constraints)]
        Postconditions:
           [returns: or prints:]
           [return value name - return value description (return value type)] 
        -------------------------------------------------------
        """
        current = self._front
        return copy.deepcopy(current._value)
    
    def peek_rear( self ):
        """
        -------------------------------------------------------
        [function description]
        -------------------------------------------------------
        Preconditions:
           [parameter name - parameter description (parameter type and constraints)]
        Postconditions:
           [returns: or prints:]
           [return value name - return value description (return value type)] 
        -------------------------------------------------------
        """
        current = self._rear
        return copy.deepcopy(current._value)
    
    def print_i(self):
        """
        -------------------------------------------------------
        Prints the contents of list.
        Use: l.print_i()
        -------------------------------------------------------
        Postconditions:
          Prints each value in list.
        -------------------------------------------------------
        """
        current = self._front

        while current is not None:
            print(current._value)
            current = current._next
        return