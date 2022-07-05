# 집의수, 집의 위치
N = int(input())
house_point = list(map(int, input().split()))

distance = 0
# 최소거리를 초기화 한 이후
min_distance = float("inf")
# 각 포인트와 다른 포인트들 사이의 거리를 절대값으로 더해가면서 가장 작은 거리를 업데이트해가며 그
# 위치를 반환한다
for point1 in house_point:
    for point2 in house_point:
        distance += abs(point1-point2)
    if min_distance > distance:
        min_distance = distance
        best_point = point1

print(best_point)

