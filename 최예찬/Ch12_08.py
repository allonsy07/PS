
input = input()

cnt = 0
s_list = list()

for k in input:
    if k >= '0' and k <= '9':
        cnt += int(k) #숫자면 합
    else:
        s_list.append(k) #문자면 따로 저장

s_list.sort() #정렬

print("".join(s_list)+str(cnt))
