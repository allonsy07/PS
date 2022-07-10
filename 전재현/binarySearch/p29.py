N, X = map(int, input().split())

array = []
for i in range(N):
    array.append(int(input()))
array.sort()

distance = []
temp = array[0]
for a in array[1:]:
    distance.append(a - temp)
    temp = a

wifi = []
def binarySearch(target, array):
    start = 0
    end = len(array)-1
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid -1
        else:
            start = mid + 1
    return None