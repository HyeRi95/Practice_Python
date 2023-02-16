def solution(cipher, code):
    answer = ''
    for i in range (len(cipher)//code):
        answer = answer + cipher[(code-1)+(code*i)]
    
    return answer