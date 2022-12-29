def solution(left,right):
    
    answer = []
    for i in range(right-left+1):
        a = []
        for j in range(left+i):
            if (left+i)%(j+1) == 0 : 
                a.append(1)
            else :
                pass
        if len(a)%2 == 0:
            answer.append(left+i)
        else : 
            answer.append(-(left+i))
    return sum(answer)