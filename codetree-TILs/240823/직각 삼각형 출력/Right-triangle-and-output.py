# 변수 선언 및 입력
n = int(input())

# 길이가 n인 직각삼각형을 출력합니다.
for i in range(n):
	for _ in range(2 * i + 1):
		print("*", end="")
	print()