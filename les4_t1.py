import math
import timeit

# без использования алгоритма «Решето Эратосфена»
def sieve_without_eratosthenes(i):

    lst_prime = [2]
    number = 3
    while len(lst_prime) < i:
        flag = True
        for j in lst_prime.copy():
            if number % j == 0:
                flag = False
                break
        if flag:
            lst_prime.append(number)
        number += 1
    return lst_prime[-1]


# при использовании алгоритма «Решето Эратосфена»
def sieve_eratosthenes(i):


    i_max = prime_counting_function(i)
    lst_prime = [_ for _ in range(2, i_max)]

    for number in lst_prime:
        if lst_prime.index(number) <= number - 1:
            for j in range(2, len(lst_prime)):
                if number * j in lst_prime[number:]:
                    lst_prime.remove(number * j)
        else:
            break
    return lst_prime[i - 1]


def prime_counting_function(i):

    number_of_primes = 0
    number = 2
    while number_of_primes <= i:
        number_of_primes = number / math.log(number)
        number += 1
    return number


time11 = timeit.timeit(f'sieve_without_eratosthenes({10})', setup='from __main__ import sieve_without_eratosthenes', number=1)
time12 = timeit.timeit(f'sieve_without_eratosthenes({100})', setup='from __main__ import sieve_without_eratosthenes', number=1)
time13 = timeit.timeit(f'sieve_without_eratosthenes({1000})', setup='from __main__ import sieve_without_eratosthenes', number=1)

time21 = timeit.timeit(f'sieve_eratosthenes({10})', setup='from __main__ import sieve_eratosthenes', number=1)
time22 = timeit.timeit(f'sieve_eratosthenes({100})', setup='from __main__ import sieve_eratosthenes', number=1)
time23 = timeit.timeit(f'sieve_eratosthenes({1000})', setup='from __main__ import sieve_eratosthenes', number=1)

print(time11)  # 3.6697999999998204e-05
print(time12)  # 0.001190649999999998
print(time13)  # 0.08488583999999999
print(time21)  # 0.00014645300000000472
print(time22)  # 0.02613790499999999
print(time23)  # 7.012399212

print(f'Без использования алгоритма «Решето Эратосфена» быстрее \
чем с использованием алгоритма «Решето Эратосфена» в \
{round(time22 / time12, 2)} раз')
