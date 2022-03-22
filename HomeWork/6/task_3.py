def checkr(m, params):
    a, b, c, d = params
    return a * (m**3) + b * (m**2) + c*m + d > 0

def checkl(m, params):
    a, b, c, d = params
    return a * (m**3) + b * (m**2) + c*m + d < 0

def binsearch(l, r, eps, check, params):
    while l + eps < r:
        m = (l + r) / 2

        if check(m, params):
            r = m
        else:
            l = m
    return l


def main(params, eps):
    if params[0] >= 0:
        return binsearch(-1001, 1001, eps, checkr, params)
    return binsearch(-1001, 1001, eps, checkl, params)


if __name__ == '__main__':
    a, b, c, d = list(map(int, input().split()))
    eps = 1e-7
    print(main((a, b, c, d), eps))