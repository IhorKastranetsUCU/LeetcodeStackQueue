import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from MyCollections import myStack


class FreqStack:
    def __init__(self):
        self.group = {}
        self.freq = {}
        self.max_freq = 0

    def push(self, val: int) -> None:
        if val in self.freq:
            self.freq[val] += 1
        else:
            self.freq[val] = 1
        f = self.freq[val]

        if f > self.max_freq:
            self.max_freq = f

        if f not in self.group:
            self.group[f] = myStack()
        self.group[f].push(val)

    def pop(self) -> int:
        val = self.group[self.max_freq].pop()
        self.freq[val] -= 1
        if self.freq[val] == 0:
            del self.freq[val]

        if self.group[self.max_freq].is_empty():
            del self.group[self.max_freq]
            self.max_freq -= 1
        return val
