

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


def check_res(seq, check_f, x):
    ans = lbinsearch(0, len(seq) - 1, check_f, (seq, x))

    if not check_f(ans, (seq, x)):
        return len(seq)
    return ans

def main(seq, x):
    if x not in seq:
        return 0, 0
    first = check_res(seq, check, x)
    second = check_res(seq, checkstrogo, x)
    return first+1, second



if __name__ == '__main__':
    N = int(input())
    seq = list(map(int, input().split()))
    M = int(input())
    req = list(map(int, input().split()))
    ans = []
    for x in req:
        ans.append(main(seq, x))

    for i in range(M):
        print(*ans[i], end = '\n')
