# даны 2 отсортированные последовательности чисел (длиной N и M соответственно)
# Необходимо слить их в одну отсортированную последовательность

if __name__ == '__main__':
    seq1 = list(map(int, input().split()))
    seq2 = list(map(int, input().split()))

    merged = [0] * (len(seq1) + len(seq2))
    first1= first2 = 0

    for k in range(len(seq1) + len(seq2)):
        if first1 != len(seq1) and (first2 == len(seq2) or seq1[first1] <= seq2[first2]):
            merged[k] = seq1[first1]
            first1 += 1
        else:
            merged[k] = seq2[first2]
            first2 += 1

    print(merged)


