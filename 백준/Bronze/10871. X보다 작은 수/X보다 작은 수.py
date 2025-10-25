N, X = map(int, input().split())
num_arr = list(map(int, input().split()))
filter_arr = list(filter(lambda num: X > num, num_arr))

print(' '.join(map(str, filter_arr)))