def solution(s, start, repeats, score, count):
  result = score

  if start+repeats > len(s):
    # result += len(s[start:])
    print("End")
    return result

  # 문장의 길이만큼 반복
  if N[start:start+repeats] == N[start+repeats : start+2*repeats]:
    count += 1
    start = start+repeats
    print("Have repeat! repeats : ", repeats, "score : ", result, "Count : ", count)
    result = solution(s, start, repeats, result, count)

  else:
    if count > 1:
      count = 1
      result += repeats
    start = start + 1
    print("No repeat! repeats : ", repeats, "score : ", result)
    result += 1
    result = solution(s, start, repeats, result, count)

  return result


while (repeats <= half_len): # 전체 문장의 반절을 지나고 나서는 반복되는 문자열이 생길 수 없다
  score = solution(N, 0, repeats, 0, 1)
  print(score, repeats)
  if score < best_score:
    best_score = score
  repeats += 1

print(best_score)