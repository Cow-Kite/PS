str1 = input()
str2 = input()
str3 = input()

max_str = max(len(str1), len(str2), len(str3))
min_str = min(len(str1), len(str2), len(str3))

print(max_str-min_str)