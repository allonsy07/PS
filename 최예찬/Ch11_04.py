n = int(input())
coins = list(map(int, input().split()))

coins.sort()

a = 1

for coin in coins:
    if coin == a:
        a += coin
    elif coin < a:
        a += coin
    else:
        break

print(a)
