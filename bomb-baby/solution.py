""" Tim Hung timhung1010@gmail.com
    
    After drawing out a few examples, I realized this problem is just searching
    for the level of a node in the Calkin-Wilf tree!

    I encountered this structure first when I competed at ICPC Greater NY
    regionals in 2014. It was seen on problem F: A Rational Sequence
    http://acmgnyr.org/year2014/problems.shtml
"""

from fractions import gcd

def answer(m, f):
    m = int(m)
    f = int(f)

    small = min(m, f)
    large = max(m, f)
    if gcd(small, large) != 1:
        return 'impossible'

    generation = 0
    while small + large > 2:
        div = large / small
        mod = large % small
        if mod == 0:
            return str(generation + div - 1)

        large = small
        small = mod
        generation += div

    return str(generation)

def test():
    test_cases = {
        ('2', '1'): '1',
        ('2', '4'): 'impossible',
        ('2', '2'): 'impossible',
        ('4', '7'): '4',
        ('1', '99999999999999999999999999999999999999999999999'): '99999999999999999999999999999999999999999999998',
    }
    for case in test_cases:
        computed = answer(case[0], case[1])
        if computed != test_cases[case]:
            print '\nFailed case!', case
            print 'Computed answer: ', computed
            print 'Expected answer: ', test_cases[case]
            return
    print 'All cases passed!'
test()
