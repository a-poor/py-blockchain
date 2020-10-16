
import math
import random
import secrets


def is_prime(n: int):
    if n < 2: return False
    if n == 2: return True
    if n & 1 == 0: return False
    stop = int(n ** 0.5) + 1
    for i in range(3,stop,2):
        if n % i == 0: return False
    return True



