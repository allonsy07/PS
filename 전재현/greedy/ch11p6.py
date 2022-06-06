def NumberOfFood(food_times, K):
  kind_food = len([x for x in food_times if x>0])
  while (K >= kind_food):
    for i in range(len(food_times)):
      if food_times[i] > 0:
        food_times[i] -= 1

    K -= kind_food
    kind_food = len([x for x in food_times if x>0])
    print(kind_food)

  index = 0    
  for i in range(len(food_times)):
    if K == -1:
      break
    if food_times[i] > 0:
      food_times[i] -= 1
      K -= 1
    index += 1

  return index


food_times = [3,1,1,6]
k = 5
result = NumberOfFood(food_times, k)
print(result)