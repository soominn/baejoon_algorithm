num = int(input())
plus_long_cnt = num // 4
result = 'long int'

for i in range(1, plus_long_cnt):
    result = 'long ' + result

print(result)