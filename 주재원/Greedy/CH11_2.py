S = input()
base = 0

for s in S :
    if s == '0' or base == 0:
        base += int(s)
    else:
        base *= int(s)
        
print(base)
