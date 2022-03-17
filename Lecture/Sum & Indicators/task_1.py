# префиксные суммы
if __name__ == '__main__':
    # создаем массив с префиксными суммами
    mlist = [5, 3, 8, 1, 4, 6]
    prefixsum = [0] * (len(mlist) + 1)

    for i in range(1, len(mlist) + 1):
        prefixsum[i] = prefixsum[i-1] + mlist[i-1]

    print(f"Массив с префиксными суммами\n{prefixsum}", end = '\n\n')

    # задача - найти сумму на полуинтервале от 2 до 5
    # ответ за O(1) = prefixsum[5] - prefixsum[2]

    ans = prefixsum[5] - prefixsum[0]
    print("Sum between 2 and 5: ", ans, end = '\n\n')
