class Node:
    def __init__(self, key: int):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None

    def print(self):
        if self.left:
            # print("left:", end="", sep="")
            self.left.print()
        print(self.key, ", ", sep="", end="")
        if self.right:
            # print("right:", end="",sep="")
            self.right.print()

    def depth(self) -> int:
        depth = 0
        if self.left:
            depth = max(depth, self.left.depth())
        if self.right:
            depth = max(depth, self.right.depth())
        return depth + 1

    def min(self):
        if self.left:
            return self.left.min()
        return self

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, key:int):
        x = self.root
        y = None
        while x is not None:
            y = x
            if key >= x.key:
                x = x.right
            else:
                x = x.left
        new_node = Node(key)
        if y is None:
            # the tree was empty
            self.root = new_node
            return
        if key > y.key:
            y.right = new_node
        else:
            y.left = new_node
        new_node.parent = y

    def print(self):
        if self.root:
            self.root.print()
        print()

    def depth(self):
        if self.root:
            return self.root.depth()
        return 0

    def min(self):
        if self.root:
            return self.root.min().key
        return None

def main():
    tree = Tree()
    tree.print()
    numbers = [100,50,20,70,200]
    for number in numbers:
        tree.insert(number)
        print(F"After inserting {number}:")
        print(F"Tree depth={tree.depth()}")
        print(F"And tree contents: ", end="")
        tree.print()
        print(F"minimum = {tree.min()}")
        print()
    
if __name__=='__main__':
    main()

