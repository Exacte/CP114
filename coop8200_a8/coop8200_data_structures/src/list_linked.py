"""
-------------------------------------------------------
list_linked.py
-------------------------------------------------------
Author:  David Brown
ID:
Email:   dbrown@wlu.ca
Version: 2015-02-02
-------------------------------------------------------
Linked version of the list ADT.
-------------------------------------------------------
"""
import copy

class _ListNode:

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

class List:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty list.
        Use: l = List()
        -------------------------------------------------------
        Postconditions:
          Initializes an empty list.
        -------------------------------------------------------
        """
        self._front = None
        self._size = 0
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
        return self._size

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
        return self._size == 0

    def insert(self, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into list.
        Use: l.insert( value )
        -------------------------------------------------------
        Preconditions:
          value - a data element (?)
        Postconditions:
          value is added to the list.
        -------------------------------------------------------
        """
        node = _ListNode(value, self._front)
        self._front = node
        self._size += 1
        return

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
        value = None
        if self._size != 0:
            if key == self._front._value:
                self._front = value._next
                value = self._front._value
                self._size -= 1
            else:
                previous = self._front
                current = previous._next
                while current is not None:
                    if key == current._value:
                        value = current._value
                        previous._next = current._next
                    previous = current
                    current = current._next
                self._size -= 1
                    
        return value

    def remove_front(self):
        """
        -------------------------------------------------------
        Removes first node in list.
        Use: value = l.remove_front()
        -------------------------------------------------------
        Postconditions:
          Returns:
          value - the first value in the list, None if the list is empty.
        -------------------------------------------------------
        """
        value = None
        if self._size != 0:
            value = self._front
            self._front = value._next
            self._size -= 1
        return value._value

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

    def index(self, key):
        """
        -------------------------------------------------------
        Returns the position of key in list.
        Use: n = l.index( key )
        -------------------------------------------------------
        Preconditions:
          key - the value to search for (?)
        Postconditions:
          returns n, the distance of key from the front of the list,
          -1 if the key is not in the list
        -------------------------------------------------------
        """
        n = 0
        current = self._front
        while current is not None:
            if key == current._value:
                current = None
            else:
                current = current._next
                n += 1
        if n == self._size:
            n = -1

        return n

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
          is outside the arroy boundaries of the list.
        -------------------------------------------------------
        """
        value = None
        if 0 < n < self._size:
            current = self._front
            count = 0
            while current is not None:
                if count == n:
                    value = copy.deepcopy(current._value)
                    current = None
                else:
                    current = current._next
                count += 1
        return value

    def __contains__(self, key, ):
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
        result = False
        current = self._front
        while current is not None:
            if  key == current._value:
                result = True
                current = None
            else:
                current = current._next

        return result

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
        max_value = 0
        if self._size != 0:
            current = self._front
            max_value = current._next
            while current is not None:
                if current._value > max_value._value:
                    max_value = current
                current = current._next
            max_value = copy.deepcopy(max_value._value)
        return max_value

    def min(self):
        """
        -------------------------------------------------------
        Finds the minimum value in list.
        Use: value = l.min()
        -------------------------------------------------------
        Postconditions:
          Returns a copy of the first minimum value in the list,
          None if the list is empty.
        -------------------------------------------------------
        """
        min_value = 0
        if self._size != 0:
            current = self._front
            min_value = current._next
            while current is not None:
                if current._value > min_value._value:
                    min_value = current
                current = current._next
            min_value = copy.deepcopy(min_value._value)
        return min_value

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

        is_identical = False
        if rhs._size == self._size:
            current = self._front
            rhscurrent = rhs._front
            while current is not None:
                if rhscurrent._value == current._value:
                    rhscurrent = rhscurrent._next
                    current = current._next
                    is_identical = True
                else:
                    is_identical = False
                    current = None

        return is_identical

    def count(self, key):
        """
        -------------------------------------------------------
        Finds the number of times key appears in list.
        Use: n = l.count(key)
        -------------------------------------------------------
        Postconditions:
          Returns the number of times key appears in list..
        -------------------------------------------------------
        """
        number = 0
        current = self._front

        while current is not None:
            if key == current._value:
                number += 1
            current = current._next
        return number