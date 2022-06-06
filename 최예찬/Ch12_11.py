import sys

n = int(input())
k = int(input())

z_map = list() 
z_map.append([3]*(n+2))
for i in range(n):
    z_map.append([3]+[0]*n+[3])
z_map.append([3]*(n+2))

for i in range(k):
    a,b = map(int,input().split())
    z_map[a][b] = 2

l = int(input())

c_c = 'R'
head = [1,1]
tail = [1,1]
z_map[1][1] = 1 
clock = 1

print(z_map)

for i in range(l):
    x,c = map(str,input().split())
    for j in range(int(x)):
        if c_c == 'R':
            head[1] += 1

        elif c_c == 'L':
            head[1] -= 1

        elif c_c == 'U':
            head[0] -= 1

        elif c_c == 'D':
            head[0] += 1

        if z_map[head[0]][head[1]] == 1 or z_map[head[0]][head[1]] == 3: #벽이나 자기 몸에 부딪힐 경우
                print(clock)
                sys.exit()
            
        elif z_map[head[0]][head[1]] == 0: #사과가 아닌 그냥 이동일경우 꼬리 하나 줄여줌
            z_map[head[0]][head[1]] = 1
            z_map[tail[0]][tail[1]] = 0
            if z_map[tail[0]][tail[1]+1] == 1:
                tail[1] += 1
            elif z_map[tail[0]][tail[1]-1] == 1:
                tail[1] -= 1
            elif z_map[tail[0]+1][tail[1]] == 1:
                tail[0] += 1
            elif z_map[tail[0]-1][tail[1]] == 1:
                tail[0] -= 1
        
        else: #사과일 경우
            z_map[head[0]][head[1]] = 1

        clock += 1
       #for i in range(n+2):
       #    print(z_map[i]) 디버깅용
    c_c = c
            

#머 대충이렇게 시도는 해봄 근데 입력 예시 2부터 안댐 ㅋㅋㅋ
