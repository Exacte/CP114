"""
-------------------------------------------------------
pt_linked.py
-------------------------------------------------------
Author:  Mason Cooper
ID:    140328200
Email:   coop8200@mylaurier.ca
Version: 2014-02-20
-------------------------------------------------------
Linked class version of the pt ADT.
-------------------------------------------------------
"""
import copy

class _PTNode:

    def __init__(self, value):
        """
        -------------------------------------------------------
        Creates a node containing a copy of value.
        Use: node = _ptNode( value )
        -------------------------------------------------------
        Preconditions:
          value - data for the node (?)
        Postconditions:
          Initializes a pt node containing value. Child pointers are None,
          height is 1.
        -------------------------------------------------------
        """
        self._value = copy.deepcopy(value)
        self._left = None
        self._right = None
        self._height = 1
        self._priority = 0
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
        return "h: {}, v: {}, p: {}".format(self._height, self._value, self._priority)

class PT:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty pt.
        Use: pt = pt()
        -------------------------------------------------------
        Postconditions:
          Initializes an empty pt.
        -------------------------------------------------------
        """
        self._root = None
        return

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if pt is empty.
        Use: b = pt.is_empty()
        -------------------------------------------------------
        Postconditions:
          returns:
          True if pt is empty, False otherwise.
        -------------------------------------------------------
        """
        return self._root is None

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the number of nodes in the pt.
        Use: n = len( pt )
        -------------------------------------------------------
        Postconditions:
          returns:
          the number of nodes in the pt.
        -------------------------------------------------------
        """
        return self._count

    def insert(self, value):
        """
        -------------------------------------------------------
        Inserts a new node containing value into the pt.
        The pt may contain only one copy of a value.
        Use: b = pt.insert(value)
        -------------------------------------------------------
        Preconditions:
            value - the value to insert into the pt (?)
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
        Inserts a new node containing value into a new leaf of the pt.
        The pt may contain only one copy of a value. The tree may be
        rebalanced after the insertion.
        Private recursive operation called only by insert.
        Use: node, inserted = self._insert_aux(node, value)
        -------------------------------------------------------
        Preconditions:
            node - the current node to examine for the existence of
            value (_ptNode)
            value - the value to insert into the pt (?)
        Postconditions:
            returns:
            node - the current node (_ptNode)
            inserted - True if value has been inserted into the tree,
            False otherwise (boolean)
        -------------------------------------------------------
        """
        if node is None:
            # Base case: create the new node and increment the node count.
            node = _PTNode(value)
            inserted = True
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
        Retrieves a copy of a value matching key in a pt. (Iterative)
        Use: v = pt.retrieve( key )
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
                node._priority += 1
        if value != None:
            node = self._rebalance(node)
        return  value
    
    def _rebalance(self, node):
        """
        -------------------------------------------------------
        Rebalances the current node if its children are not balanced.
        Private recursive operation called on insertion and deletion.
        Use: node = self._rebalance(node)
        -------------------------------------------------------
        Preconditions:
            node - the pt node to rebalance (_ptNode)
        Postconditions:
            node - the pt node that replaces the original node (_ptNode)
        -------------------------------------------------------
        """
        if (node._left is not None and node._left._priority > node._priority):
            self._rotate_right(node)
        elif (node._right is not None and node._right._priority > node._priority):
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
            node - the pivot node to rotate around (_ptNode)
        Postconditions:
            node - the node that replaces the pivot node (_ptNode)
        -------------------------------------------------------
        """
        temp = node._right
        node._right = temp._left
        temp._left = node
        node = temp
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
            node - the pivot node to rotate around (_ptNode)
        Postconditions:
            node - the node that replaces the pivot node (_ptNode)
        -------------------------------------------------------
        """
        temp = node._left
        node._left = temp._right
        temp._right = node
        node = temp
        node._update_height()
        return node
    
    def __contains__(self, key):
        """
        ---------------------------------------------------------
        Determines if the pt contains key.
        Use: b = key in pt
        -------------------------------------------------------
        Preconditions:
          key - a comparable data element (?)
        Postconditions:
          Returns True if the pt contains key, False otherwise.
        -------------------------------------------------------
        """
        value = self.retrieve(key)
        return value is not None

    def inorder(self):
        """
        -------------------------------------------------------
        Prints the contents of the tree in inorder order.
        Use: pt.inorder()
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
            node - an pt node (_ptNode)
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
        Use: pt.preorder()
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
            node - an pt node (_ptNode)
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
        Use: pt.postorder()
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
            node - an pt node (_ptNode)
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
        Returns the maximum height of a pt, i.e. the length of the
        largest path from root to a leaf node in the tree.
        Use: h = pt.height()
        -------------------------------------------------------
        Postconditions:
          Returns maximum height of pt (int)
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
        Determines whether two pts are identical.
        Use: b = pt.is_identical( rhs )
        -------------------------------------------------------
        Preconditions:
          rhs - another pt (pt)
        Postconditions:
          returns:
          identical - True if this pt contains the same values
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
          node1 - node of the current pt (_ptNode)
          node2 - node of the rhs pt (_ptNode)
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
        Returns the contents of pt in an array in sorted order.
        Use: a = pt.traverse()
        ---------------------------------------------------------
        Postconditions:
            returns:
            a - an array containing the contents of pt in sorted order.
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
            node - root of the current subtree (_ptNode)
            a - target of sorted data (list)
        Postconditions:
            a contains the contents of node and its children in sorted order.
        ---------------------------------------------------------
        """
        if node is not None:
            self._traverse_aux(node._left, a)
            a.append(node._priority)
            self._traverse_aux(node._right, a)
        return

    def parent_i(self, key):
        """
        ---------------------------------------------------------
        Returns the value of the parent node of a key node in a pt.
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
        Returns the number of leaves (nodes with no children) in pt.
        Use: n = pt.leaf_count()
        (Recursive algorithm)
        ---------------------------------------------------------
        Postconditions:
          returns:
          n - number of nodes with no children in pt.
        ---------------------------------------------------------
        """
        n = self._leaf_count_aux(self._root)
        return n

    def _leaf_count_aux(self, node):
        """
        ---------------------------------------------------------
        Returns the number of leaves (nodes with no children) in pt.
        Use: n = pt.leaf_count()
        (Recursive algorithm)
        ---------------------------------------------------------
        Preconditions:
          node - a PT node (_PTNode)
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
        Use: pt.levelorder()
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
    
    def is_valid(self):
        """
        ---------------------------------------------------------
        Determines if pt is valid.
        Use: b = pt.is_valid()
        ---------------------------------------------------------
        Postconditions:
            returns:
            valid - True if the tree is a PriorityTree, False otherwise.
        ---------------------------------------------------------
        """
        valid = self._is_valid_aux(self._root)
        return valid

    def _is_valid_aux(self, node):
        """
        ---------------------------------------------------------
        Helper function to determine the PriorityTree validity of node.
        Private operation called only by is_valid.
        Use: b = self._is_valid_aux(node)
        ---------------------------------------------------------
        Preconditions:
            node - the node to check the validity of (_PTNode)
        Postconditions:
            returns:
            result - True if node is a PriorityTree, False otherwise (boolean)
        ---------------------------------------------------------
        """
        if node is None:
            result = True
        elif (node._left is not None and node._left._priority > node._priority) \
            or (node._right is not None and node._right._priority > node._priority):
            print("Priority Violation at: {}".format(node._value))
            result = False
        elif (node._left is not None and node._left._value > node._value) \
            or (node._right is not None and node._right._value < node._value):
            print("Binary Tree Violation at {}".format(node._value))
            result = False
        else:
            result = self._is_valid_aux(node._left) and \
                self._is_valid_aux(node._right)
        return result