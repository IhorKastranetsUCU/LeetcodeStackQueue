import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from MyCollections import myQueue


class MyStack:

    def __init__(self):
        self.items = myQueue()

    def push(self, x: int) -> None:
        self.items.enqueue(x)
        for _ in range(len(self.items.items) - 1):
            self.items.enqueue(self.items.dequeue())

    def pop(self) -> int:
        return self.items.dequeue()

    def top(self) -> int:
        return self.items.peek()

    def empty(self) -> bool:
        return self.items.is_empty()
