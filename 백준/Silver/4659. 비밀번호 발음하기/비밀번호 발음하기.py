vowels = ['a', 'e', 'i', 'o', 'u']

while True:
    pwd = input()
    if pwd == 'end':
        break
    
    accept = True
    # 모음 하나 이상 포함
    for v in vowels:
        if v in pwd:
            break
    else:
        accept = False

    # 모음이 3개 혹은 자음이 3개 연속되면 안됨
    for i in range(0, len(pwd)-2):
        if pwd[i] in vowels and pwd[i+1] in vowels and pwd[i+2] in vowels:
            accept = False
            break
        elif pwd[i] not in vowels and pwd[i+1] not in vowels and pwd[i+2] not in vowels:
            accept = False
            break
        else:
            continue

    # 같은 글자가 연속으로 나오면 안되나, ee와 oo은 허용함
    for i in range(0, len(pwd)-1):
        if pwd[i] == pwd[i+1]:
            if pwd[i:i+2] == 'ee' or pwd[i:i+2] == 'oo':
                continue
            else:
                accept = False
                break
    
    if accept:
        print(f'<{pwd}> is acceptable.')
    else:
        print(f'<{pwd}> is not acceptable.')