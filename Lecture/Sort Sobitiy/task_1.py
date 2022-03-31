# Сайт посетило N человек, для каждого известно время входа на сайт In, и время выхода с сайта Out.
# Считается, что человек был на сайте с момента In, по Out, включительно


# Определите, какое максимальное кол-во человек было на сайте одновременно



if __name__ == '__main__':
    In = list(map(int, input().split()))
    Out = list(map(int, input().split()))

    event = []
    for i in range(len(In)):
        event.append((In[i], -1))   # пришел
        event.append((Out[i], 1))   # вышел

    event.sort()
    online = 0
    maxonline = 0
    for i in range(len(event)):
        if event[i][1] == -1:
            online += 1
        if event[i][1] == 1:
            online -= 1
        maxonline = max(online, maxonline)

    print(maxonline)


