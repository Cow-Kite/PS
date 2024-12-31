A, B = input().split()

A_str = ""
B_str = ""

for elem in A:
    if not elem.isalpha():
        A_str += elem

for elem in B:
    if not elem.isalpha():
        B_str += elem

print(int(A_str)+int(B_str))