"""
-------------------------------------------------------
avl_linked.py
-------------------------------------------------------
Author:  Mason Cooper
ID:    140328200
Email:   coop8200@mylaurier.ca
Version: 2014-03-13
-------------------------------------------------------
Linked class version of the AVL ADT.
-------------------------------------------------------
"""
import copy
from lib2to3.pytree import Node

class _AVLNode:

    def __init__(self, value):
        """
        -------------------------------------------------------
        Creates a node containing value.
        Use: node = _AVLNode( value )
        -------------------------------------------------------
        Preconditions:
            value - data for the node (?)
        Postconditions:
            Initializes an AVL node containing value. Child pointers are None,
            height is 1.
        -------------------------------------------------------
        """
        self._value = copy.deepcopy(value)
        # New node is initially added at a leaf.
        self._left = None
        self._right = None
        self._height = 1
        return

    def _update_height(self):
        """
        -------------------------------------------------------
        Updates the height of the current node.
        Use: node._update_height()
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

    def _balance(self):
        """
        -------------------------------------------------------
        Returns the difference in height between the left and right children
        of the current node.
        Use: balance = node._balance()
        -------------------------------------------------------
        Postconditions:
            returns:
            balance - difference in height between the left and right children
            of the node. A value of -1, 0, or 1 indicates balance. -2 or less
            the node is unbalanced to the right; 2 or more the node is
            unbalanced to the left. (int)
        -------------------------------------------------------
        """
        if self._left is None:
            left_height = 0
        else:
            left_height = self._left._height

        if self._right is None:
            right_height = 0
        else:
            right_height = self._right._height

        balance = left_height - right_height
        return balance

    def __str__(self):
        """
        -------------------------------------------------------
        Returns a string version of the node. For debugging purposes.
        -------------------------------------------------------
        Postconditions:
            prints:
            the contents of the node in the form "h: height, v: value"
        -------------------------------------------------------
        """
        return "h: {}, v: {}".format(self._height, self._value)

class AVL:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty AVL.
        Use: avl = AVL()
        -------------------------------------------------------
        Postconditions:
            Initializes an empty avl.
        -------------------------------------------------------
        """
        self._root = None
        self._count = 0
        self._comparisons = 0
        return

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if avl is empty.
        Use: b = avl.is_empty()
        -------------------------------------------------------
        Postconditions:
            returns:
            True if avl is empty, False otherwise (boolean)
        -------------------------------------------------------
        """
        return self._root is None

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the number of elements in the AVL tree.
        Use: n = len( avl )
        -------------------------------------------------------
        Postconditions:
            returns:
            the number of values in the AVL tree (int)
        -------------------------------------------------------
        """
        return self._count

    def insert(self, value):
        """
        -------------------------------------------------------
        Inserts a new node containing value into the avl.
        The avl may contain only one copy of a value.
        Use: b = avl.insert(value)
        -------------------------------------------------------
        Preconditions:
            value - the value to insert into the avl (?)
        Postconditions:
            returns:
            inserted - True if value has been inserted into the tree,
            False otherwise.
        -------------------------------------------------------
        """
        self._root, inserted = self._insert_aux(self._root, value)
        return inserted

    def _insert_aux(self, node, value):
        """
        -------------------------------------------------------
        Inserts a new node containing value into a new leaf of the avl.
        The avl may contain only one copy of a value. The tree may be
        rebalanced after the insertion.
        Private recursive operation called only by insert.
        Use: node, inserted = self._insert_aux(node, value)
        -------------------------------------------------------
        Preconditions:
            node - the current node to examine for the existence of
            value (_AVLNode)
            value - the value to insert into the avl (?)
        Postconditions:
            returns:
            node - the current node (_AVLNode)
            inserted - True if value has been inserted into the tree,
            False otherwise (boolean)
        -------------------------------------------------------
        """
        if node is None:
            # Base case: create the new node and increment the node count.
            node = _AVLNode(value)
            self._count += 1
            inserted = True
            self._comparisons += 1
        elif value < node._value:
            # General case: attempt to insert the value to the left.
            node._left, inserted = self._insert_aux(node._left, value)
        elif value > node._value:
            # General case: attempt to insert the value to the right.
            node._right, inserted = self._insert_aux(node._right, value)
        else:
            # Base case: value is already in tree.
            inserted = False

        if inserted:
            # Rebalance the current node if necessary.
            node = self._rebalance(node)
        # Return the node.
        return node, inserted

    def retrieve(self, key):
        """
        -------------------------------------------------------
        Retrieves a value matching key in an AVL. (Iterative)
        Use: v = avl.retrieve( key )
        -------------------------------------------------------
        Preconditions:
            key - data to search for (?)
        Postconditions:
            returns:
            value - the full value matching key, otherwise None (?)
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

    def _rebalance(self, node):
        """
        -------------------------------------------------------
        Rebalances the current node if its children are not balanced.
        Private recursive operation called on insertion and deletion.
        Use: node = self._rebalance(node)
        -------------------------------------------------------
        Preconditions:
            node - the avl node to rebalance (_AVLNode)
        Postconditions:
            node - the avl node that replaces the original node (_AVLNode)
        -------------------------------------------------------
        """
        balance = node._balance()
        
        if balance > 1:
            balance = node._left._balance()
            
            if balance > 1:
                self._rotate_right(node)
                
            elif balance < -1:
                self._rotate_left(node._left)
                self._rotate_right(node)
                
        elif balance < -1:
            balance = node._right._balance()
            
            if balance < -1:
                self._rotate_left(node)
                
            elif balance > 1:
                self._rotate_right(node._right)
                self._rotate_left(node)
                
        return node

    def _rotate_left(self, node):
        """
        -------------------------------------------------------
        Rotates the pivot to its left around its right child.
        Updates the heights of the rotated nodes.
        Private recursive operation called on rebalancing.
        Use: node = self._rotate_left(node)
        -------------------------------------------------------
        Preconditions:
            node - the pivot node to rotate around (_AVLNode)
        Postconditions:
            node - the node that replaces the pivot node (_AVLNode)
        -------------------------------------------------------
        """
        temp = node
        node = node._right
        temp._right = node._left
        node._left = temp
        node._update_height()
        return node

    def _rotate_right(self, node):
        """
        -------------------------------------------------------
        Rotates the pivot to its right around its left child.
        Updates the heights of the rotated nodes.
        Private recursive operation called on rebalancing.
        Use: node = self._rotate_right(node)
        -------------------------------------------------------
        Preconditions:
            node - the pivot node to rotate around (_AVLNode)
        Postconditions:
            node - the node that replaces the pivot node (_AVLNode)
        -------------------------------------------------------
        """
        temp = node
        node = node._left
        temp._left = node._right
        node._right = temp
        node._update_height()
        
        return node

    def __contains__(self, key):
        """
        ---------------------------------------------------------
        Determines if the AVL contains key.
        Use: b = key in avl
        -------------------------------------------------------
        Preconditions:
            key - a comparable data element (?)
        Postconditions:
            returns:
            True if the AVL contains key, False otherwise (boolean)
        -------------------------------------------------------
        """
        value = self.retrieve(key)
        return value is not None

    def height(self):
        """
        -------------------------------------------------------
        Returns the height of the AVL.
        Use: h = avl.height()
        -------------------------------------------------------
        Postconditions:
            returns:
            h - the current height of the AVL (int)
        -------------------------------------------------------
        """
        if self._root is None:
            h = 0
        else:
            h = self._root._height
        return h

    def inorder(self):
        """
        -------------------------------------------------------
        Prints the contents of the tree in inorder order.
        Use: avl.inorder()
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
            node - an AVL node (_AVLNode)
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
        Use: avl.postorder()
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
            node - an AVL node (_AVLNode)
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
        Use: avl.preorder()
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
            node - an AVL node (_AVLNode)
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
    
    def traverse(self):
        """
        ---------------------------------------------------------
        Returns the contents of bst in an array in sorted order.
                Use: a = bst.traverse()
        ---------------------------------------------------------
        Postconditions:
          returns:
          a - an array containing the contents of bst in sorted order.
        ---------------------------------------------------------
        """
        a = []
        self._traverse_aux(self._root, a)
        return a

    def _traverse_aux(self, node, a):
        """
        ---------------------------------------------------------
        Traverse the node's subtree in inorder, adding the contents of
        each node to an array
                Use: self._traverse_aux(node, a)
        ---------------------------------------------------------
        Preconditions:
          node - the root of a subtree (_BSTNode)
        Postconditions:
          a - contains the contents of the subtree of node 
                    in sorted order.
        ---------------------------------------------------------
        """
        
        if node != None:
            self._traverse_aux(node._left, a)
            a.append(node._value)
            self._traverse_aux(node._right, a)
        
        return

    def is_valid(self):
        """
        ---------------------------------------------------------
        Determines if an AVL is valid.
        Use: b = avl.is_valid()
        ---------------------------------------------------------
        Postconditions:
            returns:
            valid - True if the tree is an AVL, False otherwise.
        ---------------------------------------------------------
        """
        valid = self._is_valid_aux(self._root)
        return valid

    def _is_valid_aux(self, node):
        """
        ---------------------------------------------------------
        Helper function to determine the AVL validity of node.
        Private operation called only by is_valid.
        Use: b = self._is_valid_aux(node)
        ---------------------------------------------------------
        Preconditions:
            node - the node to check the validity of (_AVLNode)
        Postconditions:
            returns:
            result - True if node is an AVL, False otherwise (boolean)
        ---------------------------------------------------------
        """
        if node is None or (node._left is None and node._right is None):
            # Base case: node is empty or a leaf, so tree must be an AVL.
            result = True
        elif abs(self._node_height(node._left) - \
                 self._node_height(node._right)) > 1:
            # Base case: left or right subtree is too deep.
            print("Height Violation at value: {}".format(node._value))
            result = False
        elif (node._left is not None and node._left._value > node._value) \
            or (node._right is not None and node._right._value < node._value):
            # Base case: does not follow the BST property.
            print("Binary Tree Violation")
            result = False
        else:
            # General case: check the nodes children for validity.
            result = self._is_valid_aux(node._left) and \
                     self._is_valid_aux(node._right)
        return result

    def _node_height(self, node):
        """
        ---------------------------------------------------------
        Helper function to determine the height of node - handles empty node.
        Private operation called only by _is_valid_aux.
        Use: h = self._node_height(node)
        ---------------------------------------------------------
        Preconditions:
            node - the node to get the height of (_AVLNode)
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