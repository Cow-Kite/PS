def password(number):
    while True:
        remove = False
        for i in range(len(number) - 1):
            if number[i] == number[i+1]:
                number = number[:i] + number[i+2:]
                remove = True
                break

        if not remove:
            break

    return number


for num in range(1, 11):
    n, number = input().split(' ')
    print(f'#{num} {password(number)}')