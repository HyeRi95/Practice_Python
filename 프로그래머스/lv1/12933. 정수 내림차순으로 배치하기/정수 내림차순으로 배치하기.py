def solution(n):
    s = list(str(n))
    s.sort(reverse=True)
    # answer = list(map(int,s))
    # answer = ''.join(answer) -- join에는 str 형태만 들어갈수있기때문에 에러 
    a=int(''.join(s))
    return a