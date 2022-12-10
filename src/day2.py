

FILENAME = "../resources/input_2.txt"

def decrypt_first(letter):
    return ord(letter) - ord('A')

def decrypt_second(letter):
    return ord(letter) - ord('X')

def value_win(v1, v2):
    res = (1 + v2 - v1) % 3
    return res * 3

def value_shape(v):
    return v+1

def value_game(v1, v2):
    return value_shape(v2) + value_win(v1, v2)

def get_strategy(v1, s2):
    strat = decrypt_second(s2) - 1
    return (v1 + strat) % 3


def exo_1():
    val = 0
    with open(FILENAME) as f:
        while line := f.readline():
            strings = line.strip().split()
            values = [decrypt_first(strings[0]), decrypt_second(strings[1])]
            val += value_game(values[0], values[1])
    return val

def exo_2():
    val = 0
    with open(FILENAME) as f:
        while line := f.readline():
            strings = line.strip().split()
            v1 = decrypt_first(strings[0])
            v2 = get_strategy(v1, strings[1])
            val += value_game(v1, v2)
    return val

if __name__ == "__main__":
    print(exo_1())
    print(exo_2())