""" Tim Hung timhung1010@gmail.com """

def answer(s):
    right_count, salutes = 0, 0
    for char in s:
        if char == '>':
            right_count += 1
        elif char == '<':
            salutes += 2 * right_count
    return salutes

def test():
    test_cases = {
        '--->-><-><-->-': 10,
        '>----<': 2,
        '<<>><': 4
    }
    for case in test_cases:
        computed = answer(case)
        if computed != test_cases[case]:
            print '\nFailed case!', case
            print 'Computed answer: ', computed
            print 'Expected answer: ', test_cases[case]
            #return
    print 'All cases passed!'
test()
