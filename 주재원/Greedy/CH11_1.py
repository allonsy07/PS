N = int(input())
X = list(map(int, input().split()))

X.sort()
group = 0
member = []

for x in X:
    member.append(x)
    if len(member) >= max(member):
        group += 1
        member = []
        
print(group)