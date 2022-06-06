#이거는 못해먹겠어서 답지 한번 훑고 구현해봄

from itertools import combinations

n,m = map(int,input().split())
house = []
chicken = []

for i in range(n):
    data = list(map(int,input().split()))
    for j in range(n):
        if data[j] == 1:
            house.append((i,j)) #집들의 위치 좌표로 표현
        elif data[j] ==2:
            chicken.append((i,j)) #집들의 위치 좌표로 표현

candidates = list(combinations(chicken,m)) #치킨 집들을 m개만 남기는 모든 경우의 수(조합)

def sum(candidate): #도시의 치킨 거리 구하는 함수
    sum = 0
    for hx, hy in house:
        tmp = 100
        for cx,cy in candidate:
            tmp = min(tmp,abs(cx-hx)+abs(cy-hy)) #한 가정에서 가장 가까운 치킨집 까지와의 치킨거리
        
        sum += tmp #가정들의 치킨 거리 합
    return sum

answer = 100*13

for candidate in candidates:
    answer = min(answer, sum(candidate)) #최소 치킨 거리 계산

print(answer)