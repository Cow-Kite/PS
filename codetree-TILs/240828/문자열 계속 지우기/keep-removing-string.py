str_a = input()
str_b = input()

len_a = len(str_a)
len_b = len(str_b)

while True:
    idx = -1

    candidates = len_a - len_b + 1
    for i in range(candidates):
        is_same = True

        for j in range(len_b):
            if str_a[i + j] != str_b[j]:
                is_same = False
                break
        
        if is_same:
            idx = i
            break

    if idx == -1:
        break
    
    str_a = str_a[:idx] + str_a[idx + len_b:]

    len_a = len(str_a)

print(str_a)