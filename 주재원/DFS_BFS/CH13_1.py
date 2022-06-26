from cmath import inf
from collections import deque
N, M, K, X = map(int, input().split())
info = []
graph = [[] for i in range(N+1)]
distance = [inf] * (N+1)

for i in range(M):
    info.append(list(map(int, input().split())))

for start_node, end_node in info:
    graph[start_node].append(end_node)

def bfs(graph, start, visited):
    queue = deque([[start, 0]])
    visited[start] = True
    while queue:
        v, dist = queue.popleft()
        if dist < distance[v]:
            distance[v] = dist
        distance[v] = dist
        for i in graph[v]:
            if not visited[i]:
                queue.append([i, dist+1])
                visited[i] = True

visited = [False] * (N+1)
cnt = 0

bfs(graph, X, visited)

for i, d in enumerate(distance):
    if d == K:
        print(i)
        cnt += 1
if cnt == 0:
    print(-1)
