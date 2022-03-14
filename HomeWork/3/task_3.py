def main(seq):
    mdict = {}

    for elem in seq:
        if elem in mdict:
            mdict[elem] += 1
        else:
            mdict[elem] = 1

    res = []

    for k, v in mdict.items():
        if mdict[k] == 1:
            res.append(k)

    print(*res)

if __name__ == '__main__':
    seq = [int(digit) for digit in input().split()]
    main(seq)