N, x = map(int, input().split())

nums = list(map(int, input().split()))

start = 0
end = N-1
start_idx = -1
while True:
    mid = (start + end)//2
    if nums[mid] == x and nums[mid-1] != x:
        start_idx = mid
        break
    if nums[mid] < x:
        start = mid+1
        continue
    elif nums[mid] > x or (nums[mid]==x and nums[mid-1] == x):
        end = mid-1
        continue
    if start > end:
        break

length = 0

while nums[start_idx] == x:
    if start_idx == -1:
        length = -1
        break
    length += 1
    if start_idx >= N-1:
        break
    start_idx += 1

print(length)