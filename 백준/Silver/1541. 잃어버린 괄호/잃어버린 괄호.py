import sys

expression = sys.stdin.readline().strip()

groups = expression.split('-')

result = sum(map(int, groups[0].split('+'))) # 첫번째 그룹은 모두 더하기 (10+20) -> 10, 20 -> sum(10, 20)

for group in groups[1:]:
    result -=  sum(map(int, group.split('+')))


print(result)