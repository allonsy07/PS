n, m = map(int,input().split())
balls = list(map(int, input().split()))

balls.sort()

weights = list()

for i in range(1,m+1):
    weights.append(balls.count(i))

cnt = 0

for i in range(m):
    for j in range(m):
        if i >= j:
            continue
        cnt += weights[i] * weights[j]

print(cnt)
