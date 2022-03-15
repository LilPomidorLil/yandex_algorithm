# if __name__ == '__main__':
#
#     mdict = {}
#
#     with open('input.txt', 'r', encoding='utf8') as fin:
#
#         for line in fin:
#             key, value = line.split(' ')
#
#             if key not in mdict:
#                 mdict[key] = 0
#
#
#
#             mdict[key] += int(value)
#
#         for key, value in mdict.items():
#             print(str(key) + ' ' + str(value))


# перепишем в более лаконичной форме

if __name__ == '__main__':
    mdict = {}

    with open('input.txt', 'r', encoding='utf8') as fin:
        for line in fin:
            key, value = line.split()
            mdict[key] = mdict.get(key, 0) + int(value)

        for key, value in sorted(mdict.items()):
            print(str(key) + ' ' + str(value))

