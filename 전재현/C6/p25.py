'''N = int(input())'''
N = 5
'''
array = list(map(int, input().split()))'''
array = [2,1,2,6,2,4,3,3]
maparray = [0 for _ in range(N)]
for i in array:
    if i > N:
        continue
    maparray[i-1] += 1

num_array = len(array)
failrate = []
for i, n in enumerate(maparray):
    if i == N:
        continue
    failrate.append([i+1, n/num_array])
    num_array -= n

failrate = sorted(failrate, key = lambda fail: fail[1], reverse=True)
for fail in failrate:
    print(fail[0], end=' ')

