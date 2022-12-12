def solution(n):
    answer =0
    for i in range(n):
        j = i+1
        if n%j == 1 : 
            answer = j
            break
    return answer