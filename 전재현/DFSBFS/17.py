from collections import deque

N, K = map(int, input().split())
graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))

virus = []
for i in range(N):
    for j in range(N):
        if graph[i][j] != 0:
            virus.append([graph[i][j],i,j])

S, X, Y = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(virus):
    s = 0
    temp_b = -1
    queue = deque()
    for vir in virus:
        queue.append(vir)

    while queue:
        b,x,y = queue.popleft() #큐에서 꺼냄
        if temp_b - b == K-1: ##K번째 바이러스에서 첫번째 바이러스로 돌아올때마다 1초 증가
            s += 1
        if s == S: #S초만큼 증가했을 때 while 종료
            break
        temp_b = b #b는 현재 바이러스 temp_b는 다음 큐에서 사용할 이전 바이러스 번호

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= N: #나가면 무시
                continue
            
            if graph[nx][ny] != 0: #0이 아니면 증식 X
                continue
            else: 
                graph[nx][ny] = b
                queue.append((b,nx,ny)) #바이러스 번호, 위치를 큐에 삽입


bfs(virus=virus)

print(graph[X-1][Y-1])

#바이러스 번호별로 위치정보를 저장해둔다
#1번부터 위치를 꺼내 위치별 상하좌우를 1로 바꾸고 위치정보에 넣는다 (큐)
#S번 반복한다