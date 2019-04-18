"""
-------------------------------------------------------
[filename].py
[description of main program]
-------------------------------------------------------
Author:  Mason Cooper
ID:      140328200
Email:   coop8200@mylaurier.ca
Version: 2015-03-21
-------------------------------------------------------
"""
# Use any appropriate data structure here.
from list_array import List
# Define the new_slot slot creation function.
new_slot = List

class HashSet:
    """
    -------------------------------------------------------
    Constants.
    -------------------------------------------------------
    """
    _LOAD_FACTOR = 5

    def __init__(self, size):
        """
        -------------------------------------------------------
        Initializes an empty HashSet of _size slots.
        Use: hs = HashSet( slots )
        -------------------------------------------------------
        Precondition:
            _size - number of initial slots in hashset (int > 0)
        Postconditions:
            Initializes an empty HashSet.
        -------------------------------------------------------
        """
        self._size = size
        self._slots = []

        for _ in range(self._size):
            self._slots.append(new_slot())
        self._count = 0
        return

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the number of values in the hashset.
        Use: n = len( hs )
        -------------------------------------------------------
        Postconditions:
            Returns the number of values in the hashset.
        -------------------------------------------------------
        """
        return self._count

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the hashset is empty.
        Use: b = hs.is_empty()
        -------------------------------------------------------
        Postconditions:
            Returns True if the hashset is empty, False otherwise.
        -------------------------------------------------------
        """
        return self._count == 0

    def _find_slot(self, key):
        """
        -------------------------------------------------------
        Returns the slot for a key value.
        Use: list = hs._find_slot( key )
        -------------------------------------------------------
        Postconditions:
            returns:
            slot - list at the position of hash key in self._slots
        -------------------------------------------------------
        """
        hashkey = hash(key) % self._size
        slot = self._slots[hashkey]
        return slot

    def __contains__(self, key):
        """
        ---------------------------------------------------------
        Determines if the hashset contains key.
        Use: b = key in hs
        -------------------------------------------------------
        Preconditions:
            key - a comparable data element (?)
        Postconditions:
            Returns True if the hashset contains key, False otherwise.
        -------------------------------------------------------
        """
        slot = self._find_slot(key)
        return key in slot

    def insert(self, value):
        """
        ---------------------------------------------------------
        Inserts value into the hashset, allows only one copy of value.
        Calls _rehash if the hashset _LOAD_FACTOR is exceeded.
        Use: inserted = hs.insert( value )
        -------------------------------------------------------
        Preconditions:
            value - a comparable data element (?)
        Postconditions:
            returns
            inserted - True if value is inserted, False otherwise.
        -------------------------------------------------------
        """
        inserted = False
        
        hs = self._find_slot(value)
        
        avg = self._count/self._size
        
        if avg > self._LOAD_FACTOR:
            self._rehash()
            
        elif value not in hs:
            hs.append(value)
            self._count += 1
            inserted = True

        return inserted

    def find(self, key):
        """
        ---------------------------------------------------------
        Returns the value identified by key.
        Use: value = hs.find( key )
        -------------------------------------------------------
        Preconditions:
            key - a comparable data element (?)
        Postconditions:
            returns:
            value - if it exists in the hashset, None otherwise.
        -------------------------------------------------------
        """
        slot = self._find_slot(key)
        value = slot.find(key)
        return value

    def remove(self, key):
        """
        ---------------------------------------------------------
        Removes the value matching key from the hashset, if it exists.
        Use: value = hs.remove( key )
        -------------------------------------------------------
        Preconditions:
            key - a comparable data element (?)
        Postconditions:
            returns:
            value - if it exists in the hashset, None otherwise.
        -------------------------------------------------------
        """
        value = None
        
        hs = self._find_slot(key)
        
        if key in hs:
            value = hs.remove(key)
            self._count -= 1

        return value

    def _rehash(self):
        """
        ---------------------------------------------------------
        Increases the number of slots in the hashset and reallocates the
        existing data within the hashset to the new table.
        Use: hs._rehash()
        -------------------------------------------------------
        Postconditions:
            Existing data is reallocated amongst the hashset table.
        -------------------------------------------------------
        """
        old_slots = self._slots
        self._slots = []
        self._size = 2*self._size + 1
        for slot in range(self._slot()):
            self._slots.append(new_slot())
        for slot in old_slots:
            
        
        return

    def print_i(self):
        """
        ---------------------------------------------------------
        Prints the contents of the hashset starting at slot 0.
        Use: hs.print_i()
        -------------------------------------------------------
        Postconditions:
            The contents of the hashset are printed.
        -------------------------------------------------------
        """
        for slot in self._slots:
            slot.print_i()
        return

    def debug(self):
        """
        ---------------------------------------------------------
        Prints the contents of the hashset starting at slot 0,
        showing the slot currently being printed. Used for
        debugging purposes.
        Use: hs.debug()
        -------------------------------------------------------
        Postconditions:
            The contents of the hashset are printed and the slots identified.
        -------------------------------------------------------
        """
        for i in range(self._size):
            print("------------------------")
            print("Slot {}".format(i))
            for x in range(len(self._slots[i])):
                print(self._slots[i][x])
        
        return