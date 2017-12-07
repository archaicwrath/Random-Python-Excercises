import Room as room
import Portal as portal
import random as rand
import math


class Map:

    def __init__(self, size, rooms, iconset):
        self.size = size
        self.iconset = iconset
        self.length = rand.randint(math.floor(size/2), size)
        self.width = rand.randint(math.floor(size/2), size)
        self.grid = [[self.iconset[0] for i in range(self.length)] for j in range(self.width)]
        self.rooms = [room.Room(rand.randint(math.floor(size/20), math.floor(size/8)), rand.randint(1, 6), self.iconset[1]) for i in range(rooms)]
        self.positions = [[rand.randint(math.floor(self.width/10), math.floor(self.width - self.width/10)), rand.randint(math.floor(self.length/10), math.floor(self.length - self.length/10))] for i in range(rooms)]
        self.ingress = portal.Portal(self.positions[0], iconset[2], 'Ingress')
        self.egress = portal.Portal(self.positions[len(self.positions)-1], iconset[3], 'Egress')

    def populate_map(self):
        for r in self.rooms:
            for i in range(r.length):
                for j in range(r.width):
                    try:
                        self.grid[self.positions[self.rooms.index(r)][0] + j][self.positions[self.rooms.index(r)][1] + i] = r.icon
                    except IndexError:
                        pass
        self.grid[self.ingress.position[0]][self.ingress.position[1]] = self.ingress.icon
        self.grid[self.egress.position[0]][self.egress.position[1]] = self.egress.icon

    def return_grid(self):
        return self.grid
