from collections import deque
INF = 300001

N, M, K, X = map(int, input().split())

distance_map = [[] for _ in range(N)]
for i in range(M):
    city, load = map(int, input().split())
    distance_map[city-1].append(load) #distance_map의 N-1번째 리스트에는 N도시와 연결된 도시를 저장

graph = [] 
#목적은 X도시에서 최단거리 K인 도시를 구하는게 목적이므로
#X도시에서 다른 도시 까지의 거리만 계산하면 됨
for i in range(N):
    graph.append(INF) 
    if i == X-1:
        graph[i] = 0 

def dfs(x):
    queue = deque()
    queue.append((x)) #시작도시
    while queue:
        x = queue.popleft()
        for y in distance_map[x-1]: #X도시와 연결된 도시들을 하나씩 가져옴
            graph[y-1] = min(graph[x-1] + 1, graph[y-1]) 
            #연결된 도시까지의 거리 = 전 도시까지의 거리+1, 기존 구해진 거리 중 최소값
            queue.append(y)
            #연결된 도시를 queue에 넣음

    pos = [i+1 for i in range(len(graph)) if graph[i]==K] #K거리인 도시들은 pos에 넣음
    if not pos:
        pos.append(-1)
    for i in pos:
        print(i)

dfs(X)

###########
#존재하는 단방향 도로를 [x] = y1,y2 형식으로 저장
#X 도시를 입력받으면 연결된 도시를 스택에 넣는다
#스택에서 하나씩 꺼내 연결된 도시까지의 거리를 입력한다.