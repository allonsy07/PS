import json
import numpy as np
from pyparsing import col
from sympy import ground_roots

n = int(input())
frames = np.array(json.loads(input()))

global grounds
grounds = np.zeros((n,n,2))
grounds[:,0,2] = -1

def check_state_build(x, y, cr):
    global ground
    if not cr: # 기둥이면 참 보면 거짓
        if grounds[x,y,1] == 0:
            if ground[x-1,y,2] + ground[x,y,2] + ground[x,y-1,1] + y==0:
                return 1
            return 0
        return 0 
    else:
        if grounds[x,y,2] == 0:
            if ground[x-1,y,2] + ground[x+1,y,2] + ground[x,y-1,1]:
                return 1
            return 0
        return 0


def check_state_delect(x, y, cr):
    global ground
    if not cr: # 기둥이면 참 보면 거짓
        if grounds[x,y,1] == 1:
            if ((ground[x,y+1,2] == 0) + (ground[x+1,y,1] == 1 
            or ground[x+1,y+1,2] == 1)) and ((ground[x-1,y+1,2] == 0) + (ground[x-1,y,1] == 1 
            or ground[x-2,y+1,2] == 1)) and (ground[x,y+1,1] == 0):
                return 1
            return 0
        return 0 
    else:
        if grounds[x,y,2] == 1:
            if ground[x-1,y,2] + ground[x+1,y,2] + ground[x,y-1,1]:
                return 1
            return 0
        return 0
#대가리 퍼펑!
for frame in frames:
    x, y, cr, bd = frame
    if bd:
        if not cr:
            grounds[x,y,1] = 1
        else:
            grounds[x,y,0] = 1
    else:
        if not cr:
            grounds[x,y,1] = 0
        else:
            grounds[x,y,0] = 0

print("")