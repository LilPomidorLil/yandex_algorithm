if __name__ == '__main__':
    n, k = list(map(int, input().split()))
    x = list(map(int, input().split()))
    x.sort()
    l = 0
    r = x[-1] - x[0]

    while l < r:
        m = ( l + r) // 2
        count = 0
        maxright = x[0] - 1
        for now in x:
            if now > maxright:
                count += 1
                maxright = now + m

        if count <= k:
            r = m
        else:
            l = m + 1

    print(l)


