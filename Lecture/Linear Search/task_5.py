# задачи на два прохода.

# дана последовательность слов. Вывести все самые короткие слова через пробел

def findminword(seq):
    if len(seq) == 0:
        return ''

    minlen = len(seq[0])

    # первый проход - ищем минимальную длину символа
    for i in range(len(seq)):
        if len(seq[i]) < minlen:
            minlen = len(seq[i])

    ans = []

    # второй проход - находим все объекты у которых длина равна минимально найденному значению
    for word in seq:
        if len(word) == minlen:
            ans.append(word)

    return ' '.join(ans)

print(findminword([]))