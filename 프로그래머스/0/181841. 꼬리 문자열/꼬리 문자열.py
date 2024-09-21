def solution(str_list, ex):
    answer = ''
    for elem in str_list:
        if ex not in elem:
            answer += elem
    return answer