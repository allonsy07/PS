N, X = map(int, input().split())

array = list(map(int, input().split()))

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

count = 0
while True:
    if binarySearch(X, array) != None:
        count += 1
        array.remove(X)
    else:
        break
if count == 0:
    count = -1
print(count)
    