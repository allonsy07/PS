N = int(input())
info = []
for i in range(N):
    name, korea, english, math = map(int, input().split())
    info.append([name, korea, english, math])

info.sort(key = lambda x : (-x[1], x[2], -x[3],x[0]))

for i in info:
    print(i[0])