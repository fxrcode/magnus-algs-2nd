import sys


def test_closest_pair():
    from random import randrange, seed

    seed(2523)

    seq = [randrange(10**5) for _ in range(10)]

    # print(seq)
    def naive_f():
        dd = float("inf")
        for x in seq:
            for y in seq:
                if x == y:
                    continue
                d = abs(x - y)
                if d < dd:
                    xx, yy, dd = x, y, d
        print(xx, yy, dd)

    naive_f()

    def opt_f():
        dd = float("inf")
        seq.sort()
        for i in range(len(seq) - 1):
            x, y = seq[i], seq[i + 1]
            if x == y:
                continue
            d = abs(x - y)
            if d < dd:
                xx, yy, dd = x, y, d
        print(xx, yy, dd)

    opt_f()


def test_trav():
    def trav(seq, i=0):
        if i == len(seq):
            return
        trav(seq, i + 1)

    trav(range(10))
    trav(range(1000))


# test_closest_pair()
# test_trav()


def test_max_perm():
    M = [2, 2, 0, 5, 3, 5, 7, 4]
    print(M[2])  # c is mapped to a

    def naive_max_perm(M, A=None):
        pass


test_max_perm()
