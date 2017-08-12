def answer(l, t):
    return [-1, -1]

test_cases = [
    (
        [4, 3, 10, 2, 8],
        12,
        [2, 3]
    ),
    (
        [1, 2, 3, 4],
        15,
        [-1, -1]
    ),
    (
        [15, 10, 5, 15],
        15,
        [0, 0]
    )
]
for case in test_cases:
    computed = answer(case[0], case[1])
    print 'Passed case!' if computed == case[-1] else 'Failed case!'
