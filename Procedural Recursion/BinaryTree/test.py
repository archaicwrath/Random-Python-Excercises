from BinaryTree import *

values = []
length = 0


def main():
    setTreeAttributes()
    tree = generateTree(length)
    traverse(tree)


def setTreeAttributes():
    length = int(input('Enter the size of your tree: '))
    for i in range(length):
        values.append(input('Enter value ' + str(i) + ': '))


def generateTree(size):
    if size < len(values):
        return BinaryTree(values[size], left=generateTree((size+1)*2-1), right=generateTree((size+1)*2))


def traverse(tree):
    try:
        if tree:
            print(tree)
            traverse(tree.getLeftChild())
            traverse(tree.getRightChild())
    except TypeError:
        pass

if __name__ == '__main__':
    main()