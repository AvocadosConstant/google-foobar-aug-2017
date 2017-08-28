def banana_game(b1, b2):
    if b1 == b2:
        return b1, b2
    b1, b2 = min(b1, b2), max(b1, b2)
    b2 -= b1
    b1 *= 2
    return min(b1, b2), max(b1, b2)

def count_banana_games(b1, b2):
    cur = (b1, b2)
    #print cur
    visited = set([cur])

    cur = banana_game(*cur)

    rounds_until_stable = 0
    while cur not in visited:
        #print cur
        rounds_until_stable += 1
        visited.add(cur)
        cur = banana_game(*cur)
    """
    if cur[0] == cur[1]:
        if b1 < b2:
            print '{}\t{}\t\t{}'.format(rounds_until_stable, (b1, b2), 1.0 * b2 / b1)
    """
    return rounds_until_stable, cur[0] != cur[1]

dim = 512
for y in range(dim, 0, -1):
    row = []
    for x in range (dim):
        #row.append(' ' if count_banana_games(x, y)[1] else 'X')
        cbg = count_banana_games(x, y)
        row.append(' ' if (y < x or cbg[1]) else str(cbg[0]))
    print y, '\t', ' '.join(row)

#print count_banana_games(9, 7)
