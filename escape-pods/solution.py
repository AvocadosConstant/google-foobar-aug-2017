""" Tim Hung timhung1010@gmail.com """

inf = float('inf')

def answer(entrances, exits, path):
    caps = [list(row) for row in path]
    source = len(caps)
    sink = source + 1

    for i, room in enumerate(caps):
        room.extend([0, inf if i in exits else 0])

    caps.append([0] * (sink + 1))

    for entrance in entrances:
        caps[source][entrance] = inf

    print '\n\ncaps:\n', '\n'.join(['\t\t\t' + str(row) for row in caps]),

    return 0
