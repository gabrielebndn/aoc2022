import numpy as np

FILENAME = "../resources/input_8.txt"

def parse_file(filename: str) -> np.ndarray:
    lst = []
    with open(filename) as f:
        while line := f.readline():
            line = line.strip()
            lst.append([int(elem) for elem in line])
    return np.array(lst)

def exo_1():
    m = parse_file(FILENAME)
    ct = 0
    rows = m.shape[0]
    cols = m.shape[1]
    for row in range(rows):
        for col in range(cols):
            val = m[row, col]
            left  = m[row, 0:col]
            right = m[row, col+1:]
            up   = m[0:row,  col]
            down = m[row+1:, col]
            viz_left = all(left < val)
            viz_right = all(right < val)
            viz_up = all(up < val)
            viz_down = all(down < val)
            viz = viz_left or viz_right or viz_up or viz_down
            if viz:
                ct += 1
    return ct

def count_distance(val, arr):
    ct = 0
    for h in arr:
        ct += 1
        if h >= val:
            break
    return ct

def exo_2():
    m = parse_file(FILENAME)
    rows = m.shape[0]
    cols = m.shape[1]
    max_score = 0
    for row in range(rows):
        for col in range(cols):
            val = m[row, col]
            left  = m[row, 0:col]
            right = m[row, col+1:]
            up   = m[0:row,  col]
            down = m[row+1:, col]
            d_left = count_distance(val, np.array(list(reversed(left))))
            d_right = count_distance(val, right)
            d_up = count_distance(val, np.array(list(reversed(up))))
            d_down = count_distance(val, down)
            score = d_left * d_right * d_up * d_down
            if score > max_score:
                max_score = score
    return max_score


if __name__ == "__main__":
    print(exo_1())
    print(exo_2())
