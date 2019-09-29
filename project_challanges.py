from cmath import sqrt
from functools import reduce
from math import floor
from typing import List


def challenge_1():
    multiples = [i for i in range(1000) if i % 5 == 0 or i % 3 == 0]

    return sum(multiples)


def challenge_2():
    fib = [1, 1]
    while True:
        new_fib = fib[-1] + fib[-2]
        if new_fib > 4000000:
            break
        fib.append(new_fib)

    even_sum = sum([val for val in fib if val % 2 == 0])

    return even_sum


def is_prime(val):
    i = 2
    # for i in range(1, val):
    while True:
        if val % i == 0:
            return False

        i += 1
        if i >= val - 1:
            break

    return True


def challenge_3():
    NUMBER = 60085147
    i = 1
    max_prime = None

    while True:

        if NUMBER % i == 0 and is_prime(i):
            max_prime = i

        i += 1
        if i >= NUMBER - 1:
            break

    return max_prime


def is_palindrome(number: int) -> bool:
    digits = []
    tmp_number = number
    while tmp_number >= 1:
        digits += [int(tmp_number % 10)]
        tmp_number /= 10

    is_it = digits[::] == digits[::-1]

    return is_it


def challenge_4():
    three_digit_numbers = range(1000, 100, -1)

    for three_digit_number_i in three_digit_numbers:
        for three_digit_number_j in three_digit_numbers:
            multiplied = three_digit_number_i * three_digit_number_j
            if is_palindrome(multiplied):
                return multiplied


def prime_decompose(number: int) -> List[int]:
    def step(index):
        """Will generate a subset of the I set, while being an superset of the prime numbers"""
        return 1 + (index << 2) - ((index >> 1) << 1)

    max_quotient = floor(sqrt(number).real)
    d = 1
    q = number % 2 == 0 and 2 or 3
    while q <= max_quotient and number % q != 0:
        q = step(d)
        d += 1
    return q <= max_quotient and [q] + prime_decompose(number // q) or [number]


def challenge_5():
    one_to_twenty = range(1, 21)
    decompositions = [prime_decompose(val) for val in one_to_twenty]

    max_val = max(sum(decompositions, []))
    factors = []
    for i in range(max_val + 1):
        factors += [max([decomposition.count(i) for decomposition in decompositions])]
        i += 1

    result = reduce(lambda x, y: x * y, [i ** fac for i, fac in enumerate(factors)])

    return result


def challenge_6():
    values = range(1, 101)
    sum_of_squares = sum([val**2 for val in values])
    square_of_sums = sum(values)**2

    return square_of_sums - sum_of_squares
