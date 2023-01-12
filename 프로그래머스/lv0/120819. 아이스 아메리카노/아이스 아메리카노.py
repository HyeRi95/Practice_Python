# def solution(money):
#     answer_c = 0
#     for i in range (1000000//5500) : 
#         if money >= 5500 :
#             money = money - 5500
#             answer_c = answer_c + 1 
#         if money < 5500 :
#             break
#     return [answer_c, money]
def solution (money) : 
    answer = [money // 5500, money % 5500]
    return answer