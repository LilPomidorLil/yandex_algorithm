if __name__ == '__main__':
    mdict = {}
    with open('input.txt', 'r', encoding='utf8') as fin:
        for line in fin:
            for key in line.split():
                mdict[key] = mdict.get(key, 0) + 1

    fin.close()

    ans = []

    for key in mdict:
        ans.append((-mdict[key], key))
    ans.sort()

    for word in ans:
        print(word[1], end = '\n')
