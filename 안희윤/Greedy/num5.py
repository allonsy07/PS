from collections import Counter
n, m = map(int, input().split())

data = list(map(int, input().split()))
each_pin = Counter(data)
result = n*(n-1)/2
for pin_num in each_pin:
    nums = each_pin[pin_num]
    result -= nums*(nums-1)/2

print(int(result))