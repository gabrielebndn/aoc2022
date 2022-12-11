

FILENAME = "../resources/input_4.txt"

def contains(p1, p2):
    return p1[0] <= p2[0] and p1[1] >= p2[1]

def overlap(p1, p2):
    # return bool(set(range(p1[0], p1[1]+1)).intersection(set(range(p2[0], p2[1]+1))))
    return p1[0] <= p2[0] and p2[0] <= p1[1] or p1[0] <= p2[1] and p2[1] <= p1[1] or contains(p2, p1)

def exo_1():
    val = 0
    with open(FILENAME) as f:
        while line := f.readline():
            line = line.strip()
            pair_strings = line.split(',')
            assert len(pair_strings) == 2
            p = [[int(num) for num in pair_strings[i].split('-')] for i in range(2)]
            if contains(p[0], p[1]) or contains(p[1], p[0]):
                val += 1

    return val

def exo_2():
    val = 0
    with open(FILENAME) as f:
        while line := f.readline():
            line = line.strip()
            pair_strings = line.split(',')
            assert len(pair_strings) == 2
            p = [[int(num) for num in pair_strings[i].split('-')] for i in range(2)]
            if overlap(p[0], p[1]):
                val += 1

    return val

if __name__ == "__main__":
    print(exo_1())
    print(exo_2())