def solution(n):
    a = 1
    b = 1
    for i in range(11):
        b = i+1
        a = a*b
        if a > n : 
            return i
    # answer = 0
    # return answer