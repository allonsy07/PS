import numpy as np

n = int(input())
k = int(input())

pos = [1,1]
tail = [1,1]
tail_temp = []
time = 0

direct = [[-1,0], [0,1], [1,0], [0,-1]]
now_direct = 1

board = np.zeros((n,n))
board = np.pad(board, ((1,1),(1,1)),'constant', constant_values=2) #벽
for i in range(k):
    emb = list(map(int, input().split()))
    board[emb[0], emb[1]] = 1

l = int(input())
move_list = []
for i in range(l):
    move_list.append(list(map(str ,input().split())))

for step, dir_ch in move_list:
    st = int(step)
    for i in range(st):
        pos[0] += direct[now_direct][0]
        pos[1] += direct[now_direct][1]
        tail_temp.append(pos)

        if board[pos[0], pos[1]] == 2:
            break
        else:
            time += 1
            board[pos[0], pos[1]] = 2
            if board[pos[0], pos[1]] != 1:
                board[tail[0], tail[1]] = 0
                tail = tail_temp.pop()

    if board[pos[0], pos[1]] == 2:
        break

    if dir_ch == "L":
        now_direct -= 1
        if now_direct < 0:
            now_direct += 4
    elif dir_ch == "D":
        now_direct += 1
        if now_direct > 4:
            now_direct -= 4
            
print(time)

