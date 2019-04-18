"""
-------------------------------------------------------
rbt_linked.py
-------------------------------------------------------
Author:  Mason Cooper
ID:    140328200
Email:   coop8200@mylaurier.ca
Version: 2013-03-13
-------------------------------------------------------
Linked class version of the RBT ADT.
-------------------------------------------------------
"""
import copy

class _RBTNode:

    def __init__(self, parent, value):
        """
        -------------------------------------------------------
        Creates a node containing a copy of value.
        Use: node = _RBTNode( value )
        -------------------------------------------------------
        Preconditions:
            value - data for the node (?)
        Postconditions:
            Initializes a RBT node containing value. Child pointers are None,
            height is 1, black height is 0, colour is red.
        -------------------------------------------------------
        """
        self._value = copy.deepcopy(value)
        self._left = None
        self._right = None
        self._height = 1
        self._black_height = 0
        self._parent = parent
        self._colour = RBT.RED
        return

    def _update_height(self):
        """
        -------------------------------------------------------
        Updates the height of the current node.
        Assumes that left and right black heights are the same
        (which they must be for a valid RBT)
        Use: b = node._update_height()
        -------------------------------------------------------
        Postconditions:
            returns:
            True if node height has been changed, False otherwise.
            _height is 1 plus the maximum of the node's two children.
        -------------------------------------------------------
        """
        old_height = self._height

        if self._left is None:
            left_height = 0
        else:
            left_height = self._left._height

        if self._right is None:
            right_height = 0
        else:
            right_height = self._right._height

        self._height = max(left_height, right_height) + 1
        return self._height != old_height

    def _update_black_height(self):
        """
        -------------------------------------------------------
        Updates the black height of the current node.
        Assumes that left and right black heights are the same
        (which they must be for a valid RBT)
        Use: b = node._update_black_height()
        -------------------------------------------------------
        Postconditions:
            returns:
            True if node black height has been changed, False otherwise.
            If the node is black, its black height is the black height of
            its children plus 1. If the node is red its black height is the
            black height of its children.
        -------------------------------------------------------
        """
        old_height = self._black_height

        if self._left is None:
            black_height = 0
        else:
            black_height = self._left._black_height

        if self._colour == RBT.RED:
            self._black_height = black_height
        else:
            self._black_height = black_height + 1
        return self._black_height != old_height

    def __str__(self):
        """
        -------------------------------------------------------
        Prints node height and value - for debugging.
        -------------------------------------------------------
        """
        return "h: {}, c: {}, v: {}".format(
                    self._height, RBT.COLOURS[self._colour], self._value)

