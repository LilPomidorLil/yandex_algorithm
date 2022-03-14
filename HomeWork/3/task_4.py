if __name__ == '__main__':
    max_digit = int(input())
    n_set = set(range(1, max_digit + 1))

    word = input().strip()

    while word != 'HELP':

        this_set = set(map(int, word.split()))

        word = input().strip()

        if word == 'YES':
            n_set.intersection_update(this_set)
        else:
            n_set.difference_update(this_set)

        word = input().strip()

    print(*n_set)