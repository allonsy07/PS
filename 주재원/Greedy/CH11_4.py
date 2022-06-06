N = int(input())
M = list(map(int, input().split()))
M.sort()
money = 1

for m in M:
    if money < m:
        break
    else:
        money += m

print(money)