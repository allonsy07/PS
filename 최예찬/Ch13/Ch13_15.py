from collections import deque

n, m, k, x = map(int,input().split())

roads = [[] for _ in range(n+1)] #인접 리스트 사용
for i in range(m):
    a, b = map(int,input().split())
    roads[a].append(b)

queue = deque() #BFS 사용

queue.append(x) #초기값 설정

visit = [] #방문 처리
visit.append(x)

dist = [9999999 for _ in range(n+1)] #최단 거리 저장

for i in range(k): #최단 거리 k인 도시를 찾으므로 k번 BFS 수행시 k 길이 도시 찾을 수 있음
    for a in roads[queue.popleft()]: #현재도시에 연결된 도시들
        queue.append(a) #quque에 넣고
        visit.append(a) #방문처리
        if dist[a] > i+1:
            dist[a] = i+1 #도시별로 최단거리 기록
        
if k not in dist:
    print(-1)

else:
    for i,a in enumerate(dist):
        if a == k:
            print(i)


    
    
