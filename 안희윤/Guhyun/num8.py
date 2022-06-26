N = list(input())

nums = [str(i) for i in range(0,10)]
number = 0
sentence = ""
for a in N:
  if a in nums:
    number += int(a)
  else:
    sentence = sentence + a


arranged = "".join(sorted(sentence)) + str(number)
print(arranged)