# Сайт посетило N человек, для каждого известно время входа на сайт In, и время выхода с сайта Out.
# Считается, что человек был на сайте с момента In, по Out, включительно


# Определите, какое суммарное время на сайте был хотя бы один человек



if __name__ == '__main__':
    In = list(map(int, input().split()))
    Out = list(map(int, input().split()))

    event = []
    for i in range(len(In)):
        event.append((In[i], -1))   # пришел
        event.append((Out[i], 1))   # вышел

    event.sort()

    online = 0
    ans = 0
    for i in range(len(event)):
        if online > 0:
            ans += event[i][0] - event[i - 1][0]

        if event[i][1] == -1:
            online += 1
        else:
            online -= 1
    print(ans)
