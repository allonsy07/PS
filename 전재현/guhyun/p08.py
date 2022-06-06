n = input()

ack = []
ch = []
for i in range(len(n)):
    ack.append(int(ord(n[i])))
ack.sort()

num = 0
for i in range(len(ack)):
    if ack[i] >= 48 and ack[i] < 58:
        num += int(chr(ack[i]))
    else:
        ch.append(chr(ack[i]))
ch.append(num)

print("".join([str(_) for _ in ch]))