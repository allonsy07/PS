S = input()
check = []

for i, s in enumerate(S):
    if i == 0:
        check.append(int(s))
    else:
        if s != S[i-1]:
            check.append(int(s))

ones = sum(check)
zeros = len(check) - ones

print(min(ones, zeros))