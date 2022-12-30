def solution(s):
    answer =[]
    s = list(s)
    for i in s:
        answer.append(ord(i))
    answer.sort(reverse=True)
    answer = list(map(chr,answer))
    return ''.join(answer)