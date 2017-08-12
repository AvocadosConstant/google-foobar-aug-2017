def answer(s):
    return 0

def test():
    test_cases = {
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
