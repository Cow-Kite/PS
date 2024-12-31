s = input()
cnt_1 = 0
cnt_2 = 0

for i in range(0, len(s) - 2):
    if s[i] == 'K' and s[i+1] == 'O' and s[i+2] == 'I':
        cnt_1 += 1
    elif s[i] == 'I' and s[i+1] == 'O' and s[i+2] == 'I':
        cnt_2 += 1

print(cnt_1, cnt_2)