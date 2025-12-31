from typing import Optional 

class AVLNode:
    def __init__(self, value):
        self.value = value
        self.left : Optional[AVLNode] = None
        self.right : Optional[AVLNode] = None
        self.parent : Optional[AVLNode] = None
        self.balance_factor = 0
        

class AVLTree:
    def __init__(self, key= lambda x: x):
        self.key = key
        self.root : Optional[AVLNode] = None



def main():
    pass

if __name__=='__main__':
    main()

