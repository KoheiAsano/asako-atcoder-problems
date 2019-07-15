class Node:
    def __init__(self, value : int, nex = None):
        self.value = value
        self.nex = nex
class Linkedlist:
    def __init__(self):
        self.front = None
        self.size = 0

    def __len__(self):
        return self.size

    def __getitem__(self, i):
        if i >= self.size:
            raise Exception("index out of range")
        top = self.front
        for _ in range(i):
            top = top.nex
        return top.value

    def appendLeft(self, k):
        if self.front is None:
            self.front = Node(k)
        else:
            self.front = Node(k, self.front)
        self.size += 1

    def insert(self, i, k):
        if i >= self.size:
            raise Exception("index out of range")
        elif i == 0:
            self.appendLeft(k)
        top = self.front
        for _ in range(i-1):
            top = top.nex
        if top.nex is None:
            top.nex = Node(k)
        else:
            top.nex = Node(k, top.nex)
        self.size += 1


LL = Linkedlist()
LL.appendLeft(1)
LL.appendLeft(34)
LL.insert(1, 36)
LL.insert(2, 39)
LL[0], LL[1], LL[2], LL[3]
