import heapq
INF = int(1e9)
N, M = map(int, input().split())

graph = [[] for i in range(N+1)]
distance = [INF]*(N+1)

for _ in range(M):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

q = []
distance[1] = 0
heapq.heappush(q, (distance[1], 1))

while q:
  dist, now = heapq.heappop(q)
  if distance[now] < dist:
    continue
  for i in graph[now]:
    cost = dist + 1
    if cost < distance[i]:
      distance[i] = cost
      heapq.heappush(q, (cost, i))

dist_to_agit = 0
num_agit = 0
several_agit = 0

for i in range(1, N+1):
  if distance[i] == INF:
    continue
  if dist_to_agit < distance[i]:
    several_agit = 1
    num_agit = i
    dist_to_agit = distance[i]
  elif dist_to_agit == distance[i]:
    several_agit += 1

print(num_agit, dist_to_agit, several_agit)