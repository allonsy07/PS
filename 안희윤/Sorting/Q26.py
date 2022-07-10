N = int(input())
nums = []
for _ in range(N):
    nums.append(int(input()))

compare_time = 0
while len(nums)!=1:
    nums.sort()
    hap = nums[0] + nums[1]
    compare_time += hap
    nums.append(hap)
    nums.remove(nums[0])
    nums.remove(nums[0])

print(compare_time)