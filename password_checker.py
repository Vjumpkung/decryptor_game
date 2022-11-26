# A to Z character for shifting
AtoZ = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# game1 = 7 , game2 = 10 , game3 = 13


def shifter(txtt):
    # caesar shift
    return ''.join(list(map(lambda x: AtoZ[(AtoZ.index(x) - 13) % len(AtoZ)], list(txtt))))


def bit_counter(string):
    # counting 1 in binary
    t = bin(ord(string))[2:]
    return str(t.count("1"))


def to_answer(txt):
    # converting caesar shift to answer
    return ''.join(list(map(bit_counter, list(txt))))


def hash_function(x):
    # for hiding real password
    return hex(abs(hash(x)))


def check_password(solution, answer):
    # check password from password box
    answer_hashed = hash_function(answer)
    solution_hashed = hash_function(to_answer(shifter(solution)))
    return answer_hashed == solution_hashed
