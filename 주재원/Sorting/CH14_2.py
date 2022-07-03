N = int(input())
location = list(map(int, input().split()))
location.sort()
mean = (N-1) // 2

print(location[mean])
