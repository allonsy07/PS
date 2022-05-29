def solution(food_times, k):
    if len(food_times) > k:
        return k+1
    if sum(food_times) <= k:
        return -1
    
    else:
        while k > 0:
            for i in range(len(food_times)):
                if food_times[i] == 0:
                    continue
                food_times[i] -= 1
                k -= 1
                answer = i + 1 # 다음에 먹어야 할 food의 index
                if k == 0:
                    break          

        for a in range(answer, len(food_times)): # answer부터 len(food_times)-1까지
            if food_times[a] > 0:
                return a + 1

        for a in range(answer):
            if food_times[a] > 0:
                return a + 1
        
        return -1