n = input()

a = int(n[0])

for i in range(1,len(n)):
    b = int(n[i])
    hap = a + b
    gop = a * b
    a = hap if hap>=gop else gop

print(a)