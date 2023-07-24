def solution(n):
    answer = 0
    n_list = [0] * (n+1)
    
    for i in range(1, n+1):
        n_list[i] = n_list[i-1] + i
        
        if n_list[i] == n:
            answer = +1
        elif n_list[i] > n:
            for j in range(i-1, -1, -1):
                n_result = n_list[i] - n_list[j]
                if n_result == n:
                    answer += 1
                elif n_result > n:
                    break
      
                
    return answer