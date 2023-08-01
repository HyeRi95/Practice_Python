def solution(s):
    # print(list(map(int, s.split(' '))))
    return ' '.join(map(str, (min(list(map(int, s.split(' ')))), max(list(map(int, s.split(' ')))))))