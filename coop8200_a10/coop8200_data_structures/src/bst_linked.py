"""
-------------------------------------------------------
bst_linked.py
-------------------------------------------------------
Author:  Mason Cooper
ID:    140328200
Email:   coop8200@mylaurier.ca
Version: 2014-02-20
-------------------------------------------------------
Linked class version of the BST ADT.
-------------------------------------------------------
"""
import copy

class _BSTNode:

    def __init__(self, value):
        """
        -------------------------------------------------------
        Creates a node containing a copy of value.
        Use: node = _BSTNode( value )
        -------------------------------------------------------
        Preconditions:
          value - data for the node (?)
        Postconditions:
          Initializes a BST node containing value. Child pointers are None,
          height is 1.
        -------------------------------------------------------
        """
        self._value = copy.deepcopy(value)
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
          _height is 1 plus the maximum of the node's (up to) two children.
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

        self._height = max(left_height, right_height) + 1
        return

    def __str__(self):
        """
        -------------------------------------------------------
        Prints node height and value - for debugging.
        -------------------------------------------------------
        """
        return "h: {}, v: {}".format(self._height, self._value)

class BST:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty BST.
        Use: bst = BST()
        -------------------------------------------------------
        Postconditions:
          Initializes an empty bst.
        -------------------------------------------------------
        """
        self._root = None
        self._count = 0
        self.comparisons = 0
        return

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if bst is empty.
        Use: b = bst.is_empty()
        -------------------------------------------------------
        Postconditions:
          returns:
          True if bst is empty, False otherwise.
        -------------------------------------------------------
        """
        return self._root is None

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the number of nodes in the BST.
        Use: n = len( bst )
        -------------------------------------------------------
        Postconditions:
          returns:
          the number of nodes in the BST.
        -------------------------------------------------------
        """
        return self._count

    def insert(self, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into the bst.
        Use: b = bst.insert( value )
        -------------------------------------------------------
        Preconditions:
          value - data to be inserted into the bst (?)
        Postconditions:
          returns:
          inserted - True if value is inserted into the BST,
          False otherwise. Values may appear only once in a tree. (bool)
        -------------------------------------------------------
        """
        self._root, inserted = self._insert_aux(self._root, value)
        return inserted

    def _insert_aux(self, node, value):
        """
        -------------------------------------------------------
        Inserts a copy of _value into node.
        Private recursive operation called only by insert.
        Use: node, inserted = self._insert_aux( node, value )
        -------------------------------------------------------
        Preconditions:
          node - a bst node (_BSTNode)
          value - data to be inserted into the node (?)
        Postconditions:
          returns:
          node - the current node (_BSTNode)
          inserted - True if value is inserted into the BST,
          False otherwise. Values may appear only once in a tree. (boolean)
        -------------------------------------------------------
        """
        if node is None:
            # Base case: add a new node containing the value.
            node = _BSTNode(value)
            self._count += 1
            inserted = True
        elif value < node._value:
            # General case: check the left subtree.
            node._left, inserted = self._insert_aux(node._left, value)
        elif value > node._value:
            # General case: check the right subtree.
            node._right, inserted = self._insert_aux(node._right, value)
        else:
            # Base case: value is already in the BST.
            inserted = False

        if inserted:
            # Update the node height if any of its children have been changed.
            node._update_height()
        return node, inserted

    def retrieve(self, key):
        """
        -------------------------------------------------------
        Retrieves a copy of a value matching key in a BST. (Iterative)
        Use: v = bst.retrieve( key )
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
            self.comparisons += 1

            if key < node._value:
                node = node._left
            elif key > node._value:
                node = node._right
            else:
                value = copy.deepcopy(node._value)
        return  value

    def remove(self, key):
        """
        -------------------------------------------------------
        Removes a node with a value matching key from the bst.
        Returns the value matched.
        Use: value = bst.remove( key )
        -------------------------------------------------------
        Preconditions:
          key - data to search for (?)
        Postconditions:
          returns:
          value - value matching key if found,
          otherwise returns None. Update structure of bst as required.
        -------------------------------------------------------
        """
        self._root, value = self._remove_aux(self._root, key)
        return value

    def _remove_aux(self, node, key):
        """
        -------------------------------------------------------
        Attempts to find a value matching key in a BST node. Deletes the node
        if found and returns the sub-tree root.
        Private recursive operation called only by remove.
        Use: node, value = self._remove_aux(node, key)
        -------------------------------------------------------
        Preconditions:
          node - a bst node (_BSTNode)
          key - data to search for (?)
        Postconditions:
          returns:
          node - the node to search for key (_BSTNode)
          value - value of node containing key if it exists, None otherwise.
        -------------------------------------------------------
        """
        if node is None:
            # Base Case: the key is not in the tree.
            value = None
        elif key < node._value:
            # Search the left subtree.
            node._left, value = self._remove_aux(node._left, key)
        elif key > node._value:
            # Search the right subtree.
            node._right, value = self._remove_aux(node._right, key)
        else:
            # Value has been found.
            value = node._value
            # Replace this node with another node.
            node = self._delete_node(node)
            self._count -= 1

        if node is not None and value is not None:
            # If the value was found, update the ancestor heights.
            node._update_height()
        return node, value

    def _delete_node(self, node):
        """
        -------------------------------------------------------
        Removes a node from the tree.
        Private operation called only by _remove_aux.
        Use: node = self._delete_node(node)
        -------------------------------------------------------
        Preconditions:
          node - the bst node to be deleted (_BSTNode)
        Postconditions:
          returns:
          node - the node that replaces the deleted node. This node is the node
          with the maximum value in the current node's left subtree (_BSTNode)
        -------------------------------------------------------
        """
        if node._left is None:
            # node has no left children.
            node = node._right
        elif node._right is None:
            # node has no right children.
            node = node._left
        else:
            # node has two children.
            parent = None
            child = node._left

            while child._right is not None:
                # Find the maximum of the left subtree.
                parent = child
                child = child._right

            if parent is not None:
                # Move child left subtree up one level.
                parent._right = child._left
                # Replace left subtree of child with left subtree of node.
                child._left = node._left
                # Update the parent's height.
                parent._update_height()
            # child has no right: replaced by right subtree of node.
            child._right = node._right
            # node is now replaced by child.
            node = child
        return node

    def __contains__(self, key):
        """
        ---------------------------------------------------------
        Determines if the bst contains key.
        Use: b = key in bst
        -------------------------------------------------------
        Preconditions:
          key - a comparable data element (?)
        Postconditions:
          Returns True if the bst contains key, False otherwise.
        -------------------------------------------------------
        """
        value = self.retrieve(key)
        return value is not None

    def inorder(self):
        """
        -------------------------------------------------------
        Prints the contents of the tree in inorder order.
        Use: bst.inorder()
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
            node - an BST node (_BSTNode)
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

    def preorder(self):
        """
        -------------------------------------------------------
        Prints the contents of the tree in preorder order.
        Use: bst.preorder()
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
            node - an BST node (_BSTNode)
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

    def postorder(self):
        """
        -------------------------------------------------------
        Prints the contents of the tree in postorder order.
        Use: bst.postorder()
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
            node - an BST node (_BSTNode)
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

    def height(self):
        """
        -------------------------------------------------------
        Returns the maximum height of a BST, i.e. the length of the
        largest path from root to a leaf node in the tree.
        Use: h = bst.height()
        -------------------------------------------------------
        Postconditions:
          Returns maximum height of bst (int)
        -------------------------------------------------------
        """
        if self._root is None:
            h = 0
        else:
            h = self._root._height
        return h

    def is_identical(self, rhs):
        """
        ---------------------------------------------------------
        Determines whether two BSTs are identical.
        Use: b = bst.is_identical( rhs )
        -------------------------------------------------------
        Preconditions:
          rhs - another bst (BST)
        Postconditions:
          returns:
          identical - True if this bst contains the same values
          in the same order as rhs, otherwise returns False.
        -------------------------------------------------------
        """
        identical = self._is_identical_aux(self._root, rhs._root)
        return identical

    def _is_identical_aux(self, node1, node2):
        """
        ---------------------------------------------------------
        Determines whether two subtrees are identical.
        Use: b = self._is_identical_aux( node1, node2 )
        -------------------------------------------------------
        Preconditions:
          node1 - node of the current BST (_BSTNode)
          node2 - node of the rhs BST (_BSTNode)
        Postconditions:
          returns:
          result - True if this stubtree contains the same values as rhs
          subtree in the same order, otherwise returns False.
        -------------------------------------------------------
        """
        if node1 is None and node2 is None:
            # Reached a bottom of the tree.
            result = True
        elif node1 is not None and node2 is not None and node1._value == node2._value \
        and node1._height == node2._height:
            result = self._is_identical_aux(node1._left, node2._left) \
                and self._is_identical_aux(node1._right, node2._right)
        else:
            result = False
        return result

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
        each node to an array.
        Private recursive operation called only by traverse.
        Use: self._traverse_aux(node, a)
        ---------------------------------------------------------
        Preconditions:
            node - root of the current subtree (_BSTNode)
            a - target of sorted data (list)
        Postconditions:
            a contains the contents of node and its children in sorted order.
        ---------------------------------------------------------
        """
        if node is not None:
            self._traverse_aux(node._left, a)
            a.append(node._value)
            self._traverse_aux(node._right, a)
        return

    def parent_i(self, key):
        """
        ---------------------------------------------------------
        Returns the value of the parent node of a key node in a bst.
        ---------------------------------------------------------
        Preconditions:
          key - a key value (?)
        Postconditions:
          returns:
          value - a copy of the value in a node that is the parent of the
          key node, None if the key is not found.
        ---------------------------------------------------------
        """
        # Find the node containing the key.
        node = self._root
        parent = None
        found = False

        while node is not None and found is False:

            if key < node._value:
                parent = node
                node = node._left
            elif key > node._value:
                parent = node
                node = node._right
            else:
                found = True

        if parent is None or not found:
            value = None
        else:
            value = copy.deepcopy(parent._value)
        return  value

    def leaf_count(self):
        """
        ---------------------------------------------------------
        Returns the number of leaves (nodes with no children) in bst.
        Use: n = bst.leaf_count()
        (Recursive algorithm)
        ---------------------------------------------------------
        Postconditions:
          returns:
          n - number of nodes with no children in bst.
        ---------------------------------------------------------
        """
        n = self._leaf_count_aux(self._root)
        return n

    def _leaf_count_aux(self, node):
        """
        ---------------------------------------------------------
        Returns the number of leaves (nodes with no children) in bst.
        Use: n = bst.leaf_count()
        (Recursive algorithm)
        ---------------------------------------------------------
        Preconditions:
          node - a BST node (_BSTNode)
        Postconditions:
          returns:
          n - number of nodes with no children below node.
        ---------------------------------------------------------
        """
        if node is None:
            count = 0
        elif node._left is None and node._right is None:
            # Base case: node has no children.
            count = 1
        else:
            count = self._leaf_count_aux(node._left) + \
                    self._leaf_count_aux(node._right)
        return count
    
    def levelorder(self):
        """
        -------------------------------------------------------
        Prints the contents of the tree in levelorder order.
        Use: bst.levelorder()
        -------------------------------------------------------
        Postconditions:
          The contents of the tree are printed levelorder.
        -------------------------------------------------------
        """
        levels = [self._root]
        
        print(levels[0]._value)
        print()
        
        while len(levels) != 0:
            for i in range(len(levels)):
                if levels[0]._left != None:
                    levels.append(levels[0]._left)
                if levels[0]._right != None:
                    levels.append(levels[0]._right)
                levels.remove(levels[0])
            for x in range(len(levels)):
                print(levels[x]._value)
            print()
        return