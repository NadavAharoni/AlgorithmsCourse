from typing import Optional 

class Node:
    def __init__(self, key: str):
        self.key = key
        self.count : int = 0
        self.left : Optional[Node] = None
        self.right : Optional[Node] = None
        self.parent : Optional[Node] = None

    def print(self):
        if self.left:
            # print("left:", end="", sep="")
            self.left.print()
        print(self.key, ", ", sep="", end="")
        if self.right:
            # print("right:", end="",sep="")
            self.right.print()

    """
    side: "left" if self is a left son, "right" if self is a right son
    and "" (empty string) if self is root
    """
    def print_indented(self, indent="", side=""):
        if self.right:
            if side == "left" or side=="":
                next_indent = indent+"   ┃"
            else:
                next_indent = indent[:-1]+"    ┃"
            # print(F"{self.key}, indent={indent}")
            self.right.print_indented(next_indent,side="right")

        current_indent=""
        if side=="left":
            current_indent=indent[:-1]+"┗"
        elif side=="right":
            current_indent=indent[:-1]+"┏"
        else:
            current_indent=""
        print(F"{current_indent}{self.key}:{self.count}")

        if self.left:
            if side == "right" or side=="":
                next_indent = indent+"   ┃"
            else:
                next_indent = indent[:-1]+"    ┃"
            # print(F"{self.key}, indent={indent}")
            self.left.print_indented(next_indent,side="left")

    # previous version
    def print_indented1(self, indent=""):
        if self.right:
            if self.parent and self.parent.right and self.parent.right == self:
                self.right.print_indented1(indent[:-1]+"   ┃")
            else:
                self.right.print_indented1(indent+"    ┃")
        else:
            if self.left:
                print(indent[:-1]+"   ┏⦻")

        side_symbol=""
        if self.parent:
            if self.parent.left == self:
                side_symbol="┗"
            else:
                side_symbol = "┏"
        print(F"{indent[:-1]}{side_symbol}{self.key}:{self.count}")

        if self.left:
            self.left.print_indented1(indent[:-1]+"   ┃")
        else:
            if self.right:
                print(indent[:-1]+"    ┗⦻")



    def depth(self) -> int:
        depth = 0
        if self.left:
            depth = max(depth, self.left.depth())
        if self.right:
            depth = max(depth, self.right.depth())
        return depth + 1

    def min(self) -> 'Node':
        if self.left:
            return self.left.min()
        return self
    
    def max(self) -> 'Node':
        if self.right:
            return self.right.max()
        return self

    def successor(self) -> Optional['Node']:
        if self.right:
            return self.right.min()
        # else
        # find the lowest ancestor of self whose left child is an ancestor of self
        x = self
        y = self.parent
        while y and  x == y.right:
            x = y
            y = y.parent
        return y
        
    def predecessor(self) -> Optional['Node']:
        if self.left:
            return self.left.max()
        # else
        # find the lowest ancestor of self whose right child is an ancestor of self
        x = self
        y = self.parent
        while y and  x == y.left:
            x = y
            y = y.parent
        return y

    def get_number_of_nodes(self) -> int:
        number_of_nodes : int = 1
        if self.left:
            number_of_nodes += self.left.get_number_of_nodes()
        if self.right:
            number_of_nodes += self.right.get_number_of_nodes()
        return number_of_nodes
    
    def get_k_node(self, k : int) -> 'Node':
        left_count = 0
        if self.left:
            left_count = self.left.get_number_of_nodes()

        if left_count == k-1:
            return self
        # else
        if left_count < k-1:
            assert(self.right)
            return self.right.get_k_node(k - left_count - 1)
        else:
            # left_count > k-1:
            assert(self.left)
            return self.left.get_k_node(k)

class Tree:
    def __init__(self):
        self.root = None

    def search_or_insert(self, key:str) -> Node:
        x = self.root
        y : Optional[Node] = None
        while x is not None:
            y = x
            if key == x.key:
                return x
            if key > x.key:
                x = x.right
            else:
                x = x.left
        new_node = Node(key)
        if y is None:
            # the tree was empty
            self.root = new_node
        elif key > y.key:
            y.right = new_node
        else:
            y.left = new_node
        new_node.parent = y
        return new_node

    def insert(self, key:str):
        x = self.root
        y : Optional[Node] = None
        while x is not None:
            if key == x.key:
                # if the key is already in the tree, ignore
                return
            y = x
            if key > x.key:
                x = x.right
            else:
                x = x.left
        
        new_node = Node(key)
        new_node.count = 1
        if y is None:
            # the tree was empty
            self.root = new_node
            return
        assert(key != y.key)
        if key > y.key:
            y.right = new_node
        else:
            y.left = new_node
        new_node.parent = y

    def get_number_of_nodes(self):
        number_of_nodes = 0
        if self.root:
            number_of_nodes += self.root.get_number_of_nodes()
        return number_of_nodes

    def print(self):
        if self.root:
            self.root.print()
        print() # print an empty line

    def print_indented(self):
        if self.root:
            self.root.print_indented()

    def print_indented1(self):
        if self.root:
            self.root.print_indented1()


    def depth(self):
        if self.root:
            return self.root.depth()
        return 0

    def min(self):
        if self.root:
            return self.root.min().key
        return None
    
    def min_node(self):
        if self.root:
            return self.root.min()
        return None
    
    def median(self) -> Optional[Node]:
        if self.root:
            number_of_nodes = self.get_number_of_nodes()
            return self.root.get_k_node(int(number_of_nodes / 2))
        else:
            return None

        
def main():
    tree = Tree()

    names = ["roy","shir","shani","shir","efraim","moshe","baruch","bracha","shai",
             "shir","vered","shani","roy","avi","aaron","reuven","pnina","efraim","roy"]
    for name in names:
        node = tree.search_or_insert(name)
        node.count += 1

    tree.print()
    print("============\n\n")
    tree.print_indented()
    tree.print_indented1()

    name = "aaron"
    node = tree.search_or_insert(name)
    node = node.successor()
    if node:
        print(F"the succesor of {name} is {node.key}")
    else:
        print(F"{name} does not have a succesor")

    node = tree.search_or_insert(name)
    node = node.predecessor()
    if node:
        print(F"the predecessor of {name} is {node.key}")
    else:
        print(F"{name} does not have a predecessor")

    median_node = tree.median()
    if median_node:
        print(F"median={median_node.key}")
    else:
        print(F"tree.median() returned None")


if __name__=='__main__':
    main()

