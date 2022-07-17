T = int(input())

N = []
M = []
array = []
for i in range(T):
    '''
    N[i], M[i] = map(int, input().split())
    temp = list(map(int, input().split()))'''
    
    N.append(3)
    M.append(4)
    array.append([])
    temp = [1,3,3,2,2,1,4,1,0,6,4,7]
    for j in range(N[i]):
        array[i].append(temp[j*M[i]:(j+1)*M[i]])


for i in range(T):
    d = [0]*(M[i]+1)
    count = 0
    
    for j in range(M[i]):
        d[j] = max(array[i][:][j])




