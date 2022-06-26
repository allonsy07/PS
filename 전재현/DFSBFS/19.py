from collections import deque
import queue

N = map(int, input())
A = list(map(int, input().split()))
addd, sub, mul, dibv = map(int, input().split())

def dfs(x):
    queue = deque()
    for a in x:
        queue.append(a)
    


#a1 a2 ... an개의 수가 있을 때, 수의 순서는 바꿀 수 없다. 
#최대가 되려면 X,+는 큰수끼리, /,-는 작은수가 오른쪽에 와야된다. 순서는 /,+ 다음 X,-
#최소가 되려면 X,+는 작은수끼리, /,-는 큰수가 오른쪽에 와야된다. 순서는 -,X 다음 +,/