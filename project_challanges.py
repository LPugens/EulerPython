import math
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


def challenge_13():
    values = '''37107287533902102798797998220837590246510135740250
46376937677490009712648124896970078050417018260538
74324986199524741059474233309513058123726617309629
91942213363574161572522430563301811072406154908250
23067588207539346171171980310421047513778063246676
89261670696623633820136378418383684178734361726757
28112879812849979408065481931592621691275889832738
44274228917432520321923589422876796487670272189318
47451445736001306439091167216856844588711603153276
70386486105843025439939619828917593665686757934951
62176457141856560629502157223196586755079324193331
64906352462741904929101432445813822663347944758178
92575867718337217661963751590579239728245598838407
58203565325359399008402633568948830189458628227828
80181199384826282014278194139940567587151170094390
35398664372827112653829987240784473053190104293586
86515506006295864861532075273371959191420517255829
71693888707715466499115593487603532921714970056938
54370070576826684624621495650076471787294438377604
53282654108756828443191190634694037855217779295145
36123272525000296071075082563815656710885258350721
45876576172410976447339110607218265236877223636045
17423706905851860660448207621209813287860733969412
81142660418086830619328460811191061556940512689692
51934325451728388641918047049293215058642563049483
62467221648435076201727918039944693004732956340691
15732444386908125794514089057706229429197107928209
55037687525678773091862540744969844508330393682126
18336384825330154686196124348767681297534375946515
80386287592878490201521685554828717201219257766954
78182833757993103614740356856449095527097864797581
16726320100436897842553539920931837441497806860984
48403098129077791799088218795327364475675590848030
87086987551392711854517078544161852424320693150332
59959406895756536782107074926966537676326235447210
69793950679652694742597709739166693763042633987085
41052684708299085211399427365734116182760315001271
65378607361501080857009149939512557028198746004375
35829035317434717326932123578154982629742552737307
94953759765105305946966067683156574377167401875275
88902802571733229619176668713819931811048770190271
25267680276078003013678680992525463401061632866526
36270218540497705585629946580636237993140746255962
24074486908231174977792365466257246923322810917141
91430288197103288597806669760892938638285025333403
34413065578016127815921815005561868836468420090470
23053081172816430487623791969842487255036638784583
11487696932154902810424020138335124462181441773470
63783299490636259666498587618221225225512486764533
67720186971698544312419572409913959008952310058822
95548255300263520781532296796249481641953868218774
76085327132285723110424803456124867697064507995236
37774242535411291684276865538926205024910326572967
23701913275725675285653248258265463092207058596522
29798860272258331913126375147341994889534765745501
18495701454879288984856827726077713721403798879715
38298203783031473527721580348144513491373226651381
34829543829199918180278916522431027392251122869539
40957953066405232632538044100059654939159879593635
29746152185502371307642255121183693803580388584903
41698116222072977186158236678424689157993532961922
62467957194401269043877107275048102390895523597457
23189706772547915061505504953922979530901129967519
86188088225875314529584099251203829009407770775672
11306739708304724483816533873502340845647058077308
82959174767140363198008187129011875491310547126581
97623331044818386269515456334926366572897563400500
42846280183517070527831839425882145521227251250327
55121603546981200581762165212827652751691296897789
32238195734329339946437501907836945765883352399886
75506164965184775180738168837861091527357929701337
62177842752192623401942399639168044983993173312731
32924185707147349566916674687634660915035914677504
99518671430235219628894890102423325116913619626622
73267460800591547471830798392868535206946944540724
76841822524674417161514036427982273348055556214818
97142617910342598647204516893989422179826088076852
87783646182799346313767754307809363333018982642090
10848802521674670883215120185883543223812876952786
71329612474782464538636993009049310363619763878039
62184073572399794223406235393808339651327408011116
66627891981488087797941876876144230030984490851411
60661826293682836764744779239180335110989069790714
85786944089552990653640447425576083659976645795096
66024396409905389607120198219976047599490197230297
64913982680032973156037120041377903785566085089252
16730939319872750275468906903707539413042652315011
94809377245048795150954100921645863754710598436791
78639167021187492431995700641917969777599028300699
15368713711936614952811305876380278410754449733078
40789923115535562561142322423255033685442488917353
44889911501440648020369068063960672322193204149535
41503128880339536053299340368006977710650566631954
81234880673210146739058568557934581403627822703280
82616570773948327592232845941706525094512325230608
22918802058777319719839450180888072429661980811197
77158542502016545090413245809786882778948721859617
72107838435069186155435662884062257473692284509516
20849603980134001723930671666823555245252804609722
53503534226472524250874054075591789781264330331690'''

    values = [int(val) for val in values.split('\n')]

    return str(sum(values))[:10]


