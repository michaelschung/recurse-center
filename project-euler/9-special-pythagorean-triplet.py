# https://projecteuler.net/problem=9

from math import prod

def is_pythag_triplet(a, b, c):
    return pow(a, 2) + pow(b, 2) == pow(c, 2)

def pythag_triplets(n):
    for a in range(1, n+1):
        for b in range(a+1, n+1):
            for c in range(b+1, n+1):
                if is_pythag_triplet(a, b, c):
                    yield (a, b, c)

def find_triplet_with_sum(n):
    triplet_gen = pythag_triplets(n)
    triplet = next(triplet_gen)
    while sum(triplet) != n:
        triplet = next(triplet_gen)
    return triplet

def special_triplet(n):
    return prod(find_triplet_with_sum(n))

print(special_triplet(1000))