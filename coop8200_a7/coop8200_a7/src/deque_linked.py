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
import copy

class _DequeNode:

    def __init__(self, value, prev_node, next_node):
        """
        -------------------------------------------------------
        Initializes a deque node.
        Use: node = _dequeNode(value, prev_node, next_node)
        -------------------------------------------------------
        Preconditions:
          value - data value for node (?)
          prev_node - another deque node (_DequeNode)
          next_node - another deque node (_DequeNode)
        Postconditions:
          Initializes a deque node that contains a copy of value
          and links to the previous and next nodes in the deque.
        -------------------------------------------------------
        """
        self._value = copy.deepcopy(value)
        self._prev = prev_node
        self._next = next_node
        return

class Deque:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty deque.
        Use: d = deque()
        -------------------------------------------------------
        Postconditions:
          Initializes an empty deque.
        -------------------------------------------------------
        """
        self._front = None
        self._rear = None
        self._count = 0
        return

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the deque is empty.
        Use: b = d.is_empty()
        -------------------------------------------------------
        Postconditions:
          Returns True if the deque is empty, False otherwise.
        -------------------------------------------------------
        """
        return self._count == 0

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the size of the deque.
        Use: n = len( d )
        -------------------------------------------------------
        Postconditions:
          Returns the number of values in the deque.
        -------------------------------------------------------
        """
        return self._count

    def insert_front(self, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into the front of the deque.
        Use: d.insert_front( value )
        -------------------------------------------------------
        Preconditions:
          value - a data element (?)
        Postconditions:
          value is added to the front of the deque.
        -------------------------------------------------------
        """
        node = _DequeNode(value, None, self._front)

        if self._front is None:
            self._rear = node
        else:
            self._front._prev = node
        self._front = node
        self._count += 1
        return

    def insert(self, value):
        self.insert_front(value)
        return

    def insert_rear(self, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into the rear of the deque.
        Use: d.insert_rear( value )
        -------------------------------------------------------
        Preconditions:
          value - a data element (?)
        Postconditions:
          value is added to the rear of the deque.
        -------------------------------------------------------
        """
        node = _DequeNode(value, self._rear, None)

        if self._rear is None:
            self._front = node
        else:
            self._rear._next = node
        self._rear = node
        self._count += 1
        return

    def remove_front(self):
        """
        -------------------------------------------------------
        Removes and returns value from the front of the deque.
        Use: v = d.remove_front()
        -------------------------------------------------------
        Postconditions:
          returns:
          value - the value at the front of deque - the value is
          removed from deque. Returns None if deque is empty (?)
        -------------------------------------------------------
        """
        if self._front is None:
            value = None
        else:
            value = self._front._value
            self._front = self._front._next
            self._count -= 1

            if self._front is None:
                self._rear = None
            else:
                self._front._prev = None
        return value

    def remove_rear(self):
        """
        -------------------------------------------------------
        Removes and returns value from the rear of the deque.
        Use: v = d.remove_rear()
        -------------------------------------------------------
        Postconditions:
          returns:
          value - the value at the rear of deque - the value is
          removed from deque. Returns None if deque is empty (?)
        -------------------------------------------------------
        """
        if self._rear is None:
            value = None
        else:
            value = self._rear._value
            self._rear = self._rear._prev
            self._count -= 1

            if self._rear is None:
                self._front = None
            else:
                self._rear._next = None
        return value

    def peek_front(self):
        """
        -------------------------------------------------------
        Peeks at the front of deque.
        Use: v = d.peek_front()
        -------------------------------------------------------
        Postconditions:
          returns:
          value - a copy of the value at the front of deque -
          the value is not removed from deque. Returns None
          if deque is empty (?)
        -------------------------------------------------------
        """
        if self._front is None:
            value = None
        else:
            value = copy.deepcopy(self._front._value)
        return value

    def peek_rear(self):
        """
        -------------------------------------------------------
        Peeks at the rear of deque.
        Use: v = d.peek_rear()
        -------------------------------------------------------
        Postconditions:
          returns:
          value - a copy of the value at the rear of deque -
          the value is not removed from deque. Returns None
          if deque is empty (?)
        -------------------------------------------------------
        """
        if self._rear is None:
            value = None
        else:
            value = copy.deepcopy(self._rear._value)
        return value

    def print_r(self):
        """
        -------------------------------------------------------
        Prints the contents of deque from rear to front.
        Use: q.print_r()
        -------------------------------------------------------
        Postconditions:
          Prints each _value in the deque from rear to front.
        -------------------------------------------------------
        """
        current = self._rear

        while current is not None:
            print(current._value)
            current = current._prev
        print()
        return

    def print_f(self):
        """
        -------------------------------------------------------
        Prints the contents of deque from front to rear.
        Use: q.print_f()
        -------------------------------------------------------
        Postconditions:
          Prints each _value in the deque from front to rear.
        -------------------------------------------------------
        """
        current = self._front

        while current is not None:
            print(current._value)
            current = current._next
        print()
        return

    def max(self):
        """
        -------------------------------------------------------
        Finds the maximum value in list.
        Use: v = l.max()
        -------------------------------------------------------
        Postconditions:
          Returns a copy of the first maximum value in the list,
          None if the list is empty.
        -------------------------------------------------------
        """
        if self._front is None:
            max_value = None
        else:
            max_value = self._front._value
            current = self._front._next

            while current is not None:
                if max_value < current._value:
                    max_value = current._value
                current = current._next
            max_value = copy.deepcopy(max_value)
        return max_value
