def solution(arr):
    answer =0
    for i in arr : 
        answer = i+answer   
    return  answer/len(arr)