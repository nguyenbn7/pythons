# https://projecteuler.net/problem=1


def calculate_total_from_1_to_n(n: int):
    return n * (n + 1) / 2


def problem_1_answer(n: int):
    total_numbers_divided_by_3 = int((n - 1) / 3)
    sum_numbers_divided_by_3 = 3 * calculate_total_from_1_to_n(
        total_numbers_divided_by_3
    )

    total_numbers_divided_by_5 = int((n - 1) / 5)
    sum_numbers_divided_by_5 = 5 * sum(
        num for num in range(total_numbers_divided_by_5 + 1) if num % 3
    )

    return sum_numbers_divided_by_3 + sum_numbers_divided_by_5


if __name__ == "__main__":
    nums = [10, 100, 1000]

    for num in nums:
        print(
            f"sum of all the natural numbers below {num} that are multiples of 3 or 5: {problem_1_answer(num)}"
        )
