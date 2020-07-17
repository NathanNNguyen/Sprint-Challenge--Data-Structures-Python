class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        prev = None
        curr = self.head
        while curr:
            # make a nxt node everytime we enter the loop
            nxt = curr.next_node

            # switch the pointer for the curr node
            curr.next_node = prev

            # now let's update our node
            # 1 -> 2 -> 3 ->
            prev = curr
            curr = nxt
            # <- 1 <- 2 -> 3 ->
            # keep going until we finish the loop
        
        # if self.head hit None, set it back to prev
        # and loop is done
        self.head = prev