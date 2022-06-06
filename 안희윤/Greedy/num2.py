S = input()
result = 0

for num in S:
  num = int(num)
  if result == 0:
    result += num
    continue
  if num == 0 or num == 1:
    result += num
  else:
    result *= num

print(result)