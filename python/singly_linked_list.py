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
        new_link = Link(value, self.head)
        self.head = new_link
        self._size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")

        value = self.head.value
        self.head = self.head.next
        self._size -= 1
        return value

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.head.value

    def is_empty(self):
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


# ---------- Tests / main ----------

def main():
    print("Creating empty stack...")
    stack = SinglyLinkedList()

    print("Is empty?", stack.is_empty())
    print("Size:", stack.size())
    print()

    print("Pushing values: 10, 20, 30")
    stack.push(10)
    stack.push(20)
    stack.push(30)

    print("Stack:", stack)
    print("Top element (peek):", stack.peek())
    print("Size:", stack.size())
    print()

    print("Popping elements:")
    print("Popped:", stack.pop())
    print("Stack:", stack)

    print("Popped:", stack.pop())
    print("Stack:", stack)

    print("Popped:", stack.pop())
    print("Stack:", stack)

    print("Is empty?", stack.is_empty())
    print()

    print("Attempting to pop from empty stack:")
    try:
        stack.pop()
    except IndexError as e:
        print("Caught exception:", e)


if __name__ == "__main__":
    main()
