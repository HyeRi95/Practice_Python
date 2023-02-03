# def solution(s1, s2):
#     answer = 0 
#     for i in s2 : 
#         if i in s1 :
#             answer = answer +1
#         else : 
#             pass
#     return answer

def solution(s1,s2) : 
    return len(set(s1)&set(s2));

# set() : 집합 연산 
# 중복을 허용하지 않는다.
# 순서가 없다(Unordered).
# s1 & s2 : 교집합
# s1 | s2 : 합집합
# s1 - s2 : 차집합