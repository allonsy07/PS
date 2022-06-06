input = input()

l = len(input) // 2 #input 길이 반으로 나눔

r_cnt = l_cnt = 0

for i in range(l):
    r_cnt += int(input[i]) #오른쪽 자리수 합
    l_cnt += int(input[-(i+1)]) #왼쪽 자리수 합

if r_cnt == l_cnt:
    print("LUCKY")
else:
    print("READY")