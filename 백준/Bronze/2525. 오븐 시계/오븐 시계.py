h, m = map(int, input().split())
plus_m = int(input())

total_m = h * 60 + m + plus_m

result_h = total_m // 60
result_m = total_m % 60

print(result_h % 24 if result_h > 23 else result_h, result_m)