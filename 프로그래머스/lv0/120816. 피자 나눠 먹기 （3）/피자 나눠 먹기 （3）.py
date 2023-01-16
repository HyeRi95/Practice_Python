def solution(slice, n):
    for i in range (1,101,1) : 
        if slice * i >= n : 
            return i
        else :
            pass