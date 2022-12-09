def solution(x):
    a = str(x)
    s=0
    for i in range(len(a)):
        s = s+int(a[i])
        int(a[i])
    print(s)
    if x%s == 0 :
        answer = True
    else :
        answer = False
    return answer