def solution(array, commands):
    answer=[]
    for i in commands : 
        pre_answer=[]
        pre_answer = array[(i[0]-1):i[1]]
        pre_answer.sort()
        print(pre_answer)
        answer.append(pre_answer[(i[2]-1)])
    return answer