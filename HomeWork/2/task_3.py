def main(seq):

    if len(seq) == 1:
        print(0)
        return


    i = 0
    j = len(seq) - 1
    min = 0

    stop = int(len(seq) / 2)

    while (i != stop):

        if seq[i] != seq[j]:
            min += 1

        i += 1
        j -= 1

    print(min)

if __name__ == '__main__':

    stroka = str(input())
    seq = list(stroka)
    main(seq)
