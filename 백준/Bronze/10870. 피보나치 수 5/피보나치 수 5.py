def recursive(num):
    if num == 0:
        return 0
    if num == 1:
        return 1
    else:
        return recursive(num-2) + recursive(num-1)
    
print(recursive(int(input())))