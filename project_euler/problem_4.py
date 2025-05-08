from warnings import warn

# https://projecteuler.net/problem=4


def is_palindrome(n: int):
    num = n
    reversed_num = 0
    while n != 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n //= 10

    return reversed_num == num


def problem_4_answer(n: int):
    if n <= 0:
        raise Exception("Number of digits must greater than 0")
    elif n > 6:
        warn("Number of digits start from 7 is really slow to get an answer")

    largest_num_n_digits = 10**n - 1
    smallest_num_n_digits = largest_num_n_digits // 10 + 1

    max_palindrome_num = -1

    # https://stackoverflow.com/questions/24772179/largest-palindrome-product-euler-project
    for i in range(largest_num_n_digits, smallest_num_n_digits - 1, -1):
        if max_palindrome_num >= i * largest_num_n_digits:
            break

        for j in range(largest_num_n_digits, i - 1, -1):
            p = i * j
            if max_palindrome_num < p and is_palindrome(p):
                max_palindrome_num = p

    return max_palindrome_num


if __name__ == "__main__":
    print(problem_4_answer(2))
    print(problem_4_answer(3))
