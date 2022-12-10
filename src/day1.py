

FILENAME = "../resources/input_1.txt"

def exo_1():
    val = 0
    max_ = 0
    with open(FILENAME) as f:
        while line := f.readline():
            line = line.strip()
            if line:
                val += int(line)
            else:
                if val > max_:
                    max_ = val
                val = 0

    return max_

def exo_2():
    lst = [0]
    with open(FILENAME) as f:
        while line := f.readline():
            line = line.strip()
            if line:
                lst[-1] += int(line)
            else:
                lst.append(0)

    lst.sort(reverse=True)
    return sum(lst[:3])

if __name__ == "__main__":
    print(exo_1())
    print(exo_2())