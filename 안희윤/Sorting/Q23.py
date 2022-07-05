N = int(input())

score = []
for i in range(N):
    name, g, e, m = input().split()
    score.append([name, g, e, m])

# key 값으로 하나씩 국어, 영어, 수학, 이름순으로 정렬하도록
score.sort(key = lambda x: (-int(x[1]), int(x[2]),-int(x[3]), x[0]))

for name,_,_,_ in score:
    print(name)
