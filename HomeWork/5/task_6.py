
def main(mlist):
    sum = mlist[0]
    for i in range(1, n):
        sum -= mlist[i]
        if sum > 0:
            return -1
        sum = mlist[i]

    return mlist[-1] - mlist[0]

if __name__ == '__main__':
    n = int(input())
    mlist = list(map(int, input().split()))


    print(main(mlist))








