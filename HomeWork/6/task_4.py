if __name__ == '__main__':
    a, k, b, m, x = list(map(int, input().split()))
    l = 0
    r = x * 2 // min(a, b) + 1

    while l < r:
        days = (l + r) // 2
        d = days // k
        f = days // m
        res = (days - d) * a + (days - f) * b

        if res >= x:
            r = days
        else:
            l = days + 1

    print(l)

