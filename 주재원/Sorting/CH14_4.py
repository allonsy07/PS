N = int(input())
card = []

for i in range(N):
    patch = int(input())
    card.append(patch)
output = 0    

while len(card) > 1:
    card.sort()
    min_1 = card.pop(0)
    min_2 = card.pop(0)

    sum_min = min_1 + min_2
    output += sum_min
    card.append(sum_min)

print(output)