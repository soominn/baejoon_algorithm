h, m = map(int, input().split())
total_m = h * 60 + m
total_m = total_m - 45

result_h = total_m // 60
result_m = total_m % 60

print('23' if result_h == -1 else result_h, result_m)