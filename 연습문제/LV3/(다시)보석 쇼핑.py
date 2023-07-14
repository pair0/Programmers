### 시간 초과
#가장 짧은 구간의 시작 진열대 번호와 끝 진열대 번호를 차례대로 배열에 담아서 return 하도록 하며, 만약 가장 짧은 구간이 여러 개라면 시작 진열대 번호가 가장 작은 구간을 return 합니다.

def solution(gems):
    answer = []
    set_gems = set(gems)
    gems_N = len(set_gems)
    
    for i in range(gems_N, len(gems)+1):
        for j in range(len(gems)-gems_N+1):
            if len(set_gems - set(gems[j:j+i])) == 0:
                answer = [j+1, j+i]
                return answer
            

### 정답
#가장 짧은 구간의 시작 진열대 번호와 끝 진열대 번호를 차례대로 배열에 담아서 return 하도록 하며, 만약 가장 짧은 구간이 여러 개라면 시작 진열대 번호가 가장 작은 구간을 return 합니다.

def solution(gems):
    N = len(gems)
    answer = [0, N-1]
    kind = len(set(gems))
    dic = {gems[0]:1}
    start, end = 0, 0
    
    while start < N and end < N: 
        if len(dic) < kind: ### 종류 부족하면 end point 증가 & dic 개숫 증가
            end += 1
            if end == N:
                break
            dic[gems[end]] = dic.get(gems[end], 0) + 1
            
        else: ### 종류 같으면 ans 비교 후 답 갱신하고, start point 증가 & dic 개수 다운
            if (end-start+1) < (answer[1]-answer[0]+1):
                answer = [start,end]
            if dic[gems[start]] == 1:
                del dic[gems[start]]
            else:
                dic[gems[start]] -= 1
            start += 1
        print(dic)
        print(start, end)

    answer[0] += 1
    answer[1] += 1
    return answer
        