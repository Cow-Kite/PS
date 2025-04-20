# 1->6->12->18->24
num = int(input())
cnt = 1
max_num = 1

while num > max_num:
    max_num += 6 * cnt
    cnt += 1

print(cnt)