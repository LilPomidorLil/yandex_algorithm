# Дана отсортированная последовательность чисел длиной N и число K
# Найти кол-во пар чисел A, B, таких что, В - А > К.

if __name__ == '__main__':
    seq = list(map(int, input().split()))
    k = int(input())
    count = 0
    last = 0

    for first in range(len(seq)):
        while last < len(seq) and seq[last] - seq[first] <= k:
            last += 1
        count += len(seq) - last

    print(count)


