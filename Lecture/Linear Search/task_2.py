# дана последовательность чисел длиной N (N > 0)

# найти максимальное число в последовательности

def findmax(seq):

    max = 0

    for i in range(1, len(seq)):
        if seq[i] > seq[max]:
            max = i

    return seq[max], max

print(findmax([100]))