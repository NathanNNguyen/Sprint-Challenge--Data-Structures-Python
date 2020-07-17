class RingBuffer:
    def __init__(self, capacity):
        # define all the variables we need
        self.capacity = capacity
        self.storage = []
        self.index = 0

    def append(self, item):
        # check if self.storage is able to append items
        if len(self.storage) < self.capacity:
            self.storage.append(item)
        
        # otherwise we have to pop item before inserting new ones
        else:
            # popping and inserting using the same index
            # so the list would stay consistent
            self.storage.pop(self.index)
            self.storage.insert(self.index, item)

            # we need to update index so when we popping
            # inserting, we use the right index
            if self.index + 1 == self.capacity:
                self.index = 0
            else:
                self.index += 1

    def get(self):
        return self.storage