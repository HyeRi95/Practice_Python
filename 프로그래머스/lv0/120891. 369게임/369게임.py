def solution(order):
    cnt = 0
    for i in str(order) :
        if i in ['3','6','9']:
            cnt = cnt + 1 
            print(i,':',cnt)
    return cnt
        