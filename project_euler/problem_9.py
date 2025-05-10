# https://projecteuler.net/problem=9

from functools import reduce


def find_pythagorean_triplet(sum_of_triplet: int):
    result = []
    sum_of_triplet_squared = sum_of_triplet**2
    for a in range(1, sum_of_triplet - 1):
        num = 2 * a**2 + sum_of_triplet_squared - 2 * sum_of_triplet * a
        den = 2 * (sum_of_triplet - a)

        if den == 0 or num % den != 0:
            continue

        c = num // den
        b = sum_of_triplet - a - c

        if b > a:
            result.append([a, b, c])

    return result


def problem_9_answer(sum_of_triplet: int):
    triplets = find_pythagorean_triplet(sum_of_triplet)

    return [reduce(lambda p, t: p * t, triplet, 1) for triplet in triplets]


if __name__ == "__main__":
    # print(problem_9_answer(12))
    # print(problem_9_answer(60))
    print(problem_9_answer(1000))
