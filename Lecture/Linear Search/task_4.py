# дана последовательность чисел длиной N

# найти минимальное четное число в последовательности или вывести -1, если такого не существует

def findminchet(seq):
    ans = -1
    flag = False


    for i in range(len(seq)):
        if (seq[i] % 2 == 0) and (not flag or ans > seq[i]):
            ans = seq[i]
            flag = True
    return ans

