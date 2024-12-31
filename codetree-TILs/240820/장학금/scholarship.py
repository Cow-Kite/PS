score1, score2 = map(int, input().split())
if score1 >= 90 and score2 >= 95:
    print(100000)
elif score1 >= 90 and score2 >= 90:
    print(50000)
else:
    print(0)