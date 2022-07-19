# 32
n = int(input())
triangle = []
# 위 문제와 유사
for _ in range(n):
    triangle.append(list(map(int, input().split())))

# 첫번째 요소와 마지막 요소일때만 위 행에 있는 요소만 선택 가능하다
# 첫번째 요소일때 : 윗열 첫번째 요소/ 마지막 요소: 윗열 마지막 요소
for h in range(1, n):
    for idx in range(h + 1):
        if idx == 0:
            triangle[h][idx] += triangle[h - 1][0]
        elif idx == h:
            triangle[h][idx] += triangle[h - 1][idx - 1]
        else:
            triangle[h][idx] += max(triangle[h - 1][idx - 1], triangle[h - 1][idx])

print(max(triangle[n - 1]))