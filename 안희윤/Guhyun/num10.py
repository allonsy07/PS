key = []
lock = []
for i in range(3):
  a = list(map(int, input().split(',')))
  key.append(a)

for k in range(3):
  b = list(map(int, input().split(',')))
  lock.append(b)


M = len(key)
N = len(lock)

lock_0 = []
for i in range(M):
  ls = lock[i]
  if 0 not in ls:
    continue
  k = ls.index(0)
  lock_0.append([i,k])