def solution(s):
    p_list =[]
    y_list =[]
    for i in s :
        if i == 'p' or i =='P'  :
            p_list.append(i)
        if i == 'y' or i == 'Y':
            y_list.append(i)
    if len(p_list) == len(y_list) :
        answer = True
    if len(p_list) != len(y_list) :
        answer = False
    if len(p_list) == 0 and len(y_list) ==0 :
        answer = True

    return answer