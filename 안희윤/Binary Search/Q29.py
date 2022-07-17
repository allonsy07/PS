
N, C = map(int, input().split())

points = []
for _ in range(N):
  points.append(int(input()))

# 이진 탐색을 위한 sorting
points.sort()

# 공유기 위치 간 gap을 이용해 해결
# 첫번째 위치와 마지막 위치 사이의 gap이 최대일 것이다.
# 가장 작은 gap과 가장 큰 gap을 start와 end에 초기화
start = points[1] - points[0]
end = points[-1] - points[0]
result = 0

# 문제는 결국 인접한 두 공유기 사이의 거리의 최댓값이므로 최대로 가질 수 있는 gap인 sorting된 리스트에서
# 제일 첫번째 요소와 제일 마지막 요소 사이의 간격에서부터 반씩 줄여나가며 몇개의 공유기를 선택할 수 있는지를 확인한다.
while start < end:
  gap = (start+end)//2 # 인접한 두 공유기 사이의 gap
  point = points[0]
  count = 1
  for i in range(1,N):
    if points[i] >= (point+gap):
      point = points[i]
      count += 1
  if count >= C:
    start = gap + 1
    result = gap
  else:
    end = gap - 1

print(result)