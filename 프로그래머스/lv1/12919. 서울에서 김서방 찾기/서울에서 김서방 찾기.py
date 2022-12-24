# def solution(seoul):
#     answer = ''
#     number = ''
#     for i in range(len(seoul)):
#         if seoul[i] == 'Kim':
#             return ('김서방은 '+str(i)+'에 있다')
        
def solution(seoul):
    return "김서방은 {}에 있다".format(seoul.index('Kim'))
        
            