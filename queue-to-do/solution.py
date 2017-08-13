""" Tim Hung timhung1010@gmail.com """

def answer(start, length):
    return 0

def test():
    test_cases = [
        (0, 3, 2),
        (17, 4, 14)
    ]
    for case in test_cases:
        computed = answer(case[0], case[1])
        if computed != case[-1]:
            print '\nFailed case!', case[0], case[1]
            print 'Computed answer: ', computed
            print 'Expected answer: ', case[-1]
            return
    print 'All cases passed!'
test()
