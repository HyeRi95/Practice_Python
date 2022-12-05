def solution(n):
    answer =[]
    a = str(n)
    for i in range(len(a)):
        answer.append(int(a[i])) 
    return sum(answer)