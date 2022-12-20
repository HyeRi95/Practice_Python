from math import sqrt
def solution(n):
    a = sqrt(n)
    if n%a == 0 :
        return (a+1)**2
    else :
        return -1