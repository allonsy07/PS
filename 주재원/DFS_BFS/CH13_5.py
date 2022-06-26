N = int(input())
A = list(map(int, input().split()))
operator = list(map(int, input().split()))

def dfs(i, now, operator):
    global minimum, maximum 
    if i == N:
        minimum = min(minimum, now)
        maximum = max(maximum, now)
    else:
        if operator[0] != 0:
            operator[0] -= 1
            dfs(i+1, now+A[i], operator)
        if operator[1] != 0:
            operator[1] -= 1
            dfs(i+1, now-A[i], operator)
        if operator[2] != 0:
            operator[2] -= 1
            dfs(i+1, now*A[i], operator)
        if operator[3] != 0:
            operator[3] -= 1
            dfs(i+1, int(now/A[i]), operator)

minimum = -1e9
maximum = 1e9

dfs(1, A[0], operator)

print(minimum)
print(maximum)