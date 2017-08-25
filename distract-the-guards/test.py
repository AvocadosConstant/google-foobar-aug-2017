from solution import answer

class test_case:
    def __init__(self, banana_list, answer):
        self.banana_list = banana_list
        self.answer = answer

    def __repr__(self):
        return (
            "\n\tTest Case\n"
            "\t=========\n"
            "\tbanana_list:\t{}\n"
            "\tAnswer:\t\t{}\n"
        ).format(
            self.banana_list,
            self.answer)


def test():
    test_cases = [
        test_case(
            [1, 1],
            2
        ),
        test_case(
            [1, 7, 3, 21, 13, 19],
            0
        ),
    ]
    for case in test_cases:
        computed = answer(case.banana_list)
        if computed != case.answer:
            print '\nFailed case!', case
            print 'Computed answer:\t', computed
            print '\n============================='
            #return
    print 'All cases passed!\n'
test()
