N, M = map(int, input().split())
K = list(map(int, input().split()))

comb = 0

for i, k in enumerate(K):
    for j in range(i+1, len(K)):
        if K[i] == K[j]:
            continue
        comb += 1
        
print(comb)