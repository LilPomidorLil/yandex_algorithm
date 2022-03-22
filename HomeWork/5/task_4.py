import time
if __name__ == '__main__':

    mlist = list(str(input()))
    stack = []
    flag = True
    for l in mlist:
        if l == '(':
            stack.append(l)
        elif l == ')':
            if len(stack) == 0:
                flag = False
                break

            r = stack.pop()
            if r == "(" and l ==")":
                continue

    if flag and len(stack) == 0:
        print("YES")
    else:
        print("NO")


