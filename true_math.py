#true_divide
from math import inf


def divide(first, second):
    if second == 0:
        return inf
    return first / second

if __name__== "__main__":
    result3 = divide(49, 7)
    print(result3)
    result4 = divide(15, 0)
    print(result4)

