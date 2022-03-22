if __name__ == '__main__':
    n_mass, n_quest = list(map(int, input().split()))

    mass = list(map(int, input().split()))

    prefixsum = [0] * (n_mass + 1)

    for i in range(1, n_mass + 1):
        prefixsum[i] = prefixsum[i-1] + mass[i - 1]

    ans_list = []
    for answer in range(n_quest):
        l, r = list(map(int, input().split()))
        ans_list.append(prefixsum[r] - prefixsum[l-1])

    print(*ans_list, sep = '\n')
