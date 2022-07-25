N, M = map(int, input().split())
INF = int(1e9)
graph = [[INF]*(N+1) for _ in range(N+1)]
for _ in range(M):
  a, b = map(int, input().split())
  graph[a][b] = 1


for a in range(1, N+1):
  for b in range(1, N+1):
    if a==b:
      graph[a][b] = 0

for k in range(1, N+1):
  for a in range(1, N+1):
    for b in range(1, N+1):
      graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

result = 0
for a in range(1, N+1): # 각 node에 대해서
  count = 0
  for b in range(1, N+1): # 연결된 각각의 node들의 연결방향에 관계없이 전부 존재하면 순위를 알 수 있다.
    if graph[a][b] != INF or graph[b][a] != INF:
      count += 1
  if count == N: # 따라서 count가 N이 되었다면 순위를 알 수 있다.
    result += 1

print(result)