
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
        if i >= val-1:
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
        if i >= NUMBER-1:
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

    return None