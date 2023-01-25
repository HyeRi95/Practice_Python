def solution(strings, n):
    answer = []
    answer_new = []
    for i in range(len(strings)):
        answer.append(strings[i][n] + strings[i])
    answer.sort()
    for i in range(len(answer)) : 
        answer_new.append(answer[i][1:])
    return answer_new