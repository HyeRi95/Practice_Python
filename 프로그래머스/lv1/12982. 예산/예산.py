def solution(d, budget):
    sum = 0
    answer = 0
    d.sort()
    for i in d :
        sum = i+sum
        answer = answer + 1
        if sum > budget:
            answer = answer - 1
            break
        else :
            pass
    return answer