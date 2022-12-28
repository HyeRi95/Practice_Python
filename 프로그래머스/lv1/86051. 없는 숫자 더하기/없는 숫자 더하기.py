def solution(numbers):
    a = 0
    for i in range(10):
        a = i+a
    return a - sum(numbers)