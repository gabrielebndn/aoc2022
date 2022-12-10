

FILENAME = "../resources/input_3.txt"

def get_prio(letter):
    if letter.islower():
        return ord(letter) - ord('a') + 1
    else:
        return ord(letter) - ord('A') + 27

def exo_1():
    val = 0
    with open(FILENAME) as f:
        while line := f.readline():
            line = line.strip()
            len_ = len(line) // 2
            intersec = list(set(line[:len_]).intersection(set(line[len_:])))
            assert len(intersec) == 1
            val += get_prio(intersec[0])
    return val

def exo_2():
    val = 0
    ct = 0
    with open(FILENAME) as f:
        while line := f.readline():
            line = line.strip()
            if ct == 0:
                intersec = set(line)
            else:
                intersec = intersec.intersection(set(line))
            if ct == 2:
                assert len(intersec) == 1
                val += get_prio(list(intersec)[0])
            ct = (ct + 1) % 3
    assert ct == 0
    return val

if __name__ == "__main__":
    print(exo_1())
    print(exo_2())