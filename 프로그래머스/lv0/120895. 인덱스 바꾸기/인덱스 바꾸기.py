def solution(my_string, num1, num2):
    # print(my_string[num1])
    new_string = list(my_string)
    new_string[num1] = my_string[num2]
    new_string[num2] = my_string[num1]
    return ''.join(new_string)