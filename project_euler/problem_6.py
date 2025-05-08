# https://projecteuler.net/problem=6


def problem_6_answer(n: int):
    square_of_sum = (n * (n + 1) / 2) ** 2
    sum_of_squares = n * (n + 1) * (2 * n + 1) / 6

    return square_of_sum - sum_of_squares


if __name__ == "__main__":
    print(problem_6_answer(10))
    print(problem_6_answer(100))
