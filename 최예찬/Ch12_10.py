def rotation(key): #오른쪽으로 90도 회전
    m = len(key)
    ret_key = [[0]*m for i in range(m)]
    print(ret_key)
    for i in range(m):
        for j in range(m):
            ret_key[i][j] = key[-(j+1)][i]
            
    return ret_key

def move_up(key):
    key[:-1] = key[1:]
    key[-1] = [0]*len(key)
    return key

def move_down(key):
    key[1:] = key[:-1]
    key[0] = [0]*len(key)
    return key

def move_left(key):
    for i in range(len(key)):
        key[i][1:] = key[i][:-1]
        key[i][0] = 0
    return key

def move_right(key):
    for i in range(len(key)):
        key[i][:-1] = key[i][1:]
        key[i][-1] = 0
    return key
    

def solution(key, lock):
    min_x = min_y = 20
    max_x = max_y = 0
    
    lock_l = len(lock)
    
    for i in range(lock_l):
        for j in range(lock_l):
            if lock[i][j] == 0:
                if min_x > i:
                    min_x = i
                if max_x < i:
                    max_x = i
                if min_y > j:
                    min_y = j
                if max_y < j:
                    max_y = j
    
    home = list()
    for i in range(max_x - min_x + 1):
        home.append(lock[min_x + i][min_y:max_y+1]) #lock에서 홈만 있는 부분만 추출?
        
    #구현방법: key를 home 사이즈에 맞게 상하와주 로테이션 시키는 경우의 수를 다 구현해서 홈과 딱 맞는 부분이 있으면 True 리턴, 4번의 로테이션 후 없으면 False?
    #근데 못해먹겠음 ㅋㅋ
    
    print(home)
                    
    