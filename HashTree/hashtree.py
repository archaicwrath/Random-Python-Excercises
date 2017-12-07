class Hashtree:

    def __init__(self, size):
        self.size = size
        self.items = [None] * self.size


    def put(self, x):
        index = self.hash(x)
        self.items[index] = x

    def hash(self, x):
        return x % self.size