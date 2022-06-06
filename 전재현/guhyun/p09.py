n = input()

min_length = len(n)
for i in range(int(len(n)/2)+1):
    strl = []
    count = 1
    temp = n[0:i+1]
    for j in range(1 + int(len(n)/(i+1))):
        if temp == n[(i+1)*(j+1):(i+1)*(j+2)]:
            count += 1
        else:
            if temp == '':
                break
            if count != 1:
                strl.append(str(count))
            strl.append(temp)
            temp = n[(i+1)*(j+1):(i+1)*(j+2)]
            count = 1

    print(strl)
    st = ''
    separtor = ''
    for idx, val in enumerate(strl):
        st += val + ('' if idx == len(strl) -1 else separtor)
    
    print(st, " ", len(st))

    if min_length > len(st):
        min_length = len(st)

print(min_length)

