n,m = map(int,input().split())

zido = []
temp = [[0]*m for _ in range(n)]

for _ in range(n):
    zido.append(list(map(int,input().split())))

#머리 아파서 답지 한번 보고 구현해볼라 했는데 이 방법 외에는 생각이 안나서 그대로 구현 함

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def virus(x,y):
    temp[x][y] = 2
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if nx >= 0 and ny >= 0 and nx < n and ny < m:
            if temp[nx][ny] == 0:
                virus(nx,ny)

def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1
    return score

def DFS(count):
    global result
    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = zido[i][j]

        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i,j)
            
        result = max(result,get_score())
        return
            
    for i in range(n):
        for j in range(m):
            if zido[i][j] == 0:
                zido[i][j] = 1
                count += 1
                DFS(count)
                zido[i][j] = 0
                count -= 1


DFS(0)
print(result)

#시발아라알아나ㅣ러ㅜㅇㅁ;ㅏㅣㅑㅍ러;ㅑㅐㄷㅈ머;ㅐㅣ펌널;ㅐㅣㅓㅁ내;랻ㅁㅈ
#왜 일어나는지 모르겠는 에러만 존나 나네 시바라ㅣ언ㅁ;ㅣㅑ러;ㄷㅈ멒ㄴㅇㅁ;펒ㅁ
#아니 시발 답지랑 똑같이 했는데 왜 나만 안됌? 개ㅅㅂ