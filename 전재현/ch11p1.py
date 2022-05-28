n = map(int, input())
m = list(map(int, input().split()))

m.sort(reverse=True)
team = 0
while(m):
  pear = m[0]
  del m[0:pear]

  team += 1

print("team number : ", team)

