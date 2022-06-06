def solution(s):
    l = len(s)
    min_l = l
    for i in range(1,l//2+1): #slicing 하는 길이, 길이 1 문자열 중복 체크, 길이 2 문자열 중복 체크 
        
        comp = s[0:i] #문자열 비교를 위한 로컬 변수
        tmp_l = i #최종 압축 문자열의 길이
        cnt_l = 1 #문자열 중복 갯수 체크
    
        for j in range(1,l//i): # s 처음부터 끝까지 돌면서 중복 체크
            
            tmp = s[j*i : (j+1)*i] #slicing 하는 길이로 나눈 중복 체크할 문자열
            
            if comp == tmp: #중복체크할 문자열이 이전의 문자열과 동일할 경우
                
                if cnt_l == 1: #동일한 문자열이 처음일 경우
                    tmp_l += 1 #중복하는 숫자 한글자 추가
                    cnt_l += 1 #중복하는 문자열 갯수 추가

                else: #이전에 동일한 문자열이 2개 이상일 경우
                    cnt_l += 1 #중복하는 문자열 갯수 추가
                    if cnt_l == 10 or cnt_l == 100 or cnt_l == 1000:
                        tmp_l += 1 #숫자 자릿수 늘어나면 1씩 길이 추가
                
            else: #문자열이 이전의 문자열과 다를 경우
                cnt_l = 1 #중복하는 문자열 갯수 초기화
                tmp_l += i #문자열 길이만큼 글자수 추가
                comp = tmp #비교 문자열 업데이트
        
        tmp_l += l%i #문자열 길이 나누고 남은 나머지 만큼 글자수 추가
        
        if tmp_l < min_l:
            min_l = tmp_l
        
    answer = min_l
    return answer