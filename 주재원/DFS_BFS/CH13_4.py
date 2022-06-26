def solution(p):
    def right(p):
        cnt = 0
        for i in p:
            if i == '(':
                cnt += 1
            else:
                cnt -= 1                
                if cnt == -1:
                    return False
        return True

    if len(p) == 0:
        return p

    if right(p):
        return p

    open=0
    close=0

    for i, w in enumerate(p):
        if w == '(':
            open+=1
        else:
            close+=1
        if open == close:
            u = p[:i+1]
            v = p[i+1:]
            break
    if right(u):
        answer = u + solution(v)

    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        u = list(u[1:-1])
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('

        answer += ''.join(u)

    return answer

# print(solution('(()())()'))
# print(solution(')('))
# print(solution('()))((()'))
print(solution(')()()((())'))