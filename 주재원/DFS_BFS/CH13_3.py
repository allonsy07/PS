from collections import deque

N, K = map(int,input().split())

graph = []

for i in range(N):
    graph.append(list(map(int, input().split())))

start = []
for i in range(N):
    for j in range(N):
        if graph[i][j] != 0:
            start.append([(i,j), graph[i][j], 0])
start.sort(key=lambda x: x[1])
S, X, Y = map(int, input().split())
dx = [-1, 1, 0, 0]
dy = [0,0, -1, 1]

def bfs(start):
    queue = deque()
    for (x,y), value, time in start:
        queue.append((x, y, value, time))
    while queue:
        x, y, value, time = queue.popleft()
        if time == S:
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = value
                queue.append((nx, ny, value, time+1))

bfs(start)
print(graph[X-1][Y-1])