n = int(input())
hap = 0
score = list(map(float, input().split()))
hap += sum(score)
avg = hap / len(score)
print(f'{avg:.1f}')
if avg >= 4.0:
    print('Perfect')
elif avg >= 3.0:
    print('Good')
else:
    print('Poor')