N = int(input())

array = []
d = []
for i in range(N):
    temp = list(map(int, input().split()))
    array.append(temp)
    d.append([0]*len(temp))

count = 0

d[0][0] = array[0][0]
for i in range(1,N):
    for j in range(i+1):
        if j == 0:
            d[i][j] = d[i-1][j]+array[i][j]
        elif j == i:
            d[i][j] = d[i-1][j-1]+array[i][j]
        else:
            d[i][j] = max(d[i-1][j-1]+array[i][j], d[i-1][j]+array[i][j])

print(max(d[-1]))
