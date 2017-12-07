import Map as map
import random as rand


def main():

    m = map.Map(100, 25, [' ', '█', '▲', '▼'])
    m.populate_map()

    for x in m.return_grid():
        print(''.join(x))


if __name__ == '__main__':
    main()
