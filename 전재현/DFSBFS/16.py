from collections import deque
INF = 300001

N, M = map(int, input().split())
graph = []
for i in range(M):
    graph.append(list(map(int, input())))
