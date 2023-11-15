"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""


def primes(number_of_primes):
    if number_of_primes <= 0:
        raise ValueError("Number of primes must be a positive integer")

    list = []
    current_num = 2
    while len(list) < number_of_primes:
        if all(current_num % prime != 0 for prime in list):
            list.append(current_num)
        current_num += 1
    return list