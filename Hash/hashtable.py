import math


class HashTable:
    def __init__(self, length):
        self.hash = [None for x in range(length)]

    def __str__(self):
        constStr = ''.join([str(x)+' ' if x is not None else 'None ' for x in self.hash])
        return constStr

    def hashItem(self, item):
        if type(item) is str:
            return math.floor(math.e * sum([ord(x) for x in item])) % len(self.hash)
        elif type(item) is int or float:
            return math.floor(math.e * sum([ord(x) for x in str(item)])) % len(self.hash)
        else:
            return math.floor(math.e * id(item)) % len(self.hash)

    def insertItem(self, hash, item):
        if self.hash[hash] is None:
            self.hash[hash] = item
        else:
            self.insertItem(self.hashItem(hash), item)

    def searchForItem(self, hash, item):
        if self.hash[hash] is item:
            return hash
        else:
            self.searchForItem(self.hashItem(hash), item)