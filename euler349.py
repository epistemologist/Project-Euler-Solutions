def euler349():
    import itertools

    # Langton's ant from rosettacode

    width = 128
    height = 128
    nsteps = 20000

    class Dir:
        up, right, down, left = range(4)

    class Turn:
        left, right = False, True

    class Color:
        white, black = '.', '#'

    M = [[Color.white] * width for _ in range(height)]
    out = []
    answers = []
    x = width // 2
    y = height // 2
    dir = Dir.up

    i = 0
    while i < nsteps and 0 <= x < width and 0 <= y < height:
        turn = Turn.left if M[y][x] == Color.black else Turn.right
        M[y][x] = Color.white if M[y][x] == Color.black else Color.black

        dir = (4 + dir + (1 if turn else -1)) % 4
        dir = [Dir.up, Dir.right, Dir.down, Dir.left][dir]
        if dir == Dir.up:
            y -= 1
        elif dir == Dir.right:
            x -= 1
        elif dir == Dir.down:
            y += 1
        elif dir == Dir.left:
            x += 1
        else:
            assert False
        N = list(itertools.chain.from_iterable(M))
        out.append(N.count('#'))
        if (i % 100 == 0):
            print i, N.count('#')
        if (i > 10800):
            print i, N.count(
                '#'), out[-1], out[-104], out[-105], out[-1]-out[-105], 10**18-i, (10**18-i) % 104
        if (i > 10800) and (10**18-i) % 104 == 0:
            answers.append(out[-1]+12*(10**18-i)/104)
        i += 1

    print answers
    #print ("\n".join("".join(row) for row in M))


print euler349()
