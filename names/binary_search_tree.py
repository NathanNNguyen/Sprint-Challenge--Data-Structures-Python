"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""

## Recursive: run the function until we reach base case
## Basecase: usually where `code` does what we need
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # take the current value of our node (self.value)
        # compare to the value we want to insert
        
        ## BASE CASES
        # if value < self.value and self.left is None:
        #     self.left = BSTNode(value)
        # if value >= self.value and self.right is None:
        #     self.right = BSTNode(value)

        # if value < self.value
            # IF self.left is already taken by a node
                # make that (left) node call insert
            # set the left to the new node with the new value
        if value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BSTNode(value)

        # if value > self.value
            # IF self.right is already taken by a node
                # make that (right) node call insert
            # set the right to the new node with the new value
        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BSTNode(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # Base case
        if self.value == target:
            return True

        # compare the target to current value
        # if target is less than current value
        if target < self.value:
            # check the left subtree (self.left.contains(target))
            # if you cannot go left, return False
            # Base case
            if self.left is None:
                return False

            return self.left.contains(target)

        # if target is greater than current value
        if target > self.value:
            # check if right subtree contains target
            # if you cannot go right, return False
            # Base case
            if self.right is None:
                return False

            return self.right.contains(target)
        
    # Return the maximum value found in the tree
    def get_max(self):
        # largest value will always be on the right
        # if we can't go right, return the current value
        # Base case
        if self.right is None:
            return self.value

        # if we can go right, call get_max on the right subtree
        max_value = self.right.get_max()  
                  
        return max_value

        # current = self

        # while current.right is not None:
        #     current = current.right

        # return current.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # call the function on current value fn(self.value)
        fn(self.value)

        # if we can go right, call for_each on the right subtree
        if self.right:
            self.right.for_each(fn)

        # if we can go left, call for_each on the left subtree
        if self.left:
            self.left.for_each(fn)
        

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # Lowest value will always be on the left
        # go left first then right
        if node.right:
            node.right.in_order_print(node.right)

        elif node:
            print(self.value)

        # if we can go left, call for_each on the left subtree
        elif node.left:
            node.left.in_order_print(node.left)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # create a queue for nodes
        # add the first node to the queue
        # while queue is not empty
            # get the current node from top of the queue
            # print that node
            # add its children to the queue
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # create a stack for nodes
        stack = []
        # add the first node to the stack
        stack.append(node)
        # while stack is not empty
        while len(stack) > 0:
            # get the current node from top of the stack
            current = stack.pop()
            # print that node
            print(current)
            # add its children to the stack
            if current.left:
                stack.append(current.left)
                current.left.dft_print(node)
            # the order we add children will matter
            if current.right:
                stack.append(current.right)
                current.right.dft_print(node)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
