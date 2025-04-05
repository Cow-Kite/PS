T = int(input())

for num in range(1, T+1):
    P, Q, R, S, W = map(int, input().split())

    a_price = P * W
    b_price = 0
    price = 0

    if W <= R:
        b_price = Q
    else:
        b_price = Q + ((W - R) * S)

    price = a_price if a_price < b_price else b_price
    print(f'#{num} {price}')