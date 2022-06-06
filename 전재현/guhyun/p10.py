import json
import numpy as np

#key=np.array(json.loads(input()))
#lock=np.array(json.loads(input()))
key=np.array([[0,0,0],[1,0,0],[0,1,1]])
lock=np.array([[1,1,1],[1,1,0],[1,0,1]])

size_lock = lock.shape
size_key = key.shape

space_lock = np.ones((2*size_key[0]+size_lock[0]-2,2*size_key[0]+size_lock[0]-2))
space_lock[size_key[0]-1:size_key[0]+size_lock[0]-1, size_key[0]-1:size_key[0]+size_lock[0]-1] = lock
print(space_lock)

result = 1
for i in range(size_key[0]-1):
    for j in range(size_key[1]-1):
        for k in range(4):
            print(key)
            print(space_lock[i:i+size_key[0],j:j+size_key[1]])
            result = int((key*space_lock[i:i+size_key[0],j:j+size_key[1]]).sum())
            #tlqkf;
            if result == 0:
                print("True")
                break
            key = np.array(np.rot90(key,3))
        if result == 0:
            break
    if result == 0:
        break

if result != 0:
    print("False")