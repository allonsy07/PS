N = int(input())

nums = list(map(int, input().split()))

start = 0
end = N-1
result = -1
while True:
    mid = (start + end)//2
    if nums[mid] == mid:
        result = mid
        break
    if nums[mid] < mid:
        start = mid+1
        continue
    elif nums[mid] > mid:
        end = mid-1
        continue
    if start > end:
        break

print(result)