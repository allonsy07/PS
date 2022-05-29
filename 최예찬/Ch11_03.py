s = input()

cnt = 0

for i in range(1,len(s)):
    if s[i-1] == '0' and s[i] == '1' :
        cnt +=1



if s[0] == '1' and s[-1] == '0':
     print(cnt+1)

else:
     print(cnt)


