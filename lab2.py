"""
Author: Jack Sanders
Project: Lab2
Extension Due Date: 11/15/2019
Topic: Implement a Binary Search Tree
"""

class Node(object):
    def __init__(self, data):
        self.parent = None
        self.left = None
        self.right = None
        self.data = data

class Tree(object):
    # Binary Search Tree
    # class constants
    PREORDER = 1
    INORDER = 2
    POSTORDER = 3

    def __init__(self):
        # Do not create any other private variables.
        # You may create more helper methods as needed.
        self.root = None

    def print(self):
        # Print the data of all nodes in order
        self.__print(self.root)

    def __print(self, curr_node):
        # Recursively print a subtree (in order), rooted at curr_node
        if curr_node is not None:
            self.__print(curr_node.left)
            self.__print(curr_node.right)
            print(str(curr_node.data), end=' ')  # save space

    def insert(self, data):
        # Find the right spot in the tree for the new node
        # Make sure to check if anything is in the tree
        # Hint: if a node n is null, calling n.getData() will cause an error
        y = None
        x = self.root
        node = Node(data)
        while x is not None:
            y = x
            if node.data < x.data:
                x = x.left
            else:
                x = x.right
        node.parent = y
        if y is None:
            self.root = node
        elif node.data < y.data:
            y.left = node
        else:
            y.right = node

    def min(self):
        # Returns the minimum value held in the tree
        # Returns None if the tree is empty
        if self.root is None:
            return None
        else:
            tempNode = self.root
            while tempNode.left is not None:
                tempNode = tempNode.left
            return tempNode

    def max(self):
        # Returns the maximum value held in the tree
        # Returns None if the tree is empty
        if self.root is None:
            return None
        else:
            tempNode = self.root
            while tempNode.right is not None:
                tempNode = tempNode.right
            return tempNode

    def __find_node(self, data):
        # returns the node with that particular data value else returns None
        tempNode = self.root
        while tempNode is not None and data is not tempNode.data:
            if data < tempNode.data:
                tempNode = tempNode.left
            else:
                tempNode = tempNode.right
        return tempNode

    def contains(self, data):
        # return True of node containing data is present in the tree.
        # otherwise, return False.
        # you may use a helper method __find_node() to find a particular node with the data value and return that node
        return self.__find_node(data) is not None

    def __iter__(self):
        # iterate over the nodes with inorder traversal using a for loop
        return self.inorder()

    def inorder(self):
        # inorder traversal : (LEFT, ROOT, RIGHT)
        return self.__traverse(self.root, Tree.INORDER)

    def preorder(self):
        # preorder traversal : (ROOT, LEFT, RIGHT)
        return self.__traverse(self.root, Tree.PREORDER)

    def postorder(self):
        # postorder traversal : (LEFT, RIGHT, ROOT)
        return self.__traverse(self.root, Tree.POSTORDER)

    def __traverse(self, curr_node, traversal_type):
        # helper method implemented using generators
        # all the traversals can be implemented using a single method
        if traversal_type == Tree.INORDER:
            if curr_node is not None:
                yield from self.__traverse(curr_node.left, traversal_type)
                yield curr_node.data
                yield from self.__traverse(curr_node.right, traversal_type)
        if traversal_type == Tree.PREORDER:
            if curr_node is not None:
                yield curr_node.data
                yield from self.__traverse(curr_node.left, traversal_type)
                yield from self.__traverse(curr_node.right, traversal_type)
        if traversal_type == Tree.POSTORDER:
            if curr_node is not None:
                yield from self.__traverse(curr_node.left, traversal_type)
                yield from self.__traverse(curr_node.right, traversal_type)
                yield curr_node.data

    def find_successor(self, data):
        # helper method to implement the delete method but may be called on its own
        # if the right subtree of the node is nonempty,then the successor is just 
        # the leftmost node in the right subtree.
        # If the right subtree of the node is empty,then go up the tree until a node that is
        # the left child of its parent is encountered.
        if self.root is None:
            raise(KeyError)
        else:
            x = self.__find_node(data)
            if x.right is not None:
                tempNode = x.right
                while tempNode.left is not None:
                    tempNode = tempNode.left
                return tempNode
            y = x.parent
            while y is not None and x == y.right:
                x = y
                y = y.parent
            return y

    def transplant(self, uNode, vNode):
        if uNode.parent is None:
            self.root = vNode
        elif uNode == uNode.parent.left:
            uNode.parent.left = vNode
        else:
            uNode.parent.right = vNode
        if vNode is not None:
            vNode.parent = uNode.parent

    def delete(self, data):
        # Find the node to delete.
        # If the value specified by delete does not exist in the tree, then don't change the tree.
        # If you find the node and ...
        #  a) The node has no children, just set it's parent's pointer to Null.
        #  b) The node has one child, make the nodes parent point to its child.
        #  c) The node has two children, replace it with its successor, and remove
        #       successor from its previous location.
        # Recall: The successor of a node is the left-most node in the node's right subtree.
        # Hint: you may want to write a new method, findSuccessor() to find the successor when there are two children

        if self.root is None:
            return
        else:
            z = self.__find_node(data)
            y = self.find_successor(data)
            if z is None:
                return
            else:
                if z.left is None:
                    self.transplant(z, z.right)
                elif z.right is None:
                    self.transplant(z, z.left)
                else:
                    if y.parent != z:
                        self.transplant(y, y.right)
                        y.right = z.right
                        y.right.parent = y
                    self.transplant(z, y)
                    y.left = z.left
                    y.left.parent = y
