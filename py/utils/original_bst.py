class Node:

    def __init__(self, key):
        self.key = key
        self.right = None
        self.left = None


# →が大きい、←が小さい
class BST:
    def __init__(self):
        self.root = Node(None)

    def insert(self, k):
        # 追加するNodeは葉へ
        z = Node(k)
        z.left, z.right = Node(None), Node(None)
        x = self.root
        y = x
        while(x.key is not None):
            y = x
            if z.key < x.key:
                # print("l")
                x = x.left
            else:
                # print("r")
                x = x.right
        # print("parent key "+str(y.key))
        z.parent = y
        if y.key is None:
            self.root = z
        else:
            if z.key < y.key:
                y.left = z
            else:
                y.right = z

    def find(self, k):
        x = self.root
        while(x.key != k and x.key is not None):
            if x.key < k:
                x = x.left
            else:
                x = x.right
        if x.key == k:
            return True
        else:
            return False

    def printInorder(self, r):
        if r.key is None:
            return
        self.printInorder(r.left)
        print(r.key)
        self.printInorder(r.right)


B = BST()

B.insert(2)
B.insert(1)
B.insert(1)
B.insert(5)
B.insert(1)
B.insert(1)
B.printInorder(B.root)

print(B.find(2))
