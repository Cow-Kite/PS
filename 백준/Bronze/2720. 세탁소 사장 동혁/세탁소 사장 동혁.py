import sys

T = int(input())

Q = 25 
D = 10
N = 5
P = 1

for _ in range(T):
    change = int(input())
    
    Q_num = change // Q
    change %= Q

    D_num = change // D
    change %= D

    N_num = change // N
    change %= N

    P_num = change // P
    
    print(Q_num, D_num, N_num, P_num)  