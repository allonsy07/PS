n = int(input())
data = list(map(int, input().split()))
result = 0
length = len(data)

data.sort(reverse=True)
i = 0
result = 0
while True:
  if data[i] <= length:
    length -= data[i]
    result += 1
    i += data[i]
  else:
    length -= 1
    i += 1
  if length <= 0:
    break

print(result)