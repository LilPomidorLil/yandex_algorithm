# дана последовательность чисел длиной N и M
# сколько нулей на полуинтервале [L, R)?

if __name__ == '__main__':
    seq = list(map(int, input().split()))

    prefixzero = [0] * (len(seq) + 1)

    for i in range(1, len(seq) + 1):
        prefixzero[i] = prefixzero[i-1] + 1 if seq[i-1] == 0 else prefixzero[i-1]

    ans = prefixzero[10] - prefixzero[5]
    print(ans)
