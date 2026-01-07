class Link:
    def __init__(self, value, next_link=None):
        self.value = value
        self.next = next_link


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self._size = 0

    # ---------- Stack operations ----------

    def push(self, value):
        """Push value onto the stack (insert at head)."""
        new_link = Link(value, self.head)
        self.head = new_link
        self._size += 1

    def pop(self):
        """Pop and return the top value from the stack."""
        if self.is_empty():
            raise IndexError("pop from empty stack")

        value = self.head.value
        self.head = self.head.next
        self._size -= 1
        return value

    def peek(self):
        """Return the top value without removing it."""
        if self.is_empty():
            raise IndexError("peek from empty stack")

        return self.head.value

    def is_empty(self):
        """Return True if the stack is empty."""
        return self.head is None

    # ---------- Utility methods ----------

    def size(self):
        return self._size

    def __iter__(self):
        current = self.head
        while current:
            yield current.value
            current = current.next

    def __repr__(self):
        values = " -> ".join(str(v) for v in self)
        return f"SinglyLinkedList({values})"

