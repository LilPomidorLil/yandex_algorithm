# дана последовательность чисел длиной N (N > 1)

# найти максимальное число в последовательности и второе по величине число (такое, которое будет максимальным,
# если вычеркнуть из последовательности одно максимальное число)

def find2max(seq):
    max1 = min(seq[0], seq[1])
    max2 = max(seq[1], seq[0])

    for i in range(2, len(seq)):
        if seq[i] > max2:
            max1 = max2
            max2 = seq[i]

        if seq[i] > max1 and seq[i] < max2:
            max1 = seq[1]

    return max2, max1

print(find2max([10, 4, 1, 3]))