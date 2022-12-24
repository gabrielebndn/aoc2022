import copy
import numpy as np
from enum import Enum
from dataclasses import dataclass
import typing as tp

FILENAME = "../resources/input_10.txt"
TESTFILE = "../resources/test_10.txt"

def parse_instruction(s: str) -> tp.Optional[int]:
    if s == 'noop':
        return None
    ss = s.split()
    assert len(ss) == 2
    assert ss[0] == 'addx'
    return int(ss[1])

def run_instructions(filename):
    seq = [1]
    with open(filename) as f:
        while line := f.readline():
            line = line.strip()
            i = parse_instruction(line)
            latest = seq[-1]
            seq.append(latest)
            if i is not None:
                seq.append(latest + i)
    return seq

def exo_1():
    key_cycles = [20 + 40 * k for k in range(6)]
    seq = run_instructions(FILENAME)
    sum_ = 0
    for k, val in enumerate(seq):
        cycle = k+1
        if cycle in key_cycles:
            sum_ += cycle * val
    return sum_


def exo_2():
    pass


if __name__ == "__main__":
    print(exo_1())
    print(exo_2())
