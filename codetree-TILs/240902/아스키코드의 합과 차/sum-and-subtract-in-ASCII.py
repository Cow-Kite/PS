a, b = input().split()
num_a = ord(a)
num_b = ord(b)
hap = num_a + num_b
cha = num_a-num_b if num_a >= num_b else num_b-num_a
print(hap, cha)