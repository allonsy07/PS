N = int(input())
array = list(map(int, input().split()))

def binarySearch(array):
    start = 0
    end = len(array)-1
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == mid:
            return mid
        elif array[mid] > mid:
            end = mid -1
        else:
            start = mid + 1
    return None

fixpoint = binarySearch(array)
if fixpoint == None:
    fixpoint = -1
print(fixpoint)