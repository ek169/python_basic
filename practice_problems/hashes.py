def hashes(n):
    t = (n-1) * 2 - 1
    r = n / 2
    for x in range(0, r):
        s = 0
        while s <= t:
            if s == x or t - s == x * 2:
                for h in range(0, x+1):
                    print("#"),
                    s += 1
            else:
                print(" "),
                s += 1
        print("")
    for y in range(r-1, -1, -1):
        s = 0
        while s <= t:
            if s == y or t - s == 2 * y:
                for h in range(0, y + 1):
                    print("#"),
                    s += 1
            else:
                print(" "),
                s += 1
        print("")

# for