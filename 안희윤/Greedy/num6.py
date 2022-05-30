def solution(food_times, k):
    answer = 0
    len_food = len(food_times)
    while True:
        for i in range(len_food):
            if k == 0:
                print("k = -1", food_times, k)
                if food_times[i]!=0:
                    answer = i + 1
                    return answer
            if food_times[i] != 0:
                print(food_times[i], k)
                food_times[i] -= 1
                k -= 1
    return answer

food_times = list(map(int, input().split()))
k = int(input())
print("answer", solution(food_times, k))