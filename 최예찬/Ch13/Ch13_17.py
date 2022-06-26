n,k = map(int,input().split())

zido = []
for _ in range(n):
    zido.append(list(map(int,input().split())))

s,x,y = map(int,input().split())

score = [9999 for _ in range(k+1)]#바이러스 별 x,y에서 최단거리
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def get_score(): #현재 바이러스까지 거리 계산, -1의 갯수 세기
    s = 0
    for i in range(n):
        for j in range(n):
            if zido[i][j] == -1:
                s += 1
    return s

def dfs(x,y):
    zido[x][y] = -1 #방문 체크(거리 기록용)
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if nx >= 0 and ny >= 0 and nx < n and ny < n:
            if zido[nx][ny] == 0:
                dfs(nx,ny)
                zido[nx][ny] = 0 #방문 체크(거리 기록용)

            else: #바이러스와 마주한 경우
                score[zido[nx][ny]] = min(score[zido[nx][ny]], get_score()) #dfs로 각 바이러스까지의 최단거리 계산해서 저장

dfs(x-1,y-1)#x,y에서 

answer = 0 #아무 바이러스도 도달하지 못한다면
for i in range(k,0,-1):#바이러스의 경쟁을 고려하여 가장 우선순위가 낮은 바이러스부터 확인
    if score[i] <= s: #s초가 되기 전에 x,y로 도달할 수 있는 바이러스
        answer = i

print(answer)
    


