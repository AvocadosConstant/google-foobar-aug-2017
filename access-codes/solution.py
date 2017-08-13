""" Tim Hung timhung1010@gmail.com """

def answer(l):
    triple_count = 0
    for x_i in range(len(l) - 2):
        for y_i in range(x_i + 1, len(l) - 1):
            if l[y_i] % l[x_i] == 0:
                for z_i in range(y_i + 1, len(l)):
                    if l[z_i] % l[y_i] == 0:
                        triple_count += 1
    return triple_count

def test():
    test_cases = [
        ([1, 1, 1], 1),
        ([1, 2, 3, 4, 5, 6], 3),
        #([], ),
    ]
    for case in test_cases:
        computed = answer(case[0])
        if computed != case[-1]:
            print '\nFailed case!', case[0]
            print 'Computed answer: ', computed
            print 'Expected answer: ', case[-1]
    print 'All cases passed!'
test()
