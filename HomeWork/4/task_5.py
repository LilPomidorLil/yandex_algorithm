if __name__ == '__main__':
    n = int(input())
    reply = [0] * n
    theme = [''] * n

    for i in range(n):
        num = int(input())

        if num == 0:
            reply[i] = i
            theme[i] = str(input())
            input()
        else:
            reply[i] = reply[num - 1]
            input()

    ans = {}

    for r in reply:
        ans[r] = ans.get(r, 0) + 1

    mlist = []
    for top in ans:
        mlist.append((-ans[top], top))

    mlist.sort()
    print(theme[min(mlist)[1]])

