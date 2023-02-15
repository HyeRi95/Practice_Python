def solution(n, t):
    answer = 0
    for i in range(t):
        answer = 2**i + answer
    return n*(answer+1)