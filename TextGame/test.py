import obj.Room as room


def main():
    room1 = room.Room([0, 0, 0],
                      'A Deceptively Empty Room',
                      'This room is deceptively empty, but not altogether unpleasant.',
                      ['north', 'east', 'south', 'west', 'up', 'down'],
                      ['a Rusty Sword', 'a Broken Shield', 'several Piles of Bones'],
                      ['No Players, Except You'],
                      ['No Enemies'])

    print(room1)

if __name__ == '__main__':
    main()
