from cmath import sqrt
from functools import reduce
from math import floor
from typing import List


def prime_superset(index):
    """Will generate a subset of the I set, while being an superset of the prime numbers"""
    return 1 + (index << 2) - ((index >> 1) << 1)


def prime_decompose(number: int) -> List[int]:

    max_quotient = floor(sqrt(number).real)
    d = 1
    q = number % 2 == 0 and 2 or 3
    while q <= max_quotient and number % q != 0:
        q = prime_superset(d)
        d += 1
    return q <= max_quotient and [q] + prime_decompose(number // q) or [number]


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
    while True:
        if val % i == 0:
            return False

        i += 1
        if i >= val - 1:
            break

    return True


def challenge_3():
    number = 600851475143
    prime_factors = prime_decompose(number)
    max_prime = max(prime_factors)

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
    three_digit_numbers = range(999, 99, -1)

    maximum_palindrome = -1

    for three_digit_number_i in three_digit_numbers:
        for three_digit_number_j in three_digit_numbers:
            multiplied = three_digit_number_i * three_digit_number_j
            if is_palindrome(multiplied):
                if multiplied > maximum_palindrome:
                    maximum_palindrome = multiplied

    return maximum_palindrome


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


def challenge_7():
    primes_found = [2, 3]
    index = 1
    while True:
        value = prime_superset(index)
        is_value_prime = is_prime(value)
        if is_value_prime:
            primes_found += [value]
            if len(primes_found) == 10001:
                return value
        index += 1


def challenge_8():
    thousand_digits = '7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478' \
                      '8518438586156078911294949545950173795833195285320880551112540698747158523863050715693290963295' \
                      '2274430435576689664895044524452316173185640309871112172238311362229893423380308135336276614282' \
                      '8064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792' \
                      '2749219016997208880937766572733300105336788122023542180975125454059475224352584907711670556013' \
                      '6048395864467063244157221553975369781797784617406495514929086256932197846862248283972241375657' \
                      '0560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171' \
                      '4799244429282308634656748139191231628245861786645835912456652947654568284891288314260769004224' \
                      '2190226710556263211111093705442175069416589604080719840385096245544436298123098787992724428490' \
                      '9188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005' \
                      '593572972571636269561882670428252483600823257530420752963450 '

    window_size = 13
    max_mul = -1
    max_window = []
    for i in range(len(thousand_digits)-window_size):
        window_digits = thousand_digits[i: i + window_size]
        result = reduce(lambda x, y: int(x)*int(y), window_digits)
        if result > max_mul:
            max_mul = result
            max_window = window_digits

    return max_mul, max_window


def challenge_9():
    numbers = list(range(1, 1000))
    for a in numbers:
        for b in numbers:
            for c in numbers:
                if a+b+c == 1000:
                    if a**2 + b**2 == c**2:
                        return a*b*c


def challenge_10():
    primes_found = [2, 3]
    index = 1
    while True:
        value = prime_superset(index)
        is_value_prime = len(prime_decompose(value)) == 1
        if is_value_prime:
            if value >= 2000000:
                return reduce(lambda x, y: x+y, primes_found)
            primes_found += [value]
        index += 1


def challenge_11():
    data_in = '''08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48'''

    data = [row for row in data_in.split('\n')]
    data = [row.split(' ') for row in data]
    data = [[int(cell) for cell in row] for row in data]

    directions = [
        (1, 1),
        (1, -1),
        (-1, 1),
        (-1, -1),
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0)
    ]

    max_val = -1
    for direction in directions:
        for i in range(len(data)):
            for j in range(len(data[0])):
                cum = 1
                pos = (i, j)
                for k in range(4):
                    if pos[0] >= len(data) or pos[1] >= len(data[0]) or pos[0] < 0 or pos[1] < 0:
                        break

                    cum *= data[pos[0]][pos[1]]
                    pos = (pos[0]+direction[0], pos[1]+direction[1])

                if cum > max_val:
                    max_val = cum
    return max_val


def count_divisors(n):
    return len(
        set(
            reduce(
                list.__add__,
                ([i, n // i] for i in range(1, int(n ** 0.5) + 1) if n % i == 0)
            )
        )
    )


def challenge_12():
    count = 1
    while True:
        value = sum(range(1, count+1))
        divisions = count_divisors(value)
        if divisions > 500:
            return value

        count += 1


if __name__ == '__main__':
    print(f'result: {challenge_12()}')
    # count_divisors(10)
