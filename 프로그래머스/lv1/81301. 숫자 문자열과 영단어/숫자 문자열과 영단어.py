# 딕셔너리로 풀기 
# def solution(s):
#     english = {'zero':'0','one':'1','two':'2','three':'3','four':'4','five':'5',
#                'six':'6','seven':'7','eight':'8','nine':'9'}

#     for key in english:
#         if key in s :
#             s = s.replace(key,english[key])
#     return int(s)

# 리스트로 풀기 
def solution(s):
    words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    for i in range(len(words)):
        s = s.replace(words[i], str(i))

    return int(s)