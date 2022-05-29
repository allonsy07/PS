def solution(food_times, k):
    
    current_food = 0

    hap = sum(food_times)
    if hap <= k:
        return -1
    
    for i in range(k):
        
        while food_times[current_food] == 0:
            current_food += 1
            if current_food == len(food_times): current_food = 0
            print(current_food)
            
        food_times[current_food] -= 1
            
        current_food += 1            
        if current_food == len(food_times): current_food = 0

    while food_times[current_food] == 0:
            current_food += 1
            if current_food == len(food_times): current_food = 0
            print(current_food)
            
    answer = current_food + 1
    return answer


#프로그래머스 사이트에서 작동해야함
#정확성 테스트는 모두 통과, 효율성 테스트에서 다 탈락
#답지에서는 우선순위 큐 사용