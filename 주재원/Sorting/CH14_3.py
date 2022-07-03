def solution(N, stages):
    import numpy as np
    np_stage = np.array(stages)
    answer = []
    user = len(stages)

    for i in range(N):
        number = sum(np_stage == (i+1))

        if user == 0:
            fail = 0
        else:
            fail = number / user

        answer.append((i+1, fail))
        user -= number
    
    answer = sorted(answer, key = lambda x: x[1])
    answer = answer[::-1]
    answer = [i[0] for i in answer]
    
    return answer