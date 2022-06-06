S = input()
S = [s for s in S]
S.sort()
numbers = [str(i) for i in range(10)]
alp = ''
num = 0
for i, s in enumerate(S):
    if s in numbers:
        num += int(s)
    else:
        alp += s

print(alp + str(num))
