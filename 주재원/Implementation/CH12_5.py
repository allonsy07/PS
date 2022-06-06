N = int(input())
K = int(input())
apple = [map(int, input().split()) for i in range(K)]
L = int(input())
changes = [input().split() for i in range(L)]
body = [[0,0]]
t = 0
idx = 0
while True:
    t += 1    
    
    if idx == 0:
        for i in range(len(body)):
            body[i] = [body[i][0], body[i][1] + 1]
        head = body.pop(-1)
    elif idx == 1:
        for i in range(len(body)):
            body[i] = [body[i][0] + 1, body[i][1]]
        head = body.pop(-1)       
    elif idx == 2:
        for i in range(len(body)):
            body[i] = [body[i][0], body[i][1] - 1]
        head = body.pop(-1)        
    elif idx == 3:                
        for i in range(len(body)):
            body[i] = [body[i][0] - 1, body[i][1]]
        head = body.pop(-1)        

    if head not in apple:
        if len(body) > 0:
            body.pop(0)
    else:
        apple.remove(head)

    if head in body:
        print(t)
        break   

    if head[0] in [N, -1] or head[1] in [N, -1]:
        print(t)
        break  

    body.append(head)  

    for i in range(L):
        if str(t) in changes[i]:
            chr = changes[i][1]

            if chr == 'D':
                idx += 1
                if idx == 4:
                    idx = 0
            else:
                idx -= 1
                if idx == -1:
                    idx = 3    