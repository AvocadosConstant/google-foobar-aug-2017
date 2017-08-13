""" Tim Hung timhung1010@gmail.com """

# Uses some nifty XOR tricks!
def xor_range(start, end):
    if start == 0 or start == 1:
        vals = [end, 1, end + 1, 0]
        return vals[end % 4]
    return xor_range(0, start - 1) ^ xor_range(0, end)

def answer(start, length):
    solution = 0
    # Handle line skipping
    for i in range(length):
        first = start + length * i
        last = first + length - i - 1
        solution ^= xor_range(first, last)
    return solution

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
    print 'All cases passed!'
test()
