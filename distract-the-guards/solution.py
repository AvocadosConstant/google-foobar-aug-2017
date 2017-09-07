""" Tim Hung timhung1010@gmail.com """

from fractions import Fraction

def banana_game(b1, b2):
    if b1 == b2:
        return b1, b2
    b1, b2 = min(b1, b2), max(b1, b2)
    b2 -= b1
    b1 *= 2
    return min(b1, b2), max(b1, b2)

def will_loop_forever_iterative(b1, b2):
    visited = set([(b1, b2)])
    cur = banana_game(b1, b2)
    while cur not in visited:
        visited.add(cur)
        cur = banana_game(*cur)
    return cur[0] != cur[1]

def will_loop_forever(b1, b2):
    frac = Fraction(min(b1, b2), max(b1, b2))
    frac_sum = frac.numerator + frac.denominator
    return (frac_sum & (frac_sum - 1)) != 0

def answer(banana_list):
    """
    for i, left in enumerate(banana_list):
        for j, right in enumerate(banana_list[i+1:]):
            print left, right, will_loop_forever(left, right), will_loop_forever_iterative(left, right)
    """

    dim = 8
    for x in range(1, dim):
        for y in range(x, dim):
            print x, y, will_loop_forever(x, y), will_loop_forever_iterative(x, y)
    return 0
