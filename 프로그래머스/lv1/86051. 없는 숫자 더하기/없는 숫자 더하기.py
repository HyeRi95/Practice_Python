# 0-9까지의 합을 알고있다고 가정 
def solution(numbers):
    return 45-sum(numbers)

# 0-9까지 리스트로 만들어 풀기
def solution(numbers):
    a = sum([0,1,2,3,4,5,6,7,8,9])
    return a - sum(numbers)

# for문 사용해서 0-9까지 더하기 
def solution(numbers):
    a = 0
    for i in range(10):
        a = i+a
    return a - sum(numbers)