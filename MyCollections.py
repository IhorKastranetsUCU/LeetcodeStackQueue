from collections import deque


class myStack:
    def __init__(self):
        self.stack = deque()

    def is_empty(self):
        """
        Is empty

        >>> s1 = myStack()
        >>> s1.is_empty()
        True
        >>> s1.push(1)
        >>> s1.is_empty()
        False
        """
        return self.size() == 0

    def push(self, item):
        """
        Appending new element

        >>> s2 = myStack()
        >>> s2.push(69)
        >>> s2.peek()
        69
        """
        self.stack.append(item)

    def pop(self):
        """
        Deleting the last element

        >>> s3 = myStack()
        >>> s3.push(6)
        >>> s3.push(9)
        >>> s3.push(42)
        >>> print(s3)
        Stack([6, 9, 42])
        >>> s3.pop()
        42
        >>> print(s3)
        Stack([6, 9])

        """
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.stack.pop()

    def peek(self):
        """
        Shows the last element in the stack

        >>> s4 = myStack()
        >>> s4.push(1)
        >>> s4.push(4)
        >>> s4.peek()
        4
        """
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.stack[-1]

    def size(self):
        """
        Shows count of elements in the stack

        >>> s4 = myStack()
        >>> s4.push(1)
        >>> s4.push(4)
        >>> s4.size()
        2
        """
        return len(self.stack)

    def __repr__(self):
        return f"Stack({str(self.stack)[6:-1]})"



class myQueue:
    def __init__(self):
        self.items = deque()

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items.popleft()

    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items[0]

    def __repr__(self):
        return f"Queue({str(self.items)[6:-1]})"