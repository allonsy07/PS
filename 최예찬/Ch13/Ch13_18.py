def check(u):
    chk = 0
    for a in u:
        if a == '(':
            chk += 1
        elif a == ')':
            chk -= 1
        
        if chk == -1:
            return -1
    return 0

def solution(p):
    if p == ' ':
        return p
    
    if check(p) == 0:
        return p
        
    p = list(p)
    u = []
    chk = 0
    for i,a in enumerate(p):
        if a == '(':
            chk += 1
        elif a == ')':
            chk -= 1
        u.append(a)
        
        if chk == 0:
            del p[:i+1]
            break
    
    if check(u) == 0:
        s = ''
        for a in p:
            s += a
        solution(s)
        
    else: 
        s = ''
        for a in p:
            s += a
        n = '(' + solution(s) + ')'
        del u[0]
        del u[-1]
        for a in u:
            if a == '(':
                n.join(')')
            elif a == ')':
                n.join('(')
        return n

        #여기 까지 했는데 못해먹겠어서 때려침