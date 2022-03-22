

def check(m, params):
    seq, x = params
    return seq[m] >= x

def checkstrogo(m, params):
    seq, x = params
    return seq[m] > x


def lbinsearch(l, r, check, params):
    while l < r:
        m = (l + r) // 2

        if check(m, params):
            r = m
        else:
            l = m + 1
    return l

def check_res(params, check_f):
    seq = params[0]
    ans = lbinsearch(0, len(seq) - 1, check_f, params)
    if not check_f(ans, params):
        return len(seq)
    return ans


def main(params):
    first = check_res((params[0], params[1]), check)
    end = check_res((params[0], params[2]), checkstrogo)
    return end - first


if __name__ == '__main__':
    n = int(input())
    seq = list(map(int, input().split()))
    seq.sort()
    k = int(input())
    ans = []
    for i in range(k):
        start, end = list(map(int, input().split()))
        ans.append(main((seq, start, end)))
    print(*ans)