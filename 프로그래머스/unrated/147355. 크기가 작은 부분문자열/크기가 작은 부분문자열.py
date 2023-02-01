def solution(t, p):
    answer=[]
    answer_new = []
    for i in range(len(t)):
        if len(t[i:(len(p)+i)]) < len(p):
            pass
        else : 
            answer.append(int(t[i:(len(p)+i)]))
    for j in answer : 
        if j <= int(p) : 
            answer_new.append(j)
        else : 
            pass
    return len(answer_new)