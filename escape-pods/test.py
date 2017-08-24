from solution import answer

class test_case:
    def __init__(self, entrances, exits, path, answer):
        self.entrances = entrances
        self.exits = exits
        self.path = path
        self.answer = answer

    def __repr__(self):
        return (
            "\n\tTest Case\n"
            "\t=========\n"
            "\tEntrances:\t{}\n"
            "\tExits:\t\t{}\n"
            "\tPaths:\t\t{}\n"
            "\tAnswer:\t\t{}\n"
        ).format(self.entrances, self.exits, self.path, self.answer)


def test():
    test_cases = [
        test_case(
            [0],
            [3],
            [[0, 7, 0, 0],
             [0, 0, 6, 0],
             [0, 0, 0, 8],
             [9, 0, 0, 0]],
            6),
        test_case(
            [0, 1],
            [4, 5],
            [[0, 0, 4, 6, 0, 0],
             [0, 0, 5, 2, 0, 0],
             [0, 0, 0, 0, 4, 4],
             [0, 0, 0, 0, 6, 6],
             [0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0]],
            16)
    ]
    for case in test_cases:
        computed = answer(case.entrances, case.exits, case.path)
        if computed != case.answer:
            print '\nFailed case!', case
            print 'Computed answer:\t', computed
            return
    print 'All cases passed!\n'
test()