class RBT:
    BLACK = 0
    RED = 1
    COLOURS = ("Black", "Red")

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty RBT.
        Use: rbt = RBT()
        -------------------------------------------------------
        Postconditions:
            Initializes an empty rbt.
        -------------------------------------------------------
        """
        self._root = None
        self._count = 0
        return

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if rbt is empty.
        Use: b = rbt.is_empty()
        -------------------------------------------------------
        Postconditions:
            returns:
            True if rbt is empty, False otherwise (boolean)
        -------------------------------------------------------
        """
        return self._root is None

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the number of nodes in the RBT.
        Use: n = len( rbt )
        -------------------------------------------------------
        Postconditions:
            returns:
            the number of nodes in rbt (int)
        -------------------------------------------------------
        """
        return self._count

    def insert(self, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into the rbt.
        Use: b = rbt.insert( value )
        -------------------------------------------------------
        Preconditions:
            value - data to be inserted into the rbt (?)
        Postconditions:
            returns:
            inserted - True if value is inserted into the RBT,
            False otherwise. Values may appear only once in a tree. (boolean)
        -------------------------------------------------------
        """
        self._root, inserted = self._insert_aux(self._root, None, value)
        # The root must always be black.
        self._root._colour = RBT.BLACK
        self._root._update_black_height()
        return inserted

    def _insert_aux(self, node, parent, value):
        """
        -------------------------------------------------------
        Inserts a copy of _value into node.
        Private recursive operation called only by insert.
        Use: node, inserted = self._insert_aux( node, value )
        -------------------------------------------------------
        Preconditions:
            node - a rbt node (_RBTNode)
            parent - the parent of node (_RBTNode)
            value - data to be inserted into the node (?)
        Postconditions:
            returns:
            node - the current node (_RBTNode)
            inserted - True if value is inserted into the RBT,
            False otherwise. Values may appear only once in a tree. (boolean)
        -------------------------------------------------------
        """
        if node is None:
            # Base case: add a new node containing the value.
            node = _RBTNode(parent, value)
            self._count += 1
            inserted = True
        elif value < node._value:
            # General case: check the left subtree.
            node._left, inserted = self._insert_aux(node._left, node, value)
        elif value > node._value:
            # General case: check the right subtree.
            node._right, inserted = self._insert_aux(node._right, node, value)
        else:
            # Base case: value is already in the RBT.
            inserted = False

        if inserted:
            # Restructure the node if necessary.
            node = self._restructure(node)
        return node, inserted

    def retrieve(self, key):
        """
        -------------------------------------------------------
        Retrieves a copy of a value matching key in a RBT. (Iterative)
        Use: v = rbt.retrieve( key )
        -------------------------------------------------------
        Preconditions:
            key - data to search for (?)
        Postconditions:
            returns:
            value - value in the node containing key, otherwise None (?)
        -------------------------------------------------------
        """
        node = self._root
        value = None

        while node is not None and value is None:

            if key < node._value:
                node = node._left
            elif key > node._value:
                node = node._right
            else:
                value = copy.deepcopy(node._value)
        return value

    def _is_red(self, node):
        """
        -------------------------------------------------------
        Determines whether a node is coloured red. (Empty nodes are black.)
        Private helper operation.
        Use: b = self._is_red(node)
        -------------------------------------------------------
        Preconditions:
            node - the node to test for red (_RBTNode)
        Postconditions:
          returns:
          True if node is red, False otherwise (boolean)
        -------------------------------------------------------
        """
        return node is not None and node._colour == RBT.RED

    def _restructure(self, node):
        """
        -------------------------------------------------------
        Restructures a subtree upon insertion of a new node.
        Private helper operation.
        Use: node = self._restructure(node)
        -------------------------------------------------------
        Preconditions:
            node - the node to restructure (_RBTNode)
        Postconditions:
            returns:
            node - the node that replaces the original node (_RBTNode)
        -------------------------------------------------------
        """
        # Update the node height if any of its children have been changed.
        if node._update_height():
            # Node height changes only if parent of inserted node is red.
            # Therefore tree must be restructured only if height changes.
            # print("Restructure: {}".format(node._value))
            left_red = self._is_red(node._left)
            right_red = self._is_red(node._right)

            if left_red and right_red:
                # Recolour and fix the black heights of the current node and
                # its children.
                node._colour = RBT.RED
                node._left._colour = RBT.BLACK
                node._right._colour = RBT.BLACK
                node._left._update_black_height()
                node._right._update_black_height()
            elif left_red and self._is_red(node._left._left):
                node = self._rotate_right(node)
            elif left_red and self._is_red(node._left._right):
                # Case 3.
                node._left = self._rotate_left(node._left)
                node = self._rotate_right(node)
            elif right_red and  self._is_red(node._right._right):
                node = self._rotate_left(node)
            elif right_red and self._is_red(node._right._left):
                node._right = self._rotate_right(node._right)
                node = self._rotate_left(node)
        return node

    def _rotate_left(self, node):
        """
        -------------------------------------------------------
        Rotates the pivot to its left around its right child.
        Updates the heights of the rotated nodes.
        Private recursive operation called on restructuring.
        Use: node = self._rotate_left(node)
        -------------------------------------------------------
        Preconditions:
            node - the pivot node to rotate around (_RBTNode)
        Postconditions:
            node - the node that replaces the pivot node (_RBTNode)
        -------------------------------------------------------
        """
        temp = node._right
        node._right = temp._left
        temp._parent = node._parent
        temp._left = node
        node._parent = temp
        # Update the colours.
        node._colour = RBT.RED
        temp._colour = RBT.BLACK
        # Update the heights.
        node._update_height()
        node._update_black_height()
        temp._update_height()
        temp._update_black_height()
        return temp

    def _rotate_right(self, node):
        """
        -------------------------------------------------------
        Rotates the pivot to its right around its left child.
        Updates the heights of the rotated nodes.
        Private recursive operation called on rebalancing.
        Use: node = self._rotate_right(node)
        -------------------------------------------------------
        Preconditions:
            node - the pivot node to rotate around (_RBTNode)
        Postconditions:
            node - the node that replaces the pivot node (_RBTNode)
        -------------------------------------------------------
        """
        temp = node._left
        node._left = temp._right
        temp._parent = node._parent
        temp._right = node
        node._parent = temp
        # Update the colours.
        node._colour = RBT.RED
        temp._colour = RBT.BLACK
        # Update the heights.
        node._update_height()
        node._update_black_height()
        temp._update_height()
        temp._update_black_height()
        return temp

    def __contains__(self, key):
        """
        ---------------------------------------------------------
        Determines if the rbt contains key.
        Use: b = key in rbt
        -------------------------------------------------------
        Preconditions:
            key - a comparable data element (?)
        Postconditions:
            returns:
            True if the rbt contains key, False otherwise (boolean)
        -------------------------------------------------------
        """
        value = self.retrieve(key)
        return value is not None

    def inorder(self):
        """
        -------------------------------------------------------
        Prints the contents of the tree in inorder order.
        Use: rbt.inorder()
        -------------------------------------------------------
        Postconditions:
            prints:
            The contents of the tree are printed inorder.
        -------------------------------------------------------
        """
        self._inorder_aux(self._root)
        return

    def _inorder_aux(self, node):
        """
        ---------------------------------------------------------
        Traverses node subtree in inorder.
        Private recursive operation called only by inorder.
        Use: self._inorder_aux(node)
        ---------------------------------------------------------
        Preconditions:
            node - an RBT node (_RBTNode)
        Postconditions:
            prints:
            The children of node are printed inorder.
        ---------------------------------------------------------
        """
        if node is not None:
            self._inorder_aux(node._left)
            print(node._value)
            self._inorder_aux(node._right)
        return

    def postorder(self):
        """
        -------------------------------------------------------
        Prints the contents of the tree in postorder order.
        Use: rbt.postorder()
        -------------------------------------------------------
        Postconditions:
            prints:
            The contents of the tree are printed postorder.
        -------------------------------------------------------
        """
        self._postorder_aux(self._root)
        return

    def _postorder_aux(self, node):
        """
        ---------------------------------------------------------
        Traverses node subtree in postorder.
        Private recursive operation called only by postorder.
        Use: self._postorder_aux(node)
        ---------------------------------------------------------
        Preconditions:
            node - an RBT node (_RBTNode)
        Postconditions:
            prints:
            The children of node are printed postorder.
        ---------------------------------------------------------
        """
        if node is not None:
            self._postorder_aux(node._left)
            self._postorder_aux(node._right)
            print(node._value)
        return

    def preorder(self):
        """
        -------------------------------------------------------
        Prints the contents of the tree in preorder order.
        Use: rbt.preorder()
        -------------------------------------------------------
        Postconditions:
            prints:
            The contents of the tree are printed preorder.
        -------------------------------------------------------
        """
        self._preorder_aux(self._root)
        return

    def _preorder_aux(self, node):
        """
        ---------------------------------------------------------
        Traverses node subtree in preorder.
        Private recursive operation called only by preorder.
        Use: self._preorder_aux(node)
        ---------------------------------------------------------
        Preconditions:
            node - an RBT node (_RBTNode)
        Postconditions:
            prints:
            The children of node are printed preorder.
        ---------------------------------------------------------
        """
        if node is not None:
            print(node._value)
            self._preorder_aux(node._left)
            self._preorder_aux(node._right)
        return

    def height(self):
        """
        -------------------------------------------------------
        Returns the maximum height of a RBT, i.e. the length of the
        largest path from root to a leaf node in the tree.
        -------------------------------------------------------
        Postconditions:
          Returns maximum height of rbt (int)
        -------------------------------------------------------
        """
        if self._root is None:
            h = 0
        else:
            h = self._root._height
        return h

    def _node_height(self, node):
        """
        ---------------------------------------------------------
        Helper function to determine the height of node - handles empty node.
        Private operation called only by _is_valid_aux.
        Use: h = self._node_height(node)
        ---------------------------------------------------------
        Preconditions:
            node - the node to get the height of (_RBTNode)
        Postconditions:
            returns:
            height - 0 if node is None, node._height otherwise (int)
        ---------------------------------------------------------
        """
        if node is None:
            height = 0
        else:
            height = node._height
        return height

    def _black_height(self, node):
        """
        ---------------------------------------------------------
        Helper function to determine the black height of node - handles
        empty node.
        Private operation called only by _is_valid_aux.
        Use: h = self._black_height(node)
        ---------------------------------------------------------
        Preconditions:
            node - the node to get the black height of (_RBTNode)
        Postconditions:
            returns:
            height - 0 if node is None, node._black_height otherwise (int)
        ---------------------------------------------------------
        """
        if node is None:
            black_height = 0
        else:
            black_height = node._black_height
        return black_height