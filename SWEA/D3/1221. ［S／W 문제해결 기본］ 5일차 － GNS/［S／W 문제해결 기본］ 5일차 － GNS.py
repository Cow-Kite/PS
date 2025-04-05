num_map = {
    "ZRO": 0, "ONE": 1, "TWO": 2, "THR": 3, "FOR": 4,
    "FIV": 5, "SIX": 6, "SVN": 7, "EGT": 8, "NIN": 9
}

# 역 매핑
reverse_map = {v: k for k, v in num_map.items()}

T = int(input())

for _ in range(1, T+1):
    num, length = input().split()
    words = input().split()

    # 문자열 -> 숫자 변환
    numbers = [num_map[word] for word in words]
    numbers.sort()

    # 숫자 -> 문자열 변환
    sorted_words = [reverse_map[num] for num in numbers]

    print(num)
    print(' '.join(sorted_words))