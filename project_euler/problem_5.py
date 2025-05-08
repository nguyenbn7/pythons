from functools import reduce

# https://projecteuler.net/problem=5


def gcd(a: int, b: int):
    while b:
        a, b = b, a % b
    return a


def lcm(a: int, b: int):
    return a * b // gcd(a, b)


def lcmm(*args):
    return reduce(lcm, args)


def problem_5_answer(n: int):
    return lcmm(*[*range(1, n + 1)])


if __name__ == "__main__":
    print(problem_5_answer(10))
    print(problem_5_answer(20))
