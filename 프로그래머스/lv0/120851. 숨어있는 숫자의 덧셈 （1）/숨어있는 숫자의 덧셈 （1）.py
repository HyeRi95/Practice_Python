def solution(my_string):
    answer = []
    string_list = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    my_string = my_string.upper()
    for i in my_string : 
        if i in string_list :
            pass 
        else :
            answer.append(int(i))
        
            
    return sum(answer)