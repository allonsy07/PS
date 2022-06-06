m = map(int, input())

value = 1
for token in m:
  if token:
    value *= token

print(value)