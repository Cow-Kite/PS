def solution(order):
    answer = 0
    for baverage in order:
        if "americano" in baverage:
            answer += 4500
        if "cafelatte" in baverage:
            answer += 5000
        if baverage == "anything":
            answer += 4500
    return answer