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
    index = 0
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
