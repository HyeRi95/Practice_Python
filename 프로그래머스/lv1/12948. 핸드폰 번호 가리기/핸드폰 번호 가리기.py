# *로 가려야 하는 숫자 범위 지정해 replace 사용해 *로 변환 변환시에 * 갯수는  뒷 4자리 뺀 길이만큼 곱해줌 
# def solution(phone_number):
#     return phone_number.replace(phone_number[0:-4],'*'*(len(phone_number[0:-4])))

# replace 사용안하고 뒷 4자리 뺀 길이만큼 * 출력하고 뒷 4자리 더해서 결과 반환
def solution(phone_number):
    return '*'*(len(phone_number[0:-4])) + phone_number[-4:]
