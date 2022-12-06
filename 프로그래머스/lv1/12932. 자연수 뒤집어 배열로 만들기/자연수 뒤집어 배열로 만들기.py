def solution(n):
    a = str(n)
    answer = []
    for i in range(len(a)) :
        answer.append(int(a[i]))
    return answer[::-1]
# answer.reverse() 
# 사용가능 