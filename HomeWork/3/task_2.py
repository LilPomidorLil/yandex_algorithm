def main(seq):
    myset = [[] for _ in range (10)]

    for x in seq:

        if x not in myset[x % 10]:
            myset[x % 10].append(x)
            print('NO')
        else:
            print('YES')


if __name__ == '__main__':
    seq = [int(digit) for digit in input().split()]
    main(seq)