def solution(age):
    age = str(age)
    answer = []
    list_eng = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','s','y','z']
    for i in range (len(age)) : 
        answer.append(list_eng[int(age[i])])
    return  ''.join(answer)