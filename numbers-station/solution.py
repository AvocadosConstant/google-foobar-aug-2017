""" Tim Hung timhung1010@gmail.com """

def answer(l, t):
    start, cur_sum = 0, 0
    for end in range(len(l)):
        cur_sum += l[end]
        while cur_sum > t:
            cur_sum -= l[start]
            start += 1
        if cur_sum == t:
            return [start, end]
    return [-1, -1]

def test():
    test_cases = [
        ([4, 3, 5, 7, 8], 12, [0, 2]),
        ([4, 3, 10, 2, 8], 12, [2, 3]),
        ([1, 2, 3, 4], 15, [-1, -1]),
        ([15, 10, 5, 15], 15, [0, 0]),
        ([4, 4, 4, 4, 4], 12, [0, 2]),
        ([4, 4, 4, 5, 4], 13, [1, 3]),
        ([4, 4, 4, 4, 5], 13, [2, 4]),
        ([14, 4, 4, 4, 5], 13, [2, 4]),
        ([1, 2, 3], 6, [0, 2]),
        ([1], 1, [0, 0]),
        ([0], 0, [0, 0]),
        ([0], 1, [-1, -1]),
        ([1, 1, 2, 1, 1, 1, 1, 1], 2, [0, 1]),
        ([1,2,15,3,4], 15, [2,2]),
        ([1,2,16,3,4], 15, [-1,-1]),
        ([1,3,3,7], 6, [1,2]),
        ([1,2,3,99,88,77,3,2,1,7], 6, [0, 2]),
        ([6,5,6,7,11], 11, [0,1]),
        ([5,6,5,6,5,6,5,6], 11, [0,1]),
        ([11, 5, 6], 11, [0, 0]),
        ([10,0,1], 11, [0,2]),
        ([1,2,3], 6, [0,2])
    ]
    for case in test_cases:
        computed = answer(case[0], case[1])
        if computed != case[-1]:
            print '\nFailed case!', case
            print 'Computed answer: ', computed
            return
    print 'All cases passed!'
