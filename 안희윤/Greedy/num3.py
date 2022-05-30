result = 0

S = input()
result = 0
memory = S[0]

for num in S[1:]:
  if num == memory:
    memory = num
    continue
  if num != memory:
    result += 1
    memory = num

result = (result//2) + (result%2)
print(result)