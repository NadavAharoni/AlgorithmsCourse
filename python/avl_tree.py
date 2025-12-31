from typing import Optional 

class AVLNode:
    def __init__(self, value):
        self.value = value
        self.left : Optional[Node] = None
        self.right : Optional[Node] = None
        self.parent : Optional[Node] = None
        self.balance_factor = 0
        



