import random as rand
import math

class Room:

    def __init__(self, size, exits, icon):
        self.icon = icon
        self.size = size
        self.exits = None
        self.length = rand.randint(math.floor(size/2), size)
        self.width = rand.randint(math.floor(size/2), size)
