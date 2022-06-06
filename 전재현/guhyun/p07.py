n = input()

leng = len(n)
pos = 0
bac = 0
for i in range(int(leng/2)):
    pos += int(n[i])
    bac += int(n[int(leng/2)+i])

if pos == bac:
    print("LUCKY")
else:
    print("READY")