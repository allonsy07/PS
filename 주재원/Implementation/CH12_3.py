s = input()
term = 1
lengths = []

def check(s, term):
    new_s = ''
    cnt = 1
    for num, i in enumerate(range(0, len(s), term)):
        if i == 0:
            prev = s[i:i+term]
        else:
            now = s[i:i+term]
            
            if prev == now :
                cnt += 1

            else:
                if cnt == 1:
                    new_s += prev
                else:
                    new_s += str(cnt) + prev
                    cnt = 1
            prev = now

        if num == int((len(s) - 1) / term): # 마지막인데 prev == new인 경우를 고려해줌
            if cnt == 1:
                new_s += now
            else:
                new_s += str(cnt) + now                    
    
    return len(new_s)

while term != int(len(s)/2 + 1):
    length = check(s, term)
    lengths.append(length)
    term += 1    
    
if len(s) == 1:
    lengths = [1]

print(min(lengths))