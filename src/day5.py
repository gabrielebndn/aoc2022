import typing as tp
from dataclasses import dataclass
import re

FILENAME = "../resources/input_5.txt"

@dataclass
class Move:
    quantity: int
    src: int
    dst: int

    @staticmethod
    def parse(s: str):
        m = re.match("move (\d*) from (\d*) to (\d*)", s)
        return Move(int(m.group(1)), int(m.group(2)), int(m.group(3)))      

class Stacks:
    stacks: tp.List

    def apply(self, move):
        for _ in range(move.quantity, 0, -1):
            self.stacks[move.dst-1].append(self.stacks[move.src-1].pop())
    
    def apply_2(self, move):
        self.stacks[move.dst-1].extend(self.stacks[move.src-1][-move.quantity:])
        self.stacks[move.src-1] = self.stacks[move.src-1][:-move.quantity]

    @staticmethod
    def parse(stack_lines: tp.List[str]):
        stack_lines = list(reversed(stack_lines))
        line0 = [int(s) for s in stack_lines[0].split()]
        res = Stacks()
        res.stacks = [[] for _ in range(len(line0))]
        for line in stack_lines[1:]:
            idx = 0
            for k in range(len(res.stacks)):
                if line[idx] == '[':
                    idx += 1
                    res.stacks[k].append(line[idx])
                    idx += 3
                else:
                    idx += 4
        return res

    def get_symbol(self):
        return ''.join([stack[-1] for stack in self.stacks])
    
    def __str__(self) -> str:
        s = ''
        for k, stack in enumerate(self.stacks):
            s += f"{k+1}. {stack}\n"
        return s

def parse_file():
    stack_lines = []
    moves = []
    parse_moves = False
    with open(FILENAME) as f:
        while line := f.readline():
            line = line.strip()
            if parse_moves:
                moves.append(Move.parse(line))
            elif not line:
                stacks = Stacks.parse(stack_lines)
                parse_moves = True
            else:
                stack_lines.append(line)
    return stacks, moves

def exo_1():
    stacks, moves = parse_file()
    for move in moves:
        stacks.apply(move)
    return stacks.get_symbol()

def exo_2():
    stacks, moves = parse_file()
    for move in moves:
        stacks.apply_2(move)
    return stacks.get_symbol()
    

if __name__ == "__main__":
    print(exo_1())
    print(exo_2())
