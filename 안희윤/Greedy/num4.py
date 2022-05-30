
from itertools import combinations

N = int(input())
coins = list(map(int, input().split()))
coins.sort()
can_make = set(coins)
result = 1
A = True

while A == True:
    candidate = []
    if result in coins:
        result += 1
        continue

    for l in range(len(coins)):
        candidate.append(coins[l])

    for i in range(2, len(candidate) + 1):
        memory = result
        comb = list(combinations(candidate, i))
        for k in comb:
            nums = list(map(int, k))
            sums = sum(nums)
            can_make.add(sums)

    if result in can_make:
        result+=1
    else:
        answer = result
        A = False

print(answer)

