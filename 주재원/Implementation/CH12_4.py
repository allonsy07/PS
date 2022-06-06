key = [[0,0,0], [1,0,0], [0,1,1]]
lock = [[1,1,1], [1,1,0], [1,0,1]]
cnt = 0

def turn(key):
    new_key = [[] for i in range(len(key))]
    for i in range(len(key)):
        for j in range(len(key[0])):
            new_key[i].append(key[len(key[0] - j)][i])
    
    return new_key

def make_base(key, lock): # key의 일부만 사용해서 lock을 풀 수도 있으니까 lock을 확장시켜줌 (zero padding 해주는 느낌)
    base = [[0 for i in range(len(key) + 2*(len(lock) - 1))] for j in range((len(key) + 2*(len(lock) - 1)))]

    for y in range(len(lock)):
        for x in range(len(lock)):
            base[y + len(key) - 1][x + len(key) - 1] = lock[y][x]

    return base

while cnt != 4:
    base = make_base(key, lock)
    for i in range(len(base) - len(key) + 1):
        for j in range(len(base) - len(key) + 1):
            
            for y in range(len(key)):
                for x in range(len(key)):
                    base[i+y][j+x] += key[y][x] # key랑 lock이랑 겹치는 부분을 합쳐서 값이 모두 1인 lock이 만들어지는걸 체크하도록 풀려고 했는데 일부만 겹칠 때를 어떻게 구현해야 할 지 모르겠음
            
            