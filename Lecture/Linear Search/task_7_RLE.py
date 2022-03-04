# сначала попробуем из строки получить строку, в которой каждая буква повторяется один раз

def pre_RLE(str_):
    if len(str_) == 0:
        return ''

    unique = []
    prev = str_[0]
    unique.append(prev)
    for i in range(len(str_)):
        if str_[i] != prev:
            unique.append(str_[i])
            prev = str_[i]

    return ''.join(unique)

# теперь добавим с учетом счетчика

def RLE(str_):

    unique = []
    prev = str_[0]
    flag = 1
    unique.append(prev)

    for i in range(1, len(str_)):
        if str_[i] != prev:
            if flag > 1:
                unique.append(str(flag))
                unique.append(str_[i])
                prev = str_[i]
                flag = 0
            elif flag == 1:
                unique.append(str_[i])
                prev = str_[i]
                flag = 0

        flag += 1

        if (i == len(str_) - 1) and flag > 1:
            unique.append(str(flag))


    return ''.join(unique)