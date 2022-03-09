def main(seq):
    if len(seq) == 0:
        return

    max = seq[0]
    for i in range(1, len(seq)):
        if seq[i] > max:
            max = seq[i]


    count = 0
    for i in range(0, len(seq)):
        if seq[i] == max:
            count += 1

    print(count)


if __name__ == '__main__':
    lst = []

    inp = input()

    while inp != '0':
        lst.append(int(inp))
        inp = input()


    main(lst)