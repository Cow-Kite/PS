self_num = [False] * 10000

for i in range(1, 10000):
    num = str(i)
    answer = i

    for n in num:
        answer += int(n)
    
    if answer < 10000:
        self_num[answer] = True

for i in range(1, len(self_num)):
    if not self_num[i]:
        print(i)
