for num in range(1, 11):
    N = int(input())
    buildings = list(map(int, input().split()))
    good_view = 0

    for i in range(2, len(buildings)-2):
        height = buildings[i]
        surrounding = max(buildings[i-2], buildings[i-1], buildings[i+1], buildings[i+2])

        if height > surrounding:
            good_view += height - surrounding

    print(f'#{num} {good_view}')