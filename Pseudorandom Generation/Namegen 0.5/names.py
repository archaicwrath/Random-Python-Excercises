import random
from swaplist import *

with open('data/surnames.txt', 'r') as sur:
    surnames = [line.strip() for line in sur]

with open('data/female.txt', 'r') as fem:
    female = [line.strip() for line in fem]

with open('data/male.txt', 'r') as mal:
    male = [line.strip() for line in mal]

with open('data/syllables.txt', 'r') as syl:
    syllables = [line.strip() for line in syl]


def genName(name):
    name = str.lower(name)
    newname = []

    for i, c in enumerate(name):
        toswap = c
        for j, s in enumerate(syllables):
            if c == syllables[j] and random.uniform(0, 1) > .25:
                toswap = swap[c][random.randint(0, len(swap[c]) - 1)]

        newname.append(toswap)

    newname = ''.join(newname)
    newname = newname.title()
    return newname


def main():
    for n in range(30):
        origname = random.choice(surnames)
        print(str.expandtabs(origname + "\t"+ str(genName(origname)), 12))


if __name__ == '__main__':
    main()