# 31
T = int(input())  # 시행수
# 시행수만큼 n, m과 그 안에 들어갈 숫자 입력
for _ in range(T):
    n, m = map(int, input().split())
    nums = list(map(int, input().split()))

    golds = []
    idx = 0
    # golds에 nxm 형태로 nums를 매핑시켜줌
    for i in range(n):
        golds.append(nums[idx:idx + m])
        idx += m

    # 오른쪽 요소가 왼쪽 요소 3개중 큰 수를 더해가면서
    # 업데이트 되는 형태이므로 2번쨰 열부터 3개 중 큰 수를 더해가면서 업데이트
    left_top = 0
    left_middle = 0
    left_bottom = 0
    for j in range(1, m):
        for i in range(n):
            # 첫번쨰 행에 존재할때는 top이 존재하지 않고, 마지막 행에 있을때는 bottom이 존재하지 않도록 조건문
            if i > 0:
                left_top = golds[i - 1][j - 1]
            left_middle = golds[i][j - 1]
            if i < n - 1:
                left_bottom = golds[i + 1][j - 1]
            golds[i][j] += max(left_top, left_middle, left_bottom)

    max_val = 0

    for i in range(n):
        if golds[i][m - 1] > max_val:
            max_val = golds[i][m - 1]

    print(max_val)
