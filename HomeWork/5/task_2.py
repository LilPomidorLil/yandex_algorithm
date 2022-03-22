if __name__ == '__main__':
    n = int(input())
    mlist = list(map(int, input().split()))

    sum = 0
    bestsum = mlist[0]

    for i in range(n):
        sum += mlist[i]

        bestsum = max(bestsum, sum)

        sum = max(sum, 0)

    print(bestsum)
