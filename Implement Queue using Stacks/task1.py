import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from MyCollections import myStack

class MyQueue:

    def __init__(self):
        self.stack_to = myStack()
        self.stack_from = myStack()

    def push(self, x: int) -> None:
        self.stack_to.push(x)

    def pop(self) -> int:
        if self.stack_from.is_empty():
            while not self.stack_to.is_empty():
                self.stack_from.push(self.stack_to.pop())

        return self.stack_from.pop()

    def peek(self) -> int:
        if self.stack_from.is_empty():
            while not self.stack_to.is_empty():
                self.stack_from.push(self.stack_to.pop())

        return self.stack_from.peek()

    def empty(self) -> bool:
        return self.stack_to.is_empty() and self.stack_from.is_empty()