N = int(input())
score_li = list(map(int, input().split()))
max_score = max(score_li)

faked_score_li = [score / max_score * 100 for score in score_li]

print(sum(faked_score_li) / len(faked_score_li))