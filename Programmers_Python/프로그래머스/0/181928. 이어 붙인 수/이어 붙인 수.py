def solution(num_list):
    a = ''
    b = ''
    for elem in num_list:
        if elem % 2 == 0:
            a += str(elem)
        else:
            b += str(elem)
    answer = int(a) + int(b)
    return answer