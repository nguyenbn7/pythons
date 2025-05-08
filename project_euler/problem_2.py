# https://projecteuler.net/problem=2


def problem_2_answer(limit: int, f0=1, f1=2):
    s = 0

    if f1 % 2 == 0:
        s += f1

    while f1 < limit:
        temp = f0 + f1
        f0 = f1
        f1 = temp
        if f1 % 2 == 0:
            s += f1

    return s


if __name__ == "__main__":
    print(problem_2_answer(4_000_000))
