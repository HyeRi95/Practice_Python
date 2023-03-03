# def solution(n):
#     for i in range (600):
#         if (6*(i+1))%n == 0:
#             return i+1 
#         else : 
#             pass
        
def solution(n):
    i=1
    while(1):
        if (6*i)%n==0:
            return i
        i+=1