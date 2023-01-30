def solution(a, b, n):
    answer = 0 
    for i in range(n) :
        answer = answer + (n//a)*b 
        n = (n//a)*b+n%a
        if n//a == 0 :
            break
    return answer