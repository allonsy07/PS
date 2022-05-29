n = int(input())
data = list(map(int, input().split()))

data.sort(reverse=True) #내림차순 정렬

groups = 0 #그룹 갯수

while(1):

    end = data[-1] #가장 작은 instance

    if end <= len(data):

        if end == data[-end]: #같은 값의 instance가 그 값 보다 많이 반복되는 경우
            for i in range(end):
                data.pop() #그 값만큼 갯수의 instance를 list에서 빼줌
            groups += 1 #그룹하나 생성

        else: #5 5 4 4 4 경우 5 5 5 5 5로 바꿔 버림 
            data[-end:] =  [ data[-end] ] * end

    else:
        break


print(groups)