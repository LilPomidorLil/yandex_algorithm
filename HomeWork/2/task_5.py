def main(seq, s):

    left_ans = 0
    right_ans = 0
    ans = True
    left = -10
    right = 100000

    for i in range(len(seq)):

        if (s % 2 != 0) and (seq[i] == int((s / 2))):
            print(seq[i])
            ans = False
        else:
            if (seq[i] > left) and (seq[i] < int((s / 2))):
                left_ans = seq[i]
                left = seq[i]
            elif (seq[i] < right) and (seq[i] >= int((s / 2))):
                right_ans = seq[i]
                right = seq[i]
    if ans:
        print(left_ans, " ", right_ans)


if __name__ == '__main__':
    length, count_cobe = input().split()

    seq = [int(cobe) for cobe in input().split()]
    main(seq, int(length))


