if __name__ == '__main__':
    n = int(input())
    mdict = {}
    for i in range(n):
        key, val = list(map(int, input().split()))

        if key not in mdict:
            mdict[key] = 0
        mdict[key] += val

    sorted_items = sorted(mdict.items())

    # print
    for i in range(len(sorted_items)):
        print(str(sorted_items[i][0]) + ' ' + str(sorted_items[i][1]), end = '\n')



