# https://projecteuler.net/problem=3


def problem_3_answer(n: int):
    largest_prime = -1

    while n % 2 == 0:
        largest_prime = 2
        n //= 2

    i = 3
    while i * i <= n:
        while n % i == 0:
            largest_prime = i
            n //= i
        i += 2

    if n > 2:
        largest_prime = n

    return largest_prime


if __name__ == "__main__":
    print(problem_3_answer(13_195))
    print(problem_3_answer(600_851_475_143))
