m = list(map(int, input()))
count = 0

one_token = 0
zero_token = 0
temp = m[0]
if temp == 0:
  zero_token += 1
else:
  one_token += 1 
  
for i in m:
  if i != temp:
    if i == 0:
      zero_token += 1
    else:
      one_token += 1 
  temp = i

count = min(one_token, zero_token)
print(count)
  