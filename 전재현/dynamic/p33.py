N = int(input())

array = []
for i in range(N):
    array.append(list(map(int, input().split())))

d = [0]*(N)
d[0] = 0
for i in range(N):
    if i + array[i][0] <= N:
        d[i] = max(array[i][1], d[i])
    j = i
    while True:
        try:
            if j + array[j][0] + array[j + array[j][0]][0] <= N:
                d[j + array[j][0]] = max(d[j]+array[j+ array[j][0]][1], d[j + array[j][0]])
                j += array[j][0]
            else:
                break
        except:
            break

print(max(d))