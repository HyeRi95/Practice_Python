from itertools import combinations
def solution(number):
    answer = 0
    answer_list = list(combinations(number, 3))
    for i in answer_list : 
        if sum(i) == 0 :
            answer = answer+1
        else:
            pass
    return answer