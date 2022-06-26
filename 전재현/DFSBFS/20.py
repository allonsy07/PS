from collections import deque
import collections 

NOTAVOIDABLE = 30
AVOIDABLE = 20

N= int(input())
graph = []
for i in range(N):
    graph.append(list(map(str, input().split())))


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dsf(graph):
    obs_map = collections.Counter(find_Obs_point(graph)).most_common()
    print(obs_map) # 장애물 놓을 자리 후보는 구했음

    return 0
    
def find_Obs_point(graph):
    obs_map = []
    queue = deque()
    t_point = [(i,j) for i in range(N) for j in range(N) if graph[i][j]=="T"]
    for x,y in t_point:
        for i in range(4):
            nx = x
            ny = y
            while True:
                nx = nx + dx[i]
                ny = ny + dy[i]

                if nx < 0 or ny < 0 or nx >= N or ny >= N: #나가면 무시
                    queue.clear()
                    break
                if graph[nx][ny] == "S": #0이 아니면 증식 X
                    while queue:
                        obs_map.append(queue.pop())
                    break
                queue.append((nx,ny))

    return obs_map

def check_safe(graph):
    t_point = [(i,j) for i in range(N) for j in range(N) if graph[i][j]=="T"]
    for x,y in t_point:
        for i in range(4):
            nx = x
            ny = y
            while True:
                nx = nx + dx[i]
                ny = ny + dy[i]

                if nx < 0 or ny < 0 or nx >= N or ny >= N: #나가면 무시
                    break
                if graph[nx][ny] == "O": #0이 아니면 증식 X
                    break
                if graph[nx][ny] == "S": #0이 아니면 증식 X
                    return NOTAVOIDABLE

    return AVOIDABLE

dsf(graph)