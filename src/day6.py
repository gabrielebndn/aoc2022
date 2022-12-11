FILENAME = "../resources/input_6.txt"

def solve(num):
    with open(FILENAME) as f:
        line = f.readline().strip()
        for k in range(num, len(line)):
            if len(set(line[k-num:k])) == num:
                return k
    return -1

def exo_1():
    return solve(4)

def exo_2():
    return solve(14)

if __name__ == "__main__":
    print(exo_1())
    print(exo_2())
