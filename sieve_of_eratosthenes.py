"""Find primes up to some target number, using the Sieve of Eratosthenes"""

import numpy as np


def find_primes(highest_to_check=100) -> list:

    def next_nonzero_value(ar: np.ndarray, hint: int):
        """Return the lowest non-zero value at or after index position 'hint'.

        :param ar: an ndarray of integers
        :param hint: the index position of the sieve to start searching from
        :return:
        """
        for i in range(hint, len(ar)):
            if ar[i] != 0:
                return i
        return None

    # array 'a' starts with all ints in range, from which we'll eliminate all non-primes:
    a = np.arange(2, highest_to_check + 1)

    current_prime = 2  # start here

    primes = []  # stores the primes we find

    while current_prime < highest_to_check:
        primes.append(current_prime)
        # use vectorized assignment & striding to remove ALL multiples of current_prime:
        a[current_prime * 2::current_prime] = 0

        # get the next prime number:
        current_prime = next_nonzero_value(a, current_prime + 1)
        if current_prime is None:
            break

    return primes


p = find_primes(100)

print(p)

# print('largest prime: ', p[-1])
# print('1000th prime: ', p[999])