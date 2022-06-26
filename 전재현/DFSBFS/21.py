from collections import deque
import queue

N, L, R = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))

def dfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= N: #나가면 무시
                break
            if abs(graph[x][y] - graph[nx][ny]) >= L or abs(graph[x][y] - graph[nx][ny]) <= R:
                queue.append((nx, ny))

