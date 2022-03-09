def main(seq):

    left = -10
    left_arr = []
    for i in range(10):

        if seq[i] == 1:
            left_arr.append(abs(left - i))

        if seq[i] == 2:
            left = i


    right = 20
    right_arr = []

    for i in range(9, -1, -1):

        if seq[i] == 1:
            right_arr.append(abs(right - i))

        if seq[i] == 2:
            right = i

    right_arr = right_arr[::-1]
    min_arr = []
    for i in range(len(right_arr)):
        min_arr.append(min(right_arr[i], left_arr[i]))

    print(max(min_arr))


if __name__ == '__main__':

    seq = [int(masi) for masi in input().split()]
    main(seq)






