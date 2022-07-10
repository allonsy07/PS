# stage 개수, 해당 스테이지를 깨고있는 사람들이 있는 단계를 입력받은뒤 오름차순으로 sort
N = int(input())
people = list(map(int, input().split()))

# stage 개수와 같은 길이의 리스트 생성
num_in_stage = [0]*N
# 몇번째 스테이지에 사람들이 멈춰있는지를 한개 더 작은 인덱스의 위치에 개수를 저장하는 방식(딕셔너리)와 유사하게
# 저장한다. 예를 들면, (1번째 스테이지에 있는 사람수 : num_in_stage 리스트 0번째 인덱스에 입력)
for stage in people:
    if stage <= len(num_in_stage):
        num_in_stage[stage-1] += 1

# 위에서 구한 값을 이용하여 실패율을 계산한다
faliure_rate = []
# 분모를 위해 전체 사람 수를 초기화
len = len(people)
# faliure rate에 [stage, 실패율] 형태로 입력해나간다.
for i in range(0, N):
  faliure_rate.append([i+1, (num_in_stage[i]/len)])
  len -= num_in_stage[i]
faliure_rate.sort(key=lambda x:-x[1])

for stage, rate in faliure_rate:
  print(stage, end = " ")