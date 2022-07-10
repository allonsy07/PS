words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]

def solution(words, queries):
    answer = []
    
    for query in queries:
        len_query = len(query)
        l_que = query.find("?")
        r_que = query.rfind("?")
        if l_que == 0:
            leftslice = True
            query = query[r_que+1:]
        else:
            leftslice = False
            query = query[:l_que]
        
        
        temp_array = []
        for word in words:
            if len(word) == len_query:
                if leftslice:
                    temp_array.append(word[r_que+1:])
                else:
                    temp_array.append(word[:l_que])
        
        count = temp_array.count(query)
        answer.append(count)
    return answer

sol = solution(words, queries)
print(sol)