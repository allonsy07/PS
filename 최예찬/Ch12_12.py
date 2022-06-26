def solution(n, build_frame):
    b_map = [[0]*(n+1) for i in range(n+1)] #건축물 맵, 0= 아무것도 없는거 1 = 기둥, 2 = 보

    for x, y, a, b in build_frame:
        
        if b == 1: #설치할 경우
            if a == 0: #기둥인 경우
                print(x,y)
                if y == 0: #바닥에 설치
                    b_map[y][x] = 1
                    
                elif b_map[y][x] >= 2: #보 위에 설치
                    b_map[y][x] += 1
                
                elif b_map[y-1][x] % 2 == 1: #기둥 위에 기둥 설치
                        b_map[y][x] += 1
                        print('hi')
                    
                if x > 0:
                    if b_map[y][x-1] >= 2: #보 위에 기둥설치
                        b_map[y][x] += 1
    
                    
            elif a == 1: #보인 경우
                
                if b_map[y-1][x] % 2 == 1: #왼쪽에 기둥이 설치 된경우
                    b_map[y][x] += 2
                    
                elif x < n: 
                    if b_map[y-1][x+1] % 2 == 1: #오른쪽에 기둥이 설치된 경우
                        b_map[y][x] += 2
                        
                    elif b_map[y][x-1] > 1 and b_map[y][x+1] > 1: #양 옆에 보가 있는 경우
                        b_map[y][x] += 2
        
                
        elif b == 0: # 삭제할 경우
            
            b_map[y][x] -= a +1 
            #이건 구현 못해먹겠네 ㅅㅂㅋㅋ
            
    answer = []
    for i in range(n+1):
        for j in range(n+1):
            if b_map[j][i] > 0:
                if b_map[j][i]%2 == 1:
                    answer.append([i,j,0])
                if b_map[j][i] > 1:
                    answer.append([i,j,1])
                    
    return answer

    #설치는 구현 다햇는데 삭제하는건 구현 못해먹겠다 ㅅㅂ!
    