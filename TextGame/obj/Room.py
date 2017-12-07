class Room:

    def __init__(self, pos, title, desc, exits, items, players, enemies):
        self.pos = [pos[0], pos[1], pos[2]]
        self.title = title
        self.desc = desc
        self.exits = [e for e in exits]
        self.items = [i for i in items]
        self.players = [p for p in players]
        self.enemies = [e for e in enemies]

    def __str__(self):
        obj_str = self.title + '\n' + self.desc + '\n' + self.output_exits() + self.output_items()\
                  + '\n' + str(self.players) + '\n' + str(self.enemies)
        return obj_str

    def output_exits(self):
        exit_list = ''

        for e in self.exits:
            exit_list += e + '\t'

        exit_list += '\n'

        return exit_list

    def output_items(self):
        item_list = ''

        for i in self.items:
            item_list += '+ ' + i + '\n'

        item_list += '\n'

        return item_list
