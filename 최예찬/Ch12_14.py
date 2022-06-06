#이것도 답지 좀 참고하면서 직접 구현

from itertools import permutations

def solution(n, weak, dist):

    length = len(weak)
    for i in range(len(weak)): #길이 2배로 만들어 원형을 1차원 배열로 바꿈
        weak.append(weak[i]+n)

    
    
    
    for i in range(1,len(dist)+1): #투입하는 친구의 수 i
        for candidate in list(permutations(dist,i)): #친구 i명 순열
            for j in range(length): #취약점 탐색 시작지점

                tmp = 0
                idx = index = j

                while tmp < i: #총 i명만큼 순차적으로 투입

                    while weak[index] <= weak[idx] + candidate[tmp]: #탐색시작점에 친구 1명 투입
                        index += 1 #그 친구의 탐색 마지막 지점까지 index 증가, index는 이제 탐색해야 할 지점

                    if (index - j + 1) > length:
                        return i

                    else:
                        tmp += 1
                    idx = index

            
    return -1