# множество

setsize = 10
myset = [[] for _ in range(setsize)]


def add(seq):

    for x in seq:
        if x in myset[x % setsize]:
            continue

        myset[x % setsize].append(x)

def find(x):
    for this in myset[x % setsize]:
        if this == x:
            return True
    return False

def delete(x):
    xlist = myset[x % setsize]
    for i in range(len(xlist)):
        if x == xlist[i]:
            xlist[i] = xlist[len(xlist) - 1]
            xlist.pop()
            return


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5, 6, 7, 7, 7, 7, 8, 90, 91, 234, 543, 12, 5456, 6542]
    add(a)
    print(myset)