def next_collatz(val):
    if val % 2 == 0:
        return val/2
    else:
        return 3*val + 1


def challenge_14():
    visited_values = set()
    values_history = {}
    for i in range(1, 1000000):
        chain_length = 1
        val = i
        while val != 1:
            val = next_collatz(val)
            if val in visited_values:
                chain_length += values_history[val]
                break
            chain_length += 1
        visited_values.add(i)
        values_history[i] = chain_length

    max_chain = -1
    max_starting = None
    for i in values_history.keys():
        if values_history[i] > max_chain:
            max_chain = values_history[i]
            max_starting = i

    return max_starting


def challenge_15():
    grid_size = 20

    path_length = grid_size * 2

    k = path_length / 2
    n = path_length

    fac = math.factorial

    return int(fac(n) / (fac(k) * fac(n-k)))


def challenge_16():
    number = 2**1000

    number = str(number)

    acc = 0
    for ch in number:
        acc += int(ch)

    return acc


def spell_number(number):
    special = {
        '10': 'ten',
        '11': 'eleven',
        '12': 'twelve',
        '13': 'thirteen',
        '14': 'fourteen',
        '15': 'fifteen',
        '16': 'sixteen',
        '17': 'seventeen',
        '18': 'eighteen',
        '19': 'nineteen'
    }

    str_number = ''.join(list(reversed(str(number))))

    result = ''

    digits = {
        '0': '',
        '1': 'one',
        '2': 'two',
        '3': 'three',
        '4': 'four',
        '5': 'five',
        '6': 'six',
        '7': 'seven',
        '8': 'eight',
        '9': 'nine'
    }

    tens = {
        '0': '',
        '1': 'teen',
        '2': 'twenty',
        '3': 'thirty',
        '4': 'forty',
        '5': 'fifty',
        '6': 'sixty',
        '7': 'seventy',
        '8': 'eighty',
        '9': 'ninety'
    }

    first_decimal = str(number)[-2:]
    if first_decimal in special:
        result = special[first_decimal]
        special = True
    else:
        special = False

    for pos, ch in enumerate(str_number):
        if pos == 0 and not special:
            result += digits[ch]
        elif pos == 1 and not special:
            if ch == '1':
                result += tens['1']
            else:
                result = tens[ch] + result
        elif pos == 2:
            if number % 100 != 0:
                result = 'and' + result
            if ch != '0':
                result = digits[ch] + 'hundred' + result
        elif pos == 3:
            if ch != '0':
                result = digits[ch] + 'thousand' + result

    return result


def challenge_17():
    length = 0
    for i in range(1, 10001):
        spelled = spell_number(i)
        length += len(spelled)

    return length


def challenge_18():
    triangle = '''75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'''

    totals = []
    for i_row, row in enumerate(triangle.split('\n')):
        row = row.split(' ')
        int_row = [int(cell) for cell in row]

        if i_row == 0:
            totals.append(int_row)
            continue

        row_above = totals[-1]
        totals += [[]]
        for k_row, cell in enumerate(int_row):
            if k_row != 0:
                path_above_left = row_above[k_row-1]
            else:
                path_above_left = -1
            if k_row < len(row_above):
                path_above_right = row_above[k_row]
            else:
                path_above_right = -1

            max_path = max(path_above_left, path_above_right)
            totals[-1].append(max_path + cell)

    return max(totals[-1])


def days_in_month(month, year):
    if month == 1 and year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return 29

    months = {
        0: 31,
        1: 28,
        2: 31,
        3: 30,
        4: 31,
        5: 30,
        6: 31,
        7: 31,
        8: 30,
        9: 31,
        10: 30,
        11: 31
    }
    return months[month]


def challenge_19():
    count = 0
    current_day = 1
    for year in range(1900, 2001):
        if year == 1901:
            count = 0
        for month in range(12):
            for day_of_month in range(days_in_month(month, year)):
                if day_of_month == 0 and current_day == 0:
                    count += 1
                current_day = (current_day + 1) % 7

    return count


if __name__ == '__main__':
    print(f'result: {challenge_19()}')
