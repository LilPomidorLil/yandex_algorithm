def main(seq):
    if len(seq) == 0:
        return
    sum = 0
    max = seq[0]

    for i in range(len(seq)):
        sum += seq[i]

        if seq[i] > max:
            max = seq[i]

    print(sum - max)

if __name__ == '__main__':
    n = input()
    seq = [int(data) for data in input().split()]

    main(seq)

