N = int(input())

array = list(map(int, input().split()))
array.sort()

b = []
mean_array = sum(array)/len(array)

for i in array:
    tmp = abs(i-mean_array)
    b.append(tmp)

    b.sort()
    search_val = b[0]
    
for i in array:
    tmp = abs(i-mean_array)
    if tmp == search_val:
        print(i)

