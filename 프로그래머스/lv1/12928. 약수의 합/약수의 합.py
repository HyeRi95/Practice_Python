def solution(n):
    div =[]
    answer = 0 
    for i in range (n) : 
        if n%(i+1) == 0 :
            div.append(i+1)
        else :
            pass
    for j in div :
        answer = j+answer
    return answer