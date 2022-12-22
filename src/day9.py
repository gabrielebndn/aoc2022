import copy
import numpy as np
from enum import Enum
from dataclasses import dataclass

FILENAME = "../resources/input_9.txt"

class Direction(Enum):
    LEFT = 0
    RIGHT = 1
    UP = 2
    DOWN = 3

    @staticmethod
    def parse(s: str) -> 'Direction':
        map = {
            'L': Direction.LEFT,
            'R': Direction.RIGHT,
            'U': Direction.UP,
            'D': Direction.DOWN
        }
        return map[s]

@dataclass
class Move:
    d: Direction
    n: int

    @staticmethod
    def parse(s: str) -> 'Move':
        ss = s.split()
        assert len(ss) == 2
        return Move(Direction.parse(ss[0]), int(ss[1]))

class Config:
    def __init__(self):
        self.head = np.array([0, 0])
        self.tail = np.array([0, 0])

    def isValid(self):
        return max(np.abs(self.head - self.tail)) <= 1
    
    def isLooselyValid(self):
        return max(np.abs(self.head - self.tail)) <= 2
    
    def moveHead(self, d: Direction):
        if d == Direction.LEFT:
            self.head[1] -= 1
        elif d == Direction.RIGHT:
            self.head[1] += 1
        elif d == Direction.DOWN:
            self.head[0] -= 1
        elif d == Direction.UP:
            self.head[0] += 1
        else:
            raise RuntimeError("Invalid dir")

    def evolve(self):
        if self.isValid():
            return
        assert self.isLooselyValid()
        diff = self.head - self.tail
        for k in (0, 1):
            k2 = 1 - k
            if diff[k] > 1 or diff[k] == 1 and diff[k2] != 0:
                self.tail[k] += 1
            elif diff[k] < -1 or diff[k] == -1 and diff[k2] != 0:
                self.tail[k] -= 1
        assert self.isValid()

    def applyDirection(self, d: Direction) -> 'Config':
        assert self.isValid()
        res = copy.deepcopy(self)
        res.moveHead(d)
        res.evolve()
        return res

class Rope:
    def __init__(self, N: int):
        assert N > 0
        self.seq = [Config() for _ in range(N)]

    def evolve(self):
        head = self.head
        for c in self.seq:
            c.head = head
            c.evolve()
            head = c.tail
    
    def moveHead(self, d: Direction):
        self.seq[0].moveHead(d)

    def applyDirection(self, d: Direction) -> 'Rope':
        res = copy.deepcopy(self)
        res.moveHead(d)
        res.evolve()
        return res

    @property
    def head(self):
        return self.seq[0].head

    @property
    def tail(self):
        return self.seq[-1].tail

def launch_simu(filename, c):
    seq = [c]
    with open(filename) as f:
        while line := f.readline():
            line = line.strip()
            move = Move.parse(line)
            for _ in range(move.n):
                c = c.applyDirection(move.d)
                seq.append(c)
    return len(set([tuple(c.tail) for c in seq]))

def exo_1():
    return launch_simu(FILENAME, Config())

def exo_2():
    return launch_simu(FILENAME, Rope(9))


if __name__ == "__main__":
    print(exo_1())
    print(exo_2())
