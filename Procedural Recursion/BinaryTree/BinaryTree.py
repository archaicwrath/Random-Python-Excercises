class BinaryTree:
    def __init__(self, rootObj, left=None, right=None):
        self.key = rootObj
        self.left = left
        self.right = right

    def __str__(self):
        try:
            if self.getLeftChild().getRootVal() is not None:
                left = self.left.key
            else:
                left = 'None'
            if self.getRightChild().getRootVal() is not None:
                right = self.right.key
            else:
                right = 'None'
            return 'Node: ' + str(self.key) + '\t' + 'Left: ' + left + '\t' + 'Right: ' + right
        except AttributeError:
            pass


    def insertLeft(self, newNode):
        if self.left is None:
            self.left = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.left = self.left
            self.left = t

    def insertRight(self, newNode):
        if self.right is None:
            self.right = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.right = self.right
            self.right = t

    def getRightChild(self):
        return self.right

    def getLeftChild(self):
        return self.left

    def setRootVal(self, obj):
        self.key = obj

    def getRootVal(self):
        return self.key