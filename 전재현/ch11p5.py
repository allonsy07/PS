n, m = map(int, input().split())
w = list(map(int, input().split()))

count = 0
for i in range(len(w)):
  for j in range(len(w)-i):
    if w[i] != w[j+i]:
      count += 1
      
print(count)