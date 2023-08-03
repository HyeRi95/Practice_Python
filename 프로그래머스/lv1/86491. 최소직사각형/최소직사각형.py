def solution(sizes):
    answer = 0 
    for i in range (len(sizes)):
        if sizes[i][0] >= sizes[i][1]:
            pass 
        else :
            w = sizes[i][0]
            sizes[i][0] = sizes[i][1]
            sizes[i][1] = w 
            
    max_w = sizes[0][0]
    max_h = sizes[0][1]
    for i in range(len(sizes)-1) : 
        
        if max_w > sizes[i+1][0] : 
            pass
        else :
            max_w = sizes[i+1][0]
            
    for i in range(len(sizes)-1) : 
        
        if max_h > sizes[i+1][1] : 
            pass
        else :
            max_h = sizes[i+1][1]
            
    return max_w * max_h