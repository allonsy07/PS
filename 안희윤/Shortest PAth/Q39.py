# heap을 이용한 다익스트라 알고리즘 활용
import heapq
INF = int(1e9)
T = int(input()) # test case
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(T):
  N = int(input()) # 맵의 크기
  distance = [[INF]*N for _ in range(N)] # 맵의 크기만큼 INF로 초기화된 그래프
  space = [] # 각 칸의 코스트를 반영하는 space

  for _ in range(N):
    space.append(list(map(int, input().split())))
  q = []
  distance[0][0] = space[0][0]
  heapq.heappush(q, (space[0][0], [0,0])) # cost, 좌표를 heap 구조에 넣어줌
  while q:
    dist, now = heapq.heappop(q)
    # 이미 꺼냈던 node의 distance에 대하여, 현재 거리 테이블에서 해당 노드까지의 최단거리보다 중복되어 꺼내는 경우의 dist가 작을 것이기 때문에 continue 처리가 가능
    if distance[now[0]][now[1]] < dist:
      continue

    for i in range(4):
        x = now[0] + dx[i]
        y = now[1] + dy[i]
        if x < 0 or x > N-1 or y < 0 or y > N-1:
          continue
        cost = dist + space[x][y]
        if cost < distance[x][y]:
          distance[x][y] = cost
          heapq.heappush(q, (cost, [x,y]))

  print(distance[-1][-1])