# задача про велосипедистов


def dist(t, params):
    x, v = params
    minpos = maxpos = x[0] + v[0] * t

    for i in range(1, len(x)):
        nowpos = x[i] + v[i] * t
        minpos = min(minpos, nowpos)
        maxpos = max(maxpos, nowpos)
    return maxpos - minpos


def check(m, eps, params):
    return dist(m + eps, params) >= dist(m, params)

def lbinsearch(l, r, eps, check, params):
    while l + eps < r:
        m = (l + r) / 2

        if check(m, eps, params):
            r = m
        else:
            l = m

    return l


def main(x, v, eps):
    return lbinsearch(0, max(x[len(x) - 1], v[len(v) - 1]), eps, check, (x, v))


if __name__ == '__main__':
    x = [10, 20]
    v = [94, 93]
    eps = 1e-13

    print(main(x, v, eps))
