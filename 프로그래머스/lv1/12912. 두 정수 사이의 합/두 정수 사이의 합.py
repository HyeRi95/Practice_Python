# def solution(a,b):
#     answer=0
#     if a<b : 
#         answer = a*(b-a+1)+(b-a+1)
#     if a>b :
#         answer = -(a*(b-a-1)-(b-a-1))
#     if a==b :
#         answer = a
#     return answer

def solution(a,b):
    answer=0
    for i in range(abs(b-a)+1):
        answer = min(a,b)+i + answer
        
    return answer