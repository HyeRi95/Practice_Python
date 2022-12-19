# numpy 사용 
import numpy as np
def solution(numbers):
    answer = ((np.array(numbers))*2).tolist()
    return answer

# for 문 사용 
# def solution(numbers):
#     answer =[]
#     for i in numbers :
#         answer.append(i*2)
#     return answer

# 한줄로 for 함수 사용 
# def solution(numbers):
#     return [x*2 for x in numbers]
