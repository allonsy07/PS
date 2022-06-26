from collections import deque

BALANCED = 10
CORRECT = 20

string = input()

def correct_string(string):
    if len(string) == 0: #빈 문자열이면 빈 문자열 반환
        return ""
    u = ""
    queue = deque()
    if string[0] == "(": #처음이 (이냐 )이냐에 따라 queue 작동이 변경 개수맞춰서 u 자르기
        for i in string:
            if i == "(":
                queue.append(i)
                u += i
            elif i == ")":
                queue.pop()
                u += i
                if not queue:
                    break
    elif string[0] == ")":
        for i in string:
            if i == ")":
                queue.append(i)
                u += i
            elif i == "(":
                queue.pop()
                u += i
                if not queue:
                    break
    v = string[len(u):] #string에서 u부분 제외

    if check_COR(u) == CORRECT:
        recu = correct_string(v) 
        output = u + recu

    elif check_COR(u) == BALANCED:
        recu = correct_string(v)
        output = "(" + recu + ")" + change_u(u)
    
    return output


def check_COR(string):
    queue = deque()
    for i in string:
        if i == "(":
            queue.append(i)
        elif i == ")":
            if not queue:
                return BALANCED
            queue.pop()

    return CORRECT

def change_u(string):
    output = ""
    for i in string[1:-1]:
        if i == "(":
            output += ")"
        elif i == ")":
            output += "("
    return output

out = correct_string(string)
print(out)