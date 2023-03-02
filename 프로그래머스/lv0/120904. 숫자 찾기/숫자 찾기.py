def solution(num, k):
    num = list(str(num))
    for i in range(len(num)):
        if num[i] == str(k):
            answer = i+1
            return answer
        else : 
            answer = -1
    return answer
