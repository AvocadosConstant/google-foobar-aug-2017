""" Tim Hung timhung1010@gmail.com """

def answer(l):
    """ num_divisors[i] counts the number of
        divisors of l[i] that come before it """
    num_divisors = [0] * len(l)
    triple_count = 0
    for large in range(1, len(l)):
        for small in range (0, large):
            if l[large] % l[small] == 0:
                num_divisors[large] += 1
                triple_count += num_divisors[small]
    return triple_count

def test():
    test_cases = [
        ([1, 1, 1], 1),
        ([1, 2, 3, 4, 5, 6], 3),
    ]
    for case in test_cases:
        computed = answer(case[0])
        if computed != case[-1]:
            print '\nFailed case!', case[0]
            print 'Computed answer: ', computed
            print 'Expected answer: ', case[-1]
            return
    print 'All cases passed!'
test()
