def solution(arr, divisor):
    answer = []
    for i in arr :
        if i%divisor == 0 :
            answer.append(i)
    #answer이 빈 리스트일 때
    if answer == [] : 
        answer = [-1]
    # 오름차순
    answer.sort()
    return answer
