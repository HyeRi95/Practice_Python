# def solution(array, height):
#     answer=[]
#     for i in array :
#         if i > height :
#             answer.append(i)
#     return len(answer)

def solution(array, height):
    answer = 0
    for i in array :
        if i > height:
            answer +=1
    return answer