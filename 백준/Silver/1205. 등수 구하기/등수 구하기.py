N, new, P = map(int, input().split())
if N==0:
    print(1)
else:
    score = list(map(int, input().split()))

    if N==P and new <= score[-1]:
        print(-1)
    else:
        score.append(new)
        score.sort(reverse=True)

        rank = 1
        for i in range(len(score)):
            if i>0 and score[i]!=score[i-1]:
                rank = i+1
            
            if score[i] == new:
                print(rank)
                break