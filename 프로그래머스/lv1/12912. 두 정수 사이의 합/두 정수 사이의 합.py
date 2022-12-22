# def solution(a,b):
#     answer=0
#     for i in range(abs(b-a)+1):
#         answer = min(a,b)+i + answer
        
#     return answer

def solution(a, b):
    return (abs(a-b)+1)*(a+b)//2