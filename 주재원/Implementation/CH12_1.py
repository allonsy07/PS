N = str(input())
half = int(len(N) / 2)
left = 0
right = 0
for i in range(0, half):
    left += int(N[i])
    right += int(N[i+half])

if left == right:
    print('LUCKY')
else:
    print('READY')