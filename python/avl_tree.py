import random
from typing import Optional, Callable

class AVLNode:
    def __init__(self, value):
        self.value = value
        self.left: Optional["AVLNode"] = None
        self.right: Optional["AVLNode"] = None
        self.parent: Optional["AVLNode"] = None
        self.balance_factor = 0

    def print_inorder(self):
        if self.left:
            self.left.print_inorder()
        print(self.value)
        if self.right:
            self.right.print_inorder()
    
    def print(self, level=0):
        if self.right:
            self.right.print(level + 1)
        print(' ' * 4 * level + '->', self.value, f"(BF={self.balance_factor})")
        if self.left:
            self.left.print(level + 1)


class AVLTree:
    def __init__(self, key: Callable = lambda x: x):
        self.key = key
        self.root: Optional[AVLNode] = None

    # -------------------------------------------------------
    # Rotation helpers
    # -------------------------------------------------------
    def rotate_left(self, x: AVLNode) -> AVLNode:
        y = x.right
        x.right = y.left
        if y.left:
            y.left.parent = x
        y.parent = x.parent

        if not x.parent:
            self.root = y
        elif x.parent.left is x:
            x.parent.left = y
        else:
            x.parent.right = y

        y.left = x
        x.parent = y

        # Update balance factors
        x.balance_factor = (self.height(x.left) - self.height(x.right))
        y.balance_factor = (self.height(y.left) - self.height(y.right))
        return y

    def rotate_right(self, x: AVLNode) -> AVLNode:
        y = x.left
        x.left = y.right
        if y.right:
            y.right.parent = x
        y.parent = x.parent

        if not x.parent:
            self.root = y
        elif x.parent.right is x:
            x.parent.right = y
        else:
            x.parent.left = y

        y.right = x
        x.parent = y

        # Update balance factors
        x.balance_factor = (self.height(x.left) - self.height(x.right))
        y.balance_factor = (self.height(y.left) - self.height(y.right))
        return y

    # -------------------------------------------------------
    # Rebalance after insert
    # -------------------------------------------------------
    def rebalance(self, node: AVLNode):
        while node:
            node.balance_factor = self.height(node.left) - self.height(node.right)

            # Left heavy
            if node.balance_factor > 1:
                # Left-Right case
                if node.left and node.left.balance_factor < 0:
                    self.rotate_left(node.left)
                node = self.rotate_right(node)

            # Right heavy
            elif node.balance_factor < -1:
                # Right-Left case
                if node.right and node.right.balance_factor > 0:
                    self.rotate_right(node.right)
                node = self.rotate_left(node)

            # Move up to check parent
            node = node.parent

    # -------------------------------------------------------
    # Insert with key function
    # -------------------------------------------------------
    def insert(self, value):
        """Insert value using key(), like Python's sorted(key=...)"""
        new = AVLNode(value)

        if not self.root:
            self.root = new
            return

        current = self.root
        while True:
            if self.key(value) < self.key(current.value):
                if not current.left:
                    current.left = new
                    new.parent = current
                    break
                current = current.left
            else:
                if not current.right:
                    current.right = new
                    new.parent = current
                    break
                current = current.right

        # After insertion, rebalance
        self.rebalance(new)

    # -------------------------------------------------------
    # Utility for balancing calculations
    # -------------------------------------------------------
    def height(self, node: Optional[AVLNode]) -> int:
        if not node:
            return 0
        return 1 + max(self.height(node.left), self.height(node.right))


    def print_inorder(self):
        if self.root:
            self.root.print_inorder()

def main():
    values = list( range(10,101,10) )
    random.shuffle(values)
    print(values)
    tree = AVLTree(key=lambda x: x)
    for v in values:
        tree.insert(v)

    tree.print_inorder()



if __name__ == "__main__":
    main()